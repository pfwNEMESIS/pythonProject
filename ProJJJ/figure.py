import cv2 as cv
import numpy as np

class ShapeAnalysis:
def init(self):
    self.shapes = {‘triangle’: 0, ‘rectangle’: 0, ‘polygons’: 0, ‘circles’: 0}

def analysis(self, frame):
    h, w, ch = frame.shape
    result = np.zeros((h, w, ch), dtype=np.uint8)
    # Двоичное изображение
    print("start to detect lines...\n")
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    cv.imshow("input image", frame)

    out_binary, contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for cnt in range(len(contours)):
                 # Извлечь и нарисовать контуры
        cv.drawContours(result, contours, cnt, (0, 255, 0), 2)

                 # Аппроксимация контура
        epsilon = 0.01 * cv.arcLength(contours[cnt], True)
        approx = cv.approxPolyDP(contours[cnt], epsilon, True)

                 # Анализировать геометрию
        corners = len(approx)
        shape_type = ""
        if corners == 3:
            count = self.shapes['triangle']
            count = count+1
            self.shapes['triangle'] = count
                         shape_type = "Треугольник"
        if corners == 4:
            count = self.shapes['rectangle']
            count = count + 1
            self.shapes['rectangle'] = count
                         shape_type = "Прямоугольник"
        if corners >= 10:
            count = self.shapes['circles']
            count = count + 1
            self.shapes['circles'] = count
                         shape_type = "Круг"
        if 4 < corners < 10:
            count = self.shapes['polygons']
            count = count + 1
            self.shapes['polygons'] = count
                         shape_type = "Многоугольник"

                 # Решить центральное положение
        mm = cv.moments(contours[cnt])
        cx = int(mm['m10'] / mm['m00'])
        cy = int(mm['m01'] / mm['m00'])
        cv.circle(result, (cx, cy), 3, (0, 0, 255), -1)

                 # Цветовой анализ
        color = frame[cy][cx]
        color_str = "(" + str(color[0]) + ", " + str(color[1]) + ", " + str(color[2]) + ")"

                 # Рассчитать площадь и периметр
        p = cv.arcLength(contours[cnt], True)
        area = cv.contourArea(contours[cnt])
                 print ("Окружность:% .3f, Область:% .3f Цвет:% s Форма:% s"% (p, area, color_str, shape_type))

    cv.imshow("Analysis Result", self.draw_text_info(result))
    cv.imwrite("D:/test-result.png", self.draw_text_info(result))
    return self.shapes

def draw_text_info(self, image):
    c1 = self.shapes['triangle']
    c2 = self.shapes['rectangle']
    c3 = self.shapes['polygons']
    c4 = self.shapes['circles']
    cv.putText(image, "triangle: "+str(c1), (10, 20), cv.FONT_HERSHEY_PLAIN, 1.2, (255, 0, 0), 1)
    cv.putText(image, "rectangle: " + str(c2), (10, 40), cv.FONT_HERSHEY_PLAIN, 1.2, (255, 0, 0), 1)
    cv.putText(image, "polygons: " + str(c3), (10, 60), cv.FONT_HERSHEY_PLAIN, 1.2, (255, 0, 0), 1)
    cv.putText(image, "circles: " + str(c4), (10, 80), cv.FONT_HERSHEY_PLAIN, 1.2, (255, 0, 0), 1)
    return image
