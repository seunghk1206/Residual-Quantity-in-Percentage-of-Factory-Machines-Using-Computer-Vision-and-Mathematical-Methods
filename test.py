percentageWhite = 0.1
actualHeight = 20#cm
actualSideLength = 100#cm
cubicVol = actualHeight*actualSideLength**2
pyramidalVol = (cubicVol*1.5-10*10*10)*1/3
totalVolume = cubicVol+pyramidalVol
cubicThreshold = 0.6
if percentageWhite > cubicThreshold:
    #20cm height
    #rate of decrease
    percentageHeight = ((percentageWhite-cubicThreshold)/(1-cubicThreshold))**(1/2)
    print((percentageHeight*actualHeight*actualSideLength**2+pyramidalVol)/totalVolume)
else:
    percentagePyramidal = (percentageWhite/cubicThreshold)
    # 2a^2+b^2 = c^2 --> k(2a^2+b^2)^(1/2)= k c #a^2*b
    print(pyramidalVol*(percentagePyramidal)/totalVolume)
