#https://docs.opencv.org/master/dc/d2e/tutorial_py_image_display.html

import cv2 as cv
import numpy as np

#img = cv.imread("boy.jpg", cv.IMREAD_GRAYSCALE)
#img1 = cv.imread("boy.jpg", -1)
#img2 = cv.imread("boy.jpg", 0)
#img3 = cv.imread("boy.jpg", 1)
img1 = cv.imread("boy.jpg",cv.WINDOW_NORMAL)

cv.imshow('img1',img1)
#cv.imshow('im2',img2)
#cv.imshow('img3',img3)
cv.waitKey(0)
cv.destroyAllWindows()
