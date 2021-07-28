import numpy as np
import cv2 as cv
from scipy import stats
def unique(a):
    order = np.lexsort(a.T)
    a = a[order]
    diff = np.diff(a, axis=0)
    ui = np.ones(len(a), 'bool')
    ui[1:] = (diff != 0).any(axis=1) 
    return a[ui]
img = cv.imread('expectedResult.png')
tempImg = img.ravel()
tempTemp = np.reshape(tempImg, (-1, 3))
leftOver = unique(tempTemp)
mode = stats.mode(tempTemp)
print(np.count_nonzero(mode[0]))
print(mode)