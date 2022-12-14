#อ่านภาพ
import cv2
img = cv2.imread("image/cat.jpg")
print(type(img.ndim))
#ออกมาเป็น array 3 มิติ
print(img)