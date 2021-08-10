import PhotoKMeanFunc as PKMF

Dir = 'comparisonPic.png' # 쓰고싶은 사진의 구체적 위치
actualHeight = 32 # 깔때기 직육면체 부분의 높이 센티미터로
actualSideLength = 68 # 깔때기 직육면체 가로 세로 길이. 정사각형이라고 들었기에 1개 뿐
cubicThreshold = 0.6 # 깔때기의 피라미드 부분만이 찼을때 찍힌 사진의 퍼센트. 예: 0.6이면 사진에서 60%가 깔때기의 물체로 차있게 보인다면, 그것은 깔때기의 피라미드 부분을 전부 채운 것이라는 가정을 한다.
print(PKMF.PhotoAnalysis(Dir, actualHeight, actualSideLength, cubicThreshold)) # 함수 불러오기. 구체적 정보는 PhotoKMeanFunc.py 참조바람
