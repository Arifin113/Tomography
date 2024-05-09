import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread(r'D:\INSTRUMENTASI CITRA DIGITAL\Kuliah_citra_29_4_24\download.jpeg')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
Merah_bawah = np.array ([0, 150, 501])
Merah_atas = np.array ([3, 255, 255])

masking = cv2.inRange(hsv, Merah_bawah, Merah_atas)

img[masking == 255] = [255, 0, 0]

resize_img = cv2.resize(img, (0, 0), fx= 0.5, fy= 0.5)

cv2.imshow('hasil', resize_img)
cv2.waitKey()
cv2.destroyAllWindows()

