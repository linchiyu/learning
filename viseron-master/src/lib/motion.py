import logging
from queue import Empty

import cv2
import imutils


class MotionDetection:
    def __init__(self, config, motion_event):
        self._logger = logging.getLogger(__name__ + "." + config.camera.name_slug)
        if getattr(config.motion_detection.logging, "level", None):
            self._logger.setLevel(config.motion_detection.logging.level)
        elif getattr(config.camera.logging, "level", None):
            self._logger.setLevel(config.camera.logging.level)

        self.avg = None
        self._motion_detected = False
        self.motion_area = 0
        self.min_motion_area = config.motion_detection.area
        self.motion_frames = config.motion_detection.frames
        self.motion_event = motion_event

    def detect(self, frame):
        gray = cv2.cvtColor(
            frame["frame"].get_resized_frame(frame["decoder_name"]), cv2.COLOR_RGB2GRAY
        )
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        gray = gray.get()  # Convert from UMat to Mat

        # if the average frame is None, initialize it
        if self.avg is None:
            self.avg = gray.astype("float")
            return 0

        # accumulate the weighted average between the current frame and
        # previous frames, then compute the difference between the current
        # frame and running average.
        # Lower value makes the motion detection more sensitive.
        cv2.accumulateWeighted(gray, self.avg, 0.1)
        frame_delta = cv2.absdiff(gray, cv2.convertScaleAbs(self.avg))

        # threshold the delta image, dilate the thresholded image to fill
        # in holes, then find contours on thresholded image
        thresh = cv2.threshold(frame_delta, 5, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations=2)
        cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)

        max_contour = max([cv2.contourArea(c) for c in cnts], default=0)
        return max_contour

    # @profile
    def motion_detection(self, motion_queue):
        _motion_frames = 0

        while True:
            try:
                frame = motion_queue.get()

                max_contour = self.detect(frame)

                if max_contour > self.min_motion_area:
                    self.motion_area = max_contour
                    _motion_found = True
                else:
                    _motion_found = False

                if _motion_found:
                    _motion_frames += 1
                    self._logger.debug(
                        "Motion frames: {}, "
                        "area: {}".format(_motion_frames, max_contour)
                    )

                    if _motion_frames >= self.motion_frames:
                        frame["frame"].motion = True
                        if not self.motion_detected:
                            self.motion_detected = True
                        continue
                else:
                    _motion_frames = 0

            except Empty:
                self._logger.error("Frame not grabbed for motion detector")

            if self.motion_detected:
                self.motion_detected = False

    @property
    def motion_detected(self):
        return self._motion_detected

    @motion_detected.setter
    def motion_detected(self, _motion_detected):
        self._motion_detected = _motion_detected

        if _motion_detected:
            self.motion_event.set()

        else:
            self._logger.debug("Motion has ended")
            self.motion_event.clear()
