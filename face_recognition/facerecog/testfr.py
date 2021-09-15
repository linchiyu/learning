import face_recognition
import cv2
import numpy
import time
import dlib
import imutils


# Load the jpg files into numpy arrays
biden_image = face_recognition.load_image_file("7.jpg")
obama2_image = face_recognition.load_image_file("5.jpg")
obama_image = face_recognition.load_image_file("1.jpg")
unknown_image = face_recognition.load_image_file("2.jpg")

# Get the face encodings for each face in each image file
# Since there could be more than one face in each image, it returns a list of encodings.
# But since I know each image only has one face, I only care about the first encoding in each image, so I grab index 0.
try:
    print(time.time())
    biden_face_encoding = face_recognition.face_encodings(biden_image)[0]
    print(time.time())
    obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
    unknown_face_encoding = face_recognition.face_encodings(unknown_image)[1]
except IndexError:
    print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
    quit()

known_faces = [
    biden_face_encoding,
    obama_face_encoding
]

detector = dlib.get_frontal_face_detector()

img_raw = biden_image
small_frame = cv2.resize(img_raw, (0, 0), fx=0.25, fy=0.25)
rgb_small_frame = small_frame[:, :, ::-1]
print(time.time())
faces = face_recognition.face_locations(rgb_small_frame)
print(time.time())
print(faces)
#-------------------
print('---------')
print(time.time())
img_raw = biden_image
small_frame = cv2.resize(img_raw, (0, 0), fx=0.25, fy=0.25)
gray = cv2.cvtColor(small_frame, cv2.COLOR_BGR2GRAY)
rects = detector(gray, 1)
print(time.time())
print(rects)

print(time.time())
face_encodings = face_recognition.face_encodings(rgb_small_frame, faces)
print(time.time())

#-------------------
print('---------')
print(time.time())
img_raw = obama2_image
small_frame = cv2.resize(img_raw, (0, 0), fx=0.25, fy=0.25)
gray = cv2.cvtColor(small_frame, cv2.COLOR_BGR2GRAY)
rects = detector(gray, 1)
print(time.time())
print(rects)

print(time.time())
face_encodings = face_recognition.face_encodings(rgb_small_frame, faces)
print(time.time())
# results is an array of True/False telling if the unknown face matched anyone in the known_faces array
results = face_recognition.compare_faces(known_faces, unknown_face_encoding)
print(results)

print("Is the unknown face a picture of Biden? {}".format(results[0]))
print("Is the unknown face a picture of Obama? {}".format(results[1]))
print("Is the unknown face a new person that we've never seen before? {}".format(not True in results))
