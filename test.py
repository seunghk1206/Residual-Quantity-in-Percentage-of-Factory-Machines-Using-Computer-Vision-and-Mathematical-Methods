def PhotoAnalysis(actualHeight, actualSideLength, cubicThreshold):
    percentageWhite = 0.8 # 사진에서의 하얀/회색 부분의 퍼센트.
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

actualHeight = 24 # 깔때기 직육면체 부분의 높이 센티미터로
actualSideLength = 68 # 깔때기 직육면체 가로 세로 길이. 정사각형이라고 들었기에 1개 뿐
cubicThreshold = 0.8 # 깔때기의 피라미드 부분만이 찼을때 찍힌 사진의 퍼센트. 예: 0.6이면 사진에서 60%가 깔때기의 물체로 차있게 보인다면, 그것은 깔때기의 피라미드 부분을 전부 채운 것이라는 가정을 한다.
print(PhotoAnalysis(actualHeight, actualSideLength, cubicThreshold)) # 함수 불러오기. 구체적 정보는 PhotoKMeanFunc.py 참조바람
