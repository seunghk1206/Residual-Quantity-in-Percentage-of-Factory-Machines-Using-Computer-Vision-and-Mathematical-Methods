import numpy as np
import cv2 as cv

def PhotoAnalysis(Dir):
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
    #여기까지
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
    pixDevDisp = ((std+std2)/2)**2
    #return pixDevDisp
    
    if pixDevDisp <= 2500:
        return 10
    elif pixDevDisp <= 2757:
        return 25
    elif pixDevDisp <= 3037:
        return 50
    elif pixDevDisp <= 3423:
        return 75
    else:
        return 100

def PhotoAnalysis2(Dir):
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
    #여기까지
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
    pixDevDisp = (std**2+std2**2)/2
    if pixDevDisp < 2500:
        return 10
    elif pixDevDisp < 2800:
        return 25
    elif pixDevDisp < 3200:
        return 50
    elif pixDevDisp < 3450:
        return 75
    else:
        return 100