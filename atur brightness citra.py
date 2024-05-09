import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread(r'D:\INSTRUMENTASI CITRA DIGITAL\Kuliah_citra_29_4_24\Modul Praktik 2\rice.tif')

#Mengatur Kecerahan Citra
faktor_kecerahan = 50
citra_hasil = np.clip(img.astype(np.int32) + faktor_kecerahan, 0, 255) .astype(np.uint8)

#mengatur kontras citra
contrast_factor = 1.5
hasil_kontras = np.clip(img.astype(np.float32) * contrast_factor, 0, 255) .astype(np.uint8)

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

#tampilkan citra yang tercerahkan
plt.subplot(2, 2, 3)
plt.imshow(hasil_kontras, cmap='gray')
plt.title('Citra Hasil Kontras')
plt.xticks([]), plt.yticks([])

#tampilkan histogram citra yang tercerahkan
plt.subplot(2, 2, 4)
plt.hist(hasil_kontras.ravel (), 256, [0, 256])
plt.title('Histogram Citra Hasil Kontras')
plt.xlim(0, 256)

plt.show()