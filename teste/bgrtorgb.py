import cv2

image = cv2.imread('f1.jpg')

image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

cv2.imshow('a', image)
cv2.waitKey(0)
cv2.destroyAllWindows()