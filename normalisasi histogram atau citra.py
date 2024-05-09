import cv2
from matplotlib import pyplot as plt

img = cv2.imread(r'D:\INSTRUMENTASI CITRA DIGITAL\Kuliah_citra_29_4_24\Modul Praktik 2\rice.tif')

#normalisasi citra/histogram
normalized_img = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)

histogram = cv2.calcHist([img], [0], None, [256], [0, 256])

#tampilkan citra asli
plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Citra Asli')
plt.xticks([]), plt.yticks([])

#tampilkan histogram citra asli
plt.subplot(2, 2, 2)
plt.hist(img.ravel (), 256, [0, 256])
plt.title('Histogram Citra Asli')
plt.xlim(0, 256)

#tampilkan citra yang dinormalisasi
plt.subplot(2, 2, 3)
plt.imshow(img, cmap='gray')
plt.title('Citra Ternormalisasi')
plt.xticks([]), plt.yticks([])

#tampilkan histogram citra yang ternormalisasi
plt.subplot(2, 2, 4)
plt.hist(normalized_img.ravel (), 256, [0, 256])
plt.title('Histogram Citra Ternormalisasi')
plt.xlim(0, 256)

plt.show()
