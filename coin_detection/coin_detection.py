import cv2
import numpy as np
img=cv2.imread('coin_detection/coin.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray_blur=cv2.GaussianBlur(gray,(15,15),0)
thresh=cv2.adaptiveThreshold(gray_blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,1)
# cv2.imwrite("coin_detection/gray.jpg",gray)
# cv2.imwrite("coin_detection/gray_blur.jpg",gray_blur)
# cv2.imwrite("coin_detection/thresh.jpg",thresh)
cv2.imshow("Output",thresh)
cv2.waitKey(0)
#ปิด
cv2.destroyAllWindows()