# Импортируем нужные библиотеки.
import numpy as np
import cv2

# Делаем управление
def nothing(args):pass
cv2.namedWindow("setup")
cv2.namedWindow("setup2")
cv2.createTrackbar("b1", "setup", 0, 255, nothing)
cv2.createTrackbar("g1", "setup", 0, 255, nothing)
cv2.createTrackbar("r1", "setup", 0, 255, nothing)
cv2.createTrackbar("b2", "setup", 255, 255, nothing)
cv2.createTrackbar("g2", "setup", 255, 255, nothing)
cv2.createTrackbar("r2", "setup", 255, 255, nothing)
cv2.createTrackbar("blur", "setup2", 0, 10, nothing)

fileName = (r'C:\Users\incum\Desktop\D\rects.jpeg')

image = cv2.imread(fileName)

wide = 500                                    # ИЗМЕНЕНИЕ РАЗМЕРА!
f = float(wide) / image.shape[1]                # ИЗМЕНЕНИЕ РАЗМЕРА!
new_size = (wide, int(image.shape[0] * f))      # ИЗМЕНЕНИЕ РАЗМЕРА!
image = cv2.resize(image, new_size,             # ИЗМЕНЕНИЕ РАЗМЕРА!
               interpolation = cv2.INTER_AREA)  # ИЗМЕНЕНИЕ РАЗМЕРА!


# подбираем параметры цветового фильтра для выделения
# нашего объекта (указанные числовые значения могут
# отличаться)
while True:
    hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    r1 = cv2.getTrackbarPos('r1', 'setup')
    g1 = cv2.getTrackbarPos('g1', 'setup')
    b1 = cv2.getTrackbarPos('b1', 'setup')
    r2 = cv2.getTrackbarPos('r2', 'setup')
    g2 = cv2.getTrackbarPos('g2', 'setup')
    b2 = cv2.getTrackbarPos('b2', 'setup')
    blur = cv2.getTrackbarPos('blur', 'setup2')
    hsv_min = np.array((r1, g1, b1), np.uint8)
    hsv_max = np.array((r2, g2, b2), np.uint8)
    img_bl = cv2.medianBlur(hsv_img, 1+blur*2) # сглаживание изображения


    # применяем цветовой фильтр к исходному изображению,
    # результат записываем в переменную img_mask
    img_mask = cv2.inRange(img_bl, hsv_min, hsv_max)
    #img_m = cv2.bitwise_and(image, image, mask = img_mask)
    # ищем контуры и записываем их в переменную contours
    # в режиме поиска всех контуров без группировки
    # cv2.RETR_LIST, для хранения контуров используем
    # метод cv2.CHAIN_APPROX_SIMPLE
    contours, hierarchy = cv2.findContours( img_mask,
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
        if area > 1000:
            # Поиск вершин прямоугольника
            box = cv2.boxPoints(rect)
            # Округляем значения.
            box = np.int0(box)
            # Рисуем прямоугольник поверх исходного изображения
            # цвет чёрный, толщина линии 2.
            cv2.drawContours(image, [box], -1, (255, 0, 0), 3)

         # Выводим итоговое значение.
    cv2.imshow('img', img_mask)
    if cv2.waitKey(33) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()