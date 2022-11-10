# Импортируем нужные библиотеки.
import numpy as np
import cv2




fileName = (r'C:\Users\incum\Desktop\D\1.jpg')

image = cv2.imread(fileName)

wide = 500                                     # ИЗМЕНЕНИЕ РАЗМЕРА!
f = float(wide) / image.shape[1]                # ИЗМЕНЕНИЕ РАЗМЕРА!
new_size = (wide, int(image.shape[0] * f))      # ИЗМЕНЕНИЕ РАЗМЕРА!
image = cv2.resize(image, new_size,                # ИЗМЕНЕНИЕ РАЗМЕРА!
               interpolation = cv2.INTER_AREA)

hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# подбираем параметры цветового фильтра для выделения
# нашего объекта (указанные числовые значения могут
# отличаться)
hsv_min = np.array((0, 0, 217), np.uint8)
hsv_max = np.array((56, 250, 255), np.uint8)

# применяем цветовой фильтр к исходному изображению,
# результат записываем в переменную hsv_msk
hsv_msk = cv2.inRange( hsv_img, hsv_min, hsv_max )

# ищем контуры и записываем их в переменную contours
# в режиме поиска всех контуров без группировки
# cv2.RETR_LIST, для хранения контуров используем
# метод cv2.CHAIN_APPROX_SIMPLE
contours, hierarchy = cv2.findContours( hsv_msk,
                                        cv2.RETR_LIST,
                                cv2.CHAIN_APPROX_SIMPLE)

# Перебираем контуры.
for icontour in contours:
    # Ищем прямоугольники.
    rect = cv2.minAreaRect(icontour)
    # Вычисляем площадь
    area = int(rect[1] [0] * rect [1] [1])
    # Если площадь больше указанного значения, эти
    # контуры выводим,
    # значения подбираются экспериментально.
    if area > 400:
        # Поиск вершин прямоугольника
        box = cv2.boxPoints(rect)
        # Округляем значения.
        box = np.int0(box)
        # Рисуем прямоугольник поверх исходного изображения
        # цвет чёрный, толщина линии 2.
        cv2.drawContours(image, [box], -1, (0, 255, 0), 2)

# Выводим итоговое значение.
cv2.imshow('contours', image)

# Нажимаем любую клавишу и закрываем окна.
cv2.waitKey()
cv2.destroyAllWindows()