import sys
import cv2 as cv
import numpy as np


# Параметры цветового фильтра.
hsv_min = np.array((2, 28, 65), np.uint8)
hsv_max = np.array((26, 238, 255), np.uint8)

if __name__ == '__main__':
    print(__doc__)

    fn = r'C:\Users\incum\Desktop\D\2.jpeg'
    img = cv.imread(fn)

    # Меняем цветовую модель с BGR на HSV.
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    # Применяем цветовой фильтр.
    thresh = cv.inRange(hsv, hsv_min, hsv_max)

    # Ищем контуры и складируем их в переменную contours.
    contours, hierarchy = cv.findContours(thresh.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # Отображаем контуры поверх изображений.
    cv.drawContours(img, contours, -1, (255,0,0), 3, cv.LINE_AA, hierarchy, 2)

    # Выводим итоговое изображение в окно.
    cv.imshow('contours', img)

    cv.waitKey()
    cv.destroyAllWindows()