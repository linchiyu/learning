import base64
from PIL import Image
from io import BytesIO
with open("f1.jpg", "rb") as img_file:
    my_string = base64.b64encode(img_file.read())

#print(my_string)
print(my_string.decode('utf-8'))
base64image = my_string.decode('utf-8')

im = Image.open(BytesIO(base64.b64decode(my_string)))
im.save('image1.png', 'PNG')

my_string = my_string.decode('utf-8')

#im = Image.open(BytesIO(base64.b64decode(my_string)))
im = Image.open(BytesIO(base64.b64decode(my_string)))
im.save('image2.png', 'PNG')
