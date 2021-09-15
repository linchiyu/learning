import cv2


img = cv2.imread('ProjetoSchulz/IMG_20200901_153714.jpg')

img = cv2.resize(img, (700,700))

cv2.imshow('img', img)

cv2.waitKey()