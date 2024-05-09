# impor fungsi pengolahan citra dari library opencv
import cv2

import numpy as np

#membaca citra dalam bentuk matrix
citra = cv2.imread('D:\INSTRUMENTASI CITRA DIGITAL\Kuliah_citra_29_4_24\wallpaperflare.com_wallpaper (1).jpg')
print(citra)

#menampilkan ukuran citra
print(citra.shape)

#mengambil ukuran citra dari ukuran asli dan memasukkan pada variabel
height, width, channels = citra.shape
lebar = width/2             #jika gambar diperbesar  >>>>>>>  lebar = width*2
tinggi = height/2           #jika gambar diperbesar  >>>>>>>  tinggi = height*2

#ubah ukuran citra
citra_kecil = cv2.resize(citra, (int(lebar), int(tinggi)))     #jika gambar diperkecil >>>>> citra = cv2.resize(citra, (int(lebar), int(tinggi)))

#periksa apakah citra berhasil dibaca
if citra is not None:
    #tampilkan citra menggunakan opencv
    cv2.imshow('gojo satoru', citra_kecil)
    #membiarkan citra tetap tampil sambai tombol apapun ditekan 
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Gagal membaca citra, pastikan nama file dan path-nya benar serta coding tidak typo")

#menyimpan citra
cv2.imwrite('D:\INSTRUMENTASI CITRA DIGITAL\Gojo.tiff', citra)

#Konversi citra integer 8 bit ke citra float (decimal)
image_float = citra.astype(float)/255.0
print(image_float)
cv2.imshow('float', image_float)
cv2.waitKey()

#konversi citra ke integer 16
normalizaze_image = (citra.astype(np.float32) / 255.0) * 65535.0
image_int16 = citra.astype(np.uint16)*256
print(image_int16)
cv2.imshow('gojo16', image_int16)
cv2.waitKey()

#konversi citra ke grayscale
citra_gray = cv2.cvtColor(citra, cv2.COLOR_BGR2GRAY)
cv2.imshow('grayscale', citra_gray)
cv2.waitKey()

#konversi citra ke biner
_, citra_biner = cv2.threshold(citra_gray, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('citra biner', citra_biner)
cv2.waitKey()

