# Подключаем библиотеки
import numpy as np
import cv2 as cv

# Путь к файлу.
filePath = r'C:\Users\incum\Desktop\D\1.jpg'

# Считываем данные графического файла и записываем в
# переменную image.
image = cv.imread(filePath)

wide = 400                                     # ИЗМЕНЕНИЕ РАЗМЕРА!
f = float(wide) / image.shape[1]                # ИЗМЕНЕНИЕ РАЗМЕРА!
new_size = (wide, int(image.shape[0] * f))      # ИЗМЕНЕНИЕ РАЗМЕРА!
res = cv.resize(image, new_size,                # ИЗМЕНЕНИЕ РАЗМЕРА!
               interpolation = cv.INTER_AREA)   # ИЗМЕНЕНИЕ РАЗМЕРА!

# Конвертируем из BGR в HSV и присваиваем значение в hsv_image.
hsv_image = cv.cvtColor(image, cv.COLOR_BGR2HSV)
hsv_res = cv.cvtColor(res, cv.COLOR_BGR2HSV)    # ИЗМЕНЕНИЕ РАЗМЕРА!

# Подбираем параметры цветового фильтра.
hsv_min = np.array((20, 28, 65), np.uint8)
hsv_max = np.array((26, 238, 255), np.uint8)

# Применяем цветовую маску к изображению.
hsv_msk = cv.inRange(hsv_image, hsv_min, hsv_max)
hsv_msk = cv.inRange(hsv_res, hsv_min, hsv_max) # ИЗМЕНЕНИЕ РАЗМЕРА!

# Ищем контуры и записываем их в переменную contours
# в режиме поиска всех контуров без группировки
# cv.RETR_LIST, для хранения контуров используем
# метод cv.CHAIN_APPROX_SIMPLE
contours, hierarchy = cv.findContours( hsv_msk, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

# Отображаем все контуры поверх изображения
# цвет синий, толщина линии 3, сглаженная.
#cv.drawContours(image, contours, -1, (255, 0, 0),
#                3, cv.LINE_AA, hierarchy, 2)
cv.drawContours(res, contours, -1, (255, 0, 0), # ИЗМЕНЕНИЕ РАЗМЕРА!
                2, cv.LINE_AA, hierarchy, 2)    # ИЗМЕНЕНИЕ РАЗМЕРА!

# Выводим итоговое изображение.
cv.imshow('Contours', res)

# Ждём нажатие любой клавиши и закрываем все окна.
cv.waitKey()
cv.destroyAllWindows()