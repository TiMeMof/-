import numpy as np
import cv2
#线段绘制
canvas = np.ones((300, 300, 3), np.uint8)*255

canvas = cv2.line(canvas, (50, 50), (250, 250), (1, 222, 3), 3)
canvas = cv2.line(canvas, (250, 50), (50, 250), (1, 222, 3), 3)
canvas = cv2.line(canvas, (50, 50), (250, 50), (111, 2, 3), 3)
canvas = cv2.line(canvas, (250, 50), (250, 250), (111, 2, 3), 3)
canvas = cv2.line(canvas, (250, 250), (50, 250), (111, 2, 3), 3)
canvas = cv2.line(canvas, (50, 250), (50, 50), (111, 2, 3), 3)
cv2.imshow("lines", canvas)
#矩形绘制
six = np.ones((300, 300, 3), np.uint8)
six = cv2.rectangle(six, (23, 23), (233, 233), (111, 2, 3), 20)
cv2.imshow("rectangles", six)
cv2.waitKey()
cv2.destroyAllWindows()
