import sys
import numpy as np
import cv2 as cv
import math

hsv_min = np.array((0, 54, 5), np.uint8)
hsv_max = np.array((187, 255, 253), np.uint8)

color_blue = (255,0,0)
color_yellow = (0,255,255)

if __name__ == '__main__':
    fn = r'C:\Users\incum\Desktop\D\33.jpeg'
    img = cv.imread(fn)

    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    thresh = cv.inRange(hsv, hsv_min, hsv_max)
    contours0, hierarchy = cv.findContours(thresh.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # перебираем все найденные контуры в цикле
    for cnt in contours0:
        rect = cv.minAreaRect(cnt) # пытаемся вписать прямоугольник
        box = cv.boxPoints(rect) # поиск четырех вершин прямоугольника
        box = np.int0(box) # округление координат
        center = (int(rect[0][0]),int(rect[0][1]))
        area = int(rect[1][0]*rect[1][1]) # вычисление площади

        # вычисление координат двух векторов, являющихся сторонами прямоугольника
        edge1 = np.int0((box[1][0] - box[0][1], box[1][1] - box[0][1]))
        edge2 = np.int0((box[2][0] - box[1][0], box[2][1] - box[1][1]))

        # выясняем какой вектор больше
        usedEdge = edge1
        if cv.norm(edge2) > cv.norm(edge1):
            usedEdge = edge2
        reference = (1,0) # Горизонтальный вектор, задающий горизонт

        # вычисляем угол между самой длинной стороной прямоугольника и горизонтом
        angle = 180.0/math.pi * math.acos(
            (reference[0] * usedEdge[0] + reference[1] * usedEdge[1]) / (cv.norm(reference) * cv.norm(usedEdge)))

        if area > 500:
            cv.drawContours(img,[box],0,(255,0,0),2) # рисуем прямоугольник
            cv.circle(img, center, 5, color_blue, 2) # рисуем маленький кружок в центре прямоугольника

            # Выводим в кадр величину угла наклона.
            cv.putText(img, "%d" % int(angle), (center[0]+20, center[1]-20),
                        cv.FONT_HERSHEY_SIMPLEX, 1, color_blue, 2)

    cv.imshow('Contours', img)

    cv.waitKey()
    cv.destroyAllWindows()