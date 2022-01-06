import PhotoKMeanFunc as PKMF
from datetime import datetime
import time
import os
import csv

#Dir = '50-3.jpg' # 쓰고싶은 사진의 구체적 위치
#print(PKMF.PhotoAnalysis(Dir)) # 함수 불러오기. 구체적 정보는 PhotoKMeanFunc.py 참조바람
run = True
while run:
    initFoldL = 'FronTechTest/'
    initDirL = os.listdir(initFoldL)#['10-1.jpg', '10-2.jpg', '10-4.jpg', '10-5.jpg', '10-6.jpg', '25-1.jpg', '25-2.jpg', '25-3.jpg', '25-4.jpg', '25-5.jpg', '50-1.jpg', '50-2.jpg', '50-3.jpg', '50-4.jpg', '50-5.jpg', '75-1.jpg', '75-2.jpg', '75-3.jpg', '75-4.jpg', '75-5.jpg', '100-1.jpg', '100-2.jpg', '100-3.jpg']
    for Directory in initDirL:
        init = time.time()
        FoldL = initFoldL+Directory+'/'
        DirL = list(os.listdir(FoldL))
        OTF = 'img'+str(len(DirL)-1)+'.jpg'
        LP = []
        avgT = 0
        output = PKMF.PhotoAnalysis('./'+FoldL + OTF, './'+FoldL+'img0.jpg')
        if len(os.listdir('./csv/'))==0:
            csvFile = open('./csv/FronTechResidualLog.csv', 'w', newline='', encoding='utf-8-sig')
            wr = csv.writer(csvFile)
            wr.writerow([Directory, str(output)+'%', datetime.today()])
        else:
            csvFile = open('./csv/FronTechResidualLog.csv', 'a', newline='')
            wr = csv.writer(csvFile)
            wr.writerow([Directory, str(output)+'%', datetime.today()])
    codeRunTime = time.time()-init
    print('done')
    time.sleep(300-codeRunTime-0.01)
    csvFile.close()
'''
    for each in DirL:
        init = time.time()
        LP.append(PKMF.PhotoAnalysis(FoldL+each, FoldL+'img0'))
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
    print(correct/len(ansL))
    #10: 46~47
    #25: 51~52
    #50: 53~60!
    #75: 57~61!
    #100: 60~63
    '''