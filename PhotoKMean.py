import PhotoKMeanFunc as PKMF

Dir = 'expectedResult.png' # 쓰고싶은 사진의 구체적 위치
actualHeight = 20 # 깔때기 직육면체 부분의 높이 센티미터로
actualSideLength = 100 # 깔때기 직육면체 가로 세로 길이. 정사각형이라고 들었기에 1개 뿐
cubicThreshold = 0.6 # 깔때기의 피라미드 부분만이 찼을때 찍힌 사진의 퍼센트
PKMF.PhotoAnalysis(Dir, actualHeight, actualSideLength, cubicThreshold) # 함수 불러오기 구체적 정보는 PhotoKMeanFunc.py 참조바람