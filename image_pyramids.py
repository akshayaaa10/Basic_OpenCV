import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("lena.jpg")
# lr1=cv2.pyrDown(img)
# lr2=cv2.pyrDown(lr1)
# hr2=cv2.pyrUp(lr2)

layer=img.copy()
gp=[layer]

for i in range(6):
    layer=cv2.pyrDown(layer)
    gp.append(layer)
    cv2.imshow(str(i), layer)

layer= gp[5]
cv2.imshow('Upper Level Gaussian Pyramin', layer)
lp = [layer]

for i in range(5, 0, -1):
    # print(i)
    gaussian_extended=cv2.pyrUp(gp[i])
    laplacian=cv2.subtract(gp[i-1],gaussian_extended)
    cv2.imshow(str(i), laplacian)

cv2.imshow("Original image", img)
# cv2.imshow("pyrDown1 image", lr1)
# cv2.imshow("pyRdown2 image", lr2)
# cv2.imshow("pyRUp1 image", hr2)
cv2.waitKey(0)
cv2.destroyAllWindows()