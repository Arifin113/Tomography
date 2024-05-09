import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread(r'D:\INSTRUMENTASI CITRA DIGITAL\Kuliah_citra_29_4_24\wallpaperflare.com_wallpaper (1).jpg')

#High pass filter
hasil = cv2.Laplacian(img, cv2.CV_64F)
hasil = np.uint8(np.absolute(hasil))

#tampilkan citra asli
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Citra Asli')
plt.xticks([]), plt.yticks([])

#tampilkan citra hasil threshold
plt.subplot(1, 2, 2)
plt.imshow(hasil, cmap='gray')
plt.title('Citra hasil olah')
plt.xticks([]), plt.yticks([])

plt.show()