# Данная программа
# изменяет размер изображения в OpenCV на 700.
import cv2 as cv

wide = 700
f = float(wide) / image.shape[1]
new_size = (wide, int(image.shape[0] * f))
res = cv.resize(image, new_size, interpolation=cv.INTER_AREA)