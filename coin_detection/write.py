
import cv2
import numpy as np

cap = cv2.imread("coin_detection/coin.jpg")
gray=cv2.cvtColor(cap,cv2.COLOR_BGR2GRAY) 
gray_blur=cv2.GaussianBlur(gray,(15,15),3)       #แปลงภาพสีให้เป็นเกรย์สเกล
thresh=cv2.adaptiveThreshold(gray_blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,1)
kernel=np.ones((3,3),np.uint8)
closing=cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernel,iterations=5)
result_img=closing.copy()
# cv2.imshow("Show",gray_blur)
# cv2.waitKey(0)
cv2.imwrite("coin_detection/gray.jpg",gray)
cv2.imwrite("coin_detection/gray_blur.jpg",gray_blur)
cv2.imwrite("coin_detection/thresh.jpg",thresh)
cv2.imwrite("coin_detection/closing.jpg",closing)
cv2.destroyAllWindows()