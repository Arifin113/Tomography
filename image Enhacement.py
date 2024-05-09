import cv2
from matplotlib import pyplot as plt

img = cv2.imread(r'D:\INSTRUMENTASI CITRA DIGITAL\Kuliah_citra_29_4_24\Modul Praktik 2\rice.tif')

histogram = cv2.calcHist([img], [0], None, [256], [0, 256])

cv2.imshow('gojo', img)
cv2.waitKey()

plt.plot(histogram, color='black')
plt.title('histogram')
plt.xlim([0, 256])
plt.show()
