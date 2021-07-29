import numpy as np
import cv2 as cv
import collections
img = cv.imread('expectedResult.png')
Z = img.reshape((-1,3))
# convert to np.float32
Z = np.float32(Z)
# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 2
ret,label,center=cv.kmeans(Z,K,None,criteria,10,cv.KMEANS_RANDOM_CENTERS)
# Now convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))
cv.imshow('res2',res2)
cv.waitKey(0)
cv.destroyAllWindows()

gray = cv.cvtColor(res2, cv.COLOR_BGR2GRAY)
gray = gray.ravel()
alpha = collections.Counter(gray)
summation = 0
for key, value in alpha.items():
    if max(alpha.keys()) > key:
        pass
    else:
        numerator = value
    summation += value
percentageWhite = numerator/summation
actualHeight = 20#cm
actualSideLength = 100#cm
cubicVol = actualHeight*actualSideLength**2
pyramidalVol = (cubicVol*1.5-10*10*10)*1/3
totalVolume = cubicVol+pyramidalVol
cubicThreshold = 0.6
pyramidalThreshold = 0.1
if percentageWhite > cubicThreshold:
    #20cm height
    #rate of decrease
    percentageHeight = ((percentageWhite-cubicThreshold)/(1-cubicThreshold))**(1/2)
    print((percentageHeight*actualHeight*actualSideLength**2+pyramidalVol)/totalVolume)
elif percentageWhite > pyramidalThreshold:
    percentagePyramidal = (percentageWhite/cubicThreshold)
    # 2a^2+b^2 = c^2 --> k(2a^2+b^2)^(1/2)= k c #a^2*b
    print(pyramidalVol*(percentagePyramidal)/totalVolume)
else:
    print(0)

