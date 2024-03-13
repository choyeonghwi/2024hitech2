import cv2
import numpy as np

img = np.zeros((480, 640, 3), dtype=np.uint8)

COLOR = (0, 255, 255) # BGR : Yellow, 색깔
THICKNESS = 3 # 두께

cv2.line(img, (50, 100), (400, 50), COLOR, THICKNESS, cv2.LINE_8)
# 그릴 위치, 시작 점, 끝 점, 색깔, 두께, 선 종류
cv2.line(img, (50, 200), (400, 150), COLOR, THICKNESS, cv2.LINE_4)
cv2.line(img, (50, 300), (400, 250), COLOR, THICKNESS, cv2.LINE_AA)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()