import cv2
import time

def fadeIn (img1, img2, elapse=10): #pass images here to fade between
        #while True:
        for IN in range(0,elapse):
                fadein = IN/float(elapse)
                dst = cv2.addWeighted( img1, 1-fadein, img2, fadein, 0)#linear $
                cv2.imshow('window', dst)
                k = cv2.waitKey(100)
                if k == ord('q'):
                        break
                print (fadein)
                if fadein == 1.0: #blendmode mover
                        fadein = 1.0

        return # exit function

im1 = cv2.imread('img1.jpg')
im2 = cv2.imread('img2.jpg')

im1 = cv2.resize(im1, (800, 800))
im2 = cv2.resize(im2, (800, 800))

cv2.imshow('window', im1)
cv2.waitKey(300)
fadeIn(im1, im2)
cv2.imshow('window', im2)
cv2.waitKey(0)