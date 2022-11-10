import numpy as np
import cv2

def nothing(args):pass
cv2.namedWindow("setup")
cv2.namedWindow("setup2")
cv2.createTrackbar("h1", "setup", 0, 255, nothing)
cv2.createTrackbar("s1", "setup", 0, 255, nothing)
cv2.createTrackbar("v1", "setup", 0, 255, nothing)
cv2.createTrackbar("h2", "setup", 255, 255, nothing)
cv2.createTrackbar("s2", "setup", 255, 255, nothing)
cv2.createTrackbar("v2", "setup", 255, 255, nothing)
cv2.createTrackbar("blur", "setup2", 0, 10, nothing)



img = cv2.imread(r'C:\Users\incum\Desktop\D\1.jpg') # загрузка изображения
percent = 48.5
width = int(img.shape[1] * percent / 100)
height = int(img.shape[0] * percent / 100)
dim = (width, height)
img = cv2.resize(img, dim)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
while True:

   # считываем значения бегунков
   h1 = cv2.getTrackbarPos('h1', 'setup')
   s1 = cv2.getTrackbarPos('s1', 'setup')
   v1 = cv2.getTrackbarPos('v1', 'setup')
   h2 = cv2.getTrackbarPos('h2', 'setup')
   s2 = cv2.getTrackbarPos('s2', 'setup')
   v2 = cv2.getTrackbarPos('v2', 'setup')
   blur = cv2.getTrackbarPos('blur', 'setup2')
   min_h = np.array((h1, s1, v1), np.uint8)
   max_h = np.array((h2, s2, v2), np.uint8)
# сглаживание изображения
   img_bl = cv2.medianBlur(hsv, 1+blur*2)
   img_mask = cv2.inRange(img_bl, min_h, max_h)
   img_m = cv2.bitwise_and(hsv, hsv, mask = img_mask)

   # ищем контуры и записываем их в переменную contours
   # в режиме поиска всех контуров без группировки
   # cv2.RETR_LIST, для хранения контуров используем
   # метод cv2.CHAIN_APPROX_SIMPLE
   contours, hierarchy = cv2.findContours(img_mask,
                                          cv2.RETR_LIST,
                                          cv2.CHAIN_APPROX_SIMPLE)

   # Перебираем контуры.
   for icontour in contours:
      # Ищем прямоугольники.
      rect = cv2.minAreaRect(icontour)
      # Вычисляем площадь
      area = int(rect[1][0] * rect[1][1])
      # Если площадь больше указанного значения, эти
      # контуры выводим,
      # значения подбираются экспериментально.
      if area > 300:
         # Поиск вершин прямоугольника
         box = cv2.boxPoints(rect)
         # Округляем значения.
         box = np.int0(box)
         # Рисуем прямоугольник поверх исходного изображения
         # цвет чёрный, толщина линии 2.
         cv2.drawContours(img_m, [box], -1, (255, 0, 0), 2)

   cv2.imshow('img', img_m)
   if cv2.waitKey(33) & 0xFF == ord('q'):
      break
cv2.destroyAllWindows()