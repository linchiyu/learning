# In the first Python interactive shell
import time
import numpy as np
import cv2

class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv2.VideoCapture(0)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpeg = cv2.imencode('.jpg', image)
        #return jpeg.tobytes()
        return image

camera = VideoCamera()
img = camera.get_frame()

from multiprocessing import shared_memory
shm = shared_memory.SharedMemory(name='cameraframe', create=True, size=img.nbytes)
print(img.nbytes)
# Now create a NumPy array backed by shared memory
print(shm.buf)
b = np.ndarray(img.shape, dtype=img.dtype, buffer=shm.buf)
print(img.shape)
print(img.dtype)
b[:] = img[:]  # Copy the original data into shared memory

print(type(b))
print('server started - run client now')
i = 0
'''while i < 300:
	b[:] = camera.get_frame()
	i+=1
	time.sleep(0.3)'''


# Clean up from within the first Python shell
print(b)
del b  # Unnecessary; merely emphasizing the array is no longer used
shm.close()
shm.unlink()  # Free and release the shared memory block at the very end
print('server end')