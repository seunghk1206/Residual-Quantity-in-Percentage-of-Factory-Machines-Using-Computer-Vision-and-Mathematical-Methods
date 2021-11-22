import PhotoKMeanFunc as PKMF
import time
#Dir = '50-3.jpg' # 쓰고싶은 사진의 구체적 위치
#print(PKMF.PhotoAnalysis(Dir)) # 함수 불러오기. 구체적 정보는 PhotoKMeanFunc.py 참조바람
FoldL = 'FronTechData/'
DirL = ['10-1.jpg', '10-2.jpg', '10-4.jpg', '10-5.jpg', '10-6.jpg', '25-1.jpg', '25-2.jpg', '25-3.jpg', '25-4.jpg', '25-5.jpg', '50-1.jpg', '50-2.jpg', '50-3.jpg', '50-4.jpg', '50-5.jpg', '75-1.jpg', '75-2.jpg', '75-3.jpg', '75-4.jpg', '75-5.jpg', '100-1.jpg', '100-2.jpg', '100-3.jpg']
LP = []
avgT = 0
print(PKMF.PhotoAnalysis(FoldL+'50-2.jpg'))
'''
for each in DirL:
    init = time.time()
    LP.append(PKMF.PhotoAnalysis(FoldL+each))
    lin = time.time() - init
    avgT += lin
avgT /= len(LP)
#print(avgT)
ansL = [10, 10, 10, 10, 10, 25, 25, 25, 25, 25, 50, 50, 50, 50, 50, 75, 75, 75, 75, 75, 100, 100, 100]
correct = len(ansL)
for i in range(len(ansL)):
    if LP[i] != ansL[i]:
        correct -= 1
print(LP)
'''
#10: 46~47
#25: 51~52
#50: 53~60!
#75: 57~61!
#100: 60~63