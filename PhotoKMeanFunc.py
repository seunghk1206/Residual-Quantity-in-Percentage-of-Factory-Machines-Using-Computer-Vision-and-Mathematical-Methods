import numpy as np
import cv2 as cv

def PhotoAnalysis(Dir, actualHeight, actualSideLength, cubicThreshold):
    img = cv.imread(Dir)
    lp = len(img)
    Z = img.reshape((-1,3))
    # convert to np.float32
    Z = np.float32(Z)
    # define criteria, number of clusters(K) and apply kmeans()
    '''
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K = 10
    ret,label,center=cv.kmeans(Z,K,None,criteria,10,cv.KMEANS_RANDOM_CENTERS)
    # Now convert back into uint8, and make original image
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((img.shape))
    '''
    # 밑은 디버깅 상황 아니면 주석처리 바람
    '''
    cv.imshow('res2',img)
    cv.waitKey(0)
    cv.destroyAllWindows()
    '''
    avg = 0
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = gray.ravel() # 회색 이미지로 변경
    summation = 0 # 변수 선언
    #430, 582
    unique, counts = np.unique(np.array([gray[each*lp+960] for each in range(1080)]), return_counts=True)
    indi1 = dict(zip(unique, counts))# 특정 값의 픽셀의 갯수를 나타내는 딕셔너리
    unique, counts = np.unique(np.array([gray[each*lp+430] for each in range(1080)]), return_counts=True)
    indi2 = dict(zip(unique, counts))
    for key, value in indi1.items():
        avg += key*value
        summation += value
    avg /= summation
    std = ((sum([(key-avg)**2*value for key, value in indi1.items()]))/summation)**(1/2)
    for key, value in indi2.items():
        avg += key*value
        summation += value
    avg /= summation
    std2 = ((sum([(key-avg)**2*value for key, value in indi2.items()]))/summation)**(1/2)
    pixDevDisp = std**2+std2**2
    #return pixDevDisp
    if pixDevDisp < 5000:
        return 10
    elif pixDevDisp < 5600:
        return 25
    elif pixDevDisp < 6400:
        return 50
    elif pixDevDisp < 6900:
        return 75
    else:
        return 100
    '''
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
        yielded = (percentageCube+pyramidalVol)/totalVolume
    else:
        percentagePyramidal = pyramidalVol*(percentageWhite/cubicThreshold)**(3/2)
        # 2a^2+b^2 = c^2 --> k(2a^2+b^2)^(1/2)= k c #a^2*b
        yielded = percentagePyramidal/totalVolume
    print(yielded)
    if yielded >= 0.8:
        return 0.25
    elif 0.76 <= yielded < 0.8:
        return 0.5
    else:
        for key, value in alpha.items():
            if max(alpha.keys()) > key:
                pass
            else:
                indi1[key]
    '''


def PhotoAnalysisDark(Dir, actualHeight, actualSideLength, cubicThreshold):#만약 깔때기에 넣는 물체가 깔때기의 색보다 어두울 경우에 쓰는 함수입니다.
    return 1- PhotoAnalysis(Dir, actualHeight, actualSideLength, cubicThreshold)