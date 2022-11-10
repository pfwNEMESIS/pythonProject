# Подключаем библиотеки Numpy и OpenCV
import numpy as np
import cv2 as cv

# Задаем путь к файлу с картинкой.
fileName = r'C:\Users\incum\Desktop\D\3.jpeg'

# Считываем данные графического файла в переменную
# image
image = cv.imread(fileName)

# Изменяем размер изображения (функция по желанию!)
wide = 700
f = float(wide) / image.shape[1]
new_size = (wide, int(image.shape[0] * f))
res = cv.resize(image, new_size, interpolation=cv.INTER_AREA)

# конвертируем исходное изображение в цветовую модель
# HSV, результат записываем в переменную hsv_res
hsv_img = cv.cvtColor(res, cv.COLOR_BGR2HSV)

# Подбираем параметры цветового фильтра
# (цифры могут быть разными в зависимости от цвета)
hsv_min = np.array((50, 150, 155), np.uint8)
hsv_max = np.array((70, 255, 200), np.uint8)

# Применяем цветовую маску на изображение.
hsv_msk = cv.inRange(hsv_img, hsv_min, hsv_max)

# Ищем контуры в режиме поиска ВСЕХ контуров
# без группировки cv.RETR_LIST, для хранения контуров
# используем метод cv.CHAIN_APPROX_SIMPLE.
contours, hierarchy = cv.findContours(hsv_msk, cv.RETR_LIST,
                                      cv.CHAIN_APPROX_SIMPLE)

# Перебираем все найденные контуры.
for icontour in contours:

    # Ищем прямоугольник, результат записываем в rect.
    rect = cv.minAreaRect(icontour)

    # Ищем вершины прямоугольника, записываем в box.
    box = cv.boxPoints(rect)

    # Округляем координаты вершин.
    box = np.int0(box)

    # Рисуем прямоугольник поверх исходного изображения
    # синим цветом, толщина линии 3, рисуем объект [box]
    cv.drawContours(res, [box], -1, (255, 0, 0), 3)

# Выводим итоговое изображение.
cv.imshow('contours', res)

# Ждём нажатия клавиши.
cv.waitKey()
cv.destroyAllWindows()