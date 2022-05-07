import numpy as np
import cv2

canvas = np.ones((300, 300, 3), np.uint8)*111

canvas = cv2.line(canvas, (50, 50), (250, 250), (111, 222, 333), 3)

cv2.imshow("lines", canvas)
cv2.waitKey()
cv2.destroyAllWindows()
