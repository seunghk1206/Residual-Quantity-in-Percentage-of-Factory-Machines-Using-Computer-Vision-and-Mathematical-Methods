import numpy as np
import cv2 as cv
import collections

def PhotoAnalysis(Dir, actualHeight, actualSideLength, cubicThreshold):
    img = cv.imread(Dir)
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
    # 밑은 디버깅 상황 아니면 주석처리 바람
    cv.imshow('res2',res2)
    cv.waitKey(0)
    cv.destroyAllWindows()
    
    gray = cv.cvtColor(res2, cv.COLOR_BGR2GRAY)
    gray = gray.ravel() # 회색 이미지로 변경
    alpha = collections.Counter(gray) # 통계적 분석. 명확한 설명은 불필요.
    summation = 0 # 변수 선언
    for key, value in alpha.items():
        if max(alpha.keys()) > key:
            pass
        else:
            numerator = value
        summation += value
    percentageWhite = numerator/summation # 사진에서의 하얀/회색 부분의 퍼센트.
    cubicVol = actualHeight*actualSideLength**2 # 깔때기의 직육면체부분의 부피.
    pyramidalVol = (cubicVol*(56-actualHeight)/actualHeight-(actualSideLength*1/3)**3)*1/3 # 깔때기의 피라미드형 부분의 부피 구하는 식. 필요하면 변경 바람. 구체적인 부피를 써도 좋음.
    totalVolume = cubicVol+pyramidalVol # 전체 깔때기의 부피
    cubicThreshold = pyramidalVol/totalVolume
    if percentageWhite >= cubicThreshold:
        percentageCube = cubicVol*(percentageWhite)**(1/2)
        return (percentageCube+pyramidalVol)/totalVolume
    else:
        percentagePyramidal = pyramidalVol*(percentageWhite/cubicThreshold)**(3/2)
        # 2a^2+b^2 = c^2 --> k(2a^2+b^2)^(1/2)= k c #a^2*b
        return percentagePyramidal/totalVolume

def PhotoAnalysisDark(Dir, actualHeight, actualSideLength, cubicThreshold):#만약 깔때기에 넣는 물체가 깔때기의 색보다 어두울 경우에 쓰는 함수입니다.
    return 1- PhotoAnalysis(Dir, actualHeight, actualSideLength, cubicThreshold)