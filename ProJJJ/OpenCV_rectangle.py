import sys
import numpy as np
import cv2 as cv

hsv_min = np.array((0, 54, 5), np.uint8)
hsv_max = np.array((187, 255, 253), np.uint8)

if __name__ == '__main__':
    fn = r'C:\Users\incum\Desktop\D\34.jpeg'
    img = cv.imread(fn)

    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    thresh = cv.inRange(img, hsv_min, hsv_max)
    contours0, hierarchy = cv.findContours(thresh.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # Перебираем все найденные контуры.
    for cnt in contours0:
        rect = cv.minAreaRect(cnt) # Пытаемся вписать прямоугольник
        box = cv.boxPoints(rect) # Поиск четырех вершин прямоугольника
        box = np.int0(box) # Округление координат
        area = int(rect[1][0] * rect[1][1])
        if area > 500:
            cv.drawContours(img,[box],0,(255, 0, 0),2) # Рисуем прямоугольник

    cv.imshow('Contours', img) # Вывод обработанного кадра

    cv.waitKey()
    cv.destroyAllWindows()