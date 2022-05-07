import cv2
import numpy as np

c = cv2.imread('C://Users//TiNoMof//PycharmProjects//pythonProject//g.jpg', 1)
bgra = cv2.cvtColor(a, cv2.COLOR_BGR2BGRA)

b, g, r, a = cv2.split(bgra)
a[:, :] = 111
fixed = cv2.merge([b, g, r, a])
cv2.imshow("a", fixed)
cv2.imwrite("E://aa.png", bgra)
cv2.imwrite("E://bb.png", fixed)
cv2.waitKey()
cv2.destroyAllWindows()
