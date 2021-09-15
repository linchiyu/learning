import face_recognition
image = face_recognition.load_image_file("2.png")
image = face_recognition.load_image_file("1.jpg")
#image = image[:,:,::-1]
face_location = face_recognition.face_locations(image)
print(face_location)

x = face_recognition.face_encodings(image, face_location)

print(x)