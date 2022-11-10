import sys
import numpy as np
import cv2 as cv

hsv_min = np.array((0, 54, 5), np.uint8)
hsv_max = np.array((187, 255, 253), np.uint8)

if __name__ == '__main__':
    fn = (r'C:\Users\incum\Desktop\D\1.jpg')  # имя файла, который будем анализировать
    img = cv.imread(fn)

    wide = 500 # ИЗМЕНЕНИЕ РАЗМЕРА!
    f = float(wide) / img.shape[1]  # ИЗМЕНЕНИЕ РАЗМЕРА!
    new_size = (wide, int(img.shape[0] * f))  # ИЗМЕНЕНИЕ РАЗМЕРА!
    img = cv.resize(img, new_size,  # ИЗМЕНЕНИЕ РАЗМЕРА!
                       interpolation=cv.INTER_AREA)  # ИЗМЕНЕНИЕ РАЗМЕРА!

    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)  # меняем цветовую модель с BGR на HSV
    thresh = cv.inRange(hsv, hsv_min, hsv_max)  # применяем цветовой фильтр
    contours0, hierarchy = cv.findContours(thresh.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # перебираем все найденные контуры в цикле
    for cnt in contours0:
        rect = cv.minAreaRect(cnt)  # пытаемся вписать прямоугольник
        box = cv.boxPoints(rect)  # поиск четырех вершин прямоугольника
        box = np.int0(box)  # округление координат
        area = int(rect[1][0] * rect[1][1])  # вычисление площади
        if area > 500:
            cv.drawContours(img, [box], 0, (255, 0, 0), 2)

    cv.imshow('contours', img)  # вывод обработанного кадра в окно

    cv.waitKey()
    cv.destroyAllWindows()