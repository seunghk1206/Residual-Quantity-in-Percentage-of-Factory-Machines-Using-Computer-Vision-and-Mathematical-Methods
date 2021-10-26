import PhotoKMeanFunc as PKMF

Dir = '50-3.jpg' # 쓰고싶은 사진의 구체적 위치
print(PKMF.PhotoAnalysis(Dir)) # 함수 불러오기. 구체적 정보는 PhotoKMeanFunc.py 참조바람
DirL = ['10-1.jpg', '10-2.jpg', '10-4.jpg', '10-5.jpg', '10-6.jpg', '25-1.jpg', '25-2.jpg', '25-3.jpg', '25-4.jpg', '25-5.jpg', '50-1.jpg', '50-2.jpg', '50-3.jpg', '50-4.jpg', '50-5.jpg', '75-1.jpg', '75-2.jpg', '75-3.jpg', '75-4.jpg', '75-5.jpg', '100-1.jpg', '100-2.jpg', '100-3.jpg']
LP = []
for each in DirL:
    LP.append(PKMF.PhotoAnalysis(each))
print(LP)

#10: 46~47
#25: 51~52
#50: 53~60!
#75: 57~61!
#100: 60~63