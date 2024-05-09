import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread(r'D:\INSTRUMENTASI CITRA DIGITAL\Kuliah_citra_29_4_24\Modul Praktik 2\Taz_noise.bmp')
citra_terfilter = cv2.medianBlur(img, 3)

#tampilkan citra asli
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Citra Asli')
plt.xticks([]), plt.yticks([])

#tampilkan citra hasil kontras
plt.subplot(1, 2, 2)
plt.imshow(citra_terfilter, cmap='gray')
plt.title('Citra terfilter median')
plt.xticks([]), plt.yticks([])

plt.show()