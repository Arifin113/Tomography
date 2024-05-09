import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread(r'D:\INSTRUMENTASI CITRA DIGITAL\Kuliah_citra_29_4_24\wallpaperflare.com_wallpaper (1).jpg')
#citra_terfilter = cv2.medianBlur(img, 3)

# low pass filter
kernel = np.array([[0, 1/8, 0],
                   [1/8, 1/2, 1/8],
                   [0, 1/8, 0]], dtype=np.float32)
hasil = cv2.filter2D(img, -1, kernel)

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