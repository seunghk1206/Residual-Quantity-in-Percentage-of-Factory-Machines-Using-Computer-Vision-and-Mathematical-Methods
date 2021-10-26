import PhotoKMeanFunc as PKMF

Dir = '50-3.jpg' # 쓰고싶은 사진의 구체적 위치
actualHeight = 24 # 깔때기 직육면체 부분의 높이 센티미터로
actualSideLength = 68 # 깔때기 직육면체 가로 세로 길이. 정사각형이라고 들었기에 1개 뿐
cubicThreshold = 0.71 # 깔때기의 피라미드 부분만이 찼을때 찍힌 사진의 퍼센트. 예: 0.6이면 사진에서 60%가 깔때기의 물체로 차있게 보인다면, 그것은 깔때기의 피라미드 부분을 전부 채운 것이라는 가정을 한다.
print(PKMF.PhotoAnalysis(Dir, actualHeight, actualSideLength, cubicThreshold)) # 함수 불러오기. 구체적 정보는 PhotoKMeanFunc.py 참조바람
DirL = ['10-1.jpg', '10-2.jpg', '10-4.jpg', '10-5.jpg', '10-6.jpg', '25-1.jpg', '25-2.jpg', '25-3.jpg', '25-4.jpg', '25-5.jpg', '50-1.jpg', '50-2.jpg', '50-3.jpg', '50-4.jpg', '50-5.jpg', '75-1.jpg', '75-2.jpg', '75-3.jpg', '75-4.jpg', '75-5.jpg', '100-1.jpg', '100-2.jpg', '100-3.jpg']
LP = []
for each in DirL:
    LP.append(PKMF.PhotoAnalysis(each, actualHeight, actualSideLength, cubicThreshold))
print(LP)

#10: 46~47
#25: 51~52
#50: 53~60!
#75: 57~61!
#100: 60~63