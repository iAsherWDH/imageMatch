# _*_ coding=utf-8 _*_
from math import sqrt

__date__ = '9/24/2018 13:28 '

import cv2
import time
import os
import numpy as np
from  config import COLOR_DEGREE

def getColorVec(img):
    hei, width, channel=img.shape
    colorVec=[0 for e in range(0, int(pow(COLOR_DEGREE, 3)))]
    i=0
    while(i<hei):
        j=0
        while(j<width):
            pixel=img[i][j]
            grade=getPixelGrade(pixel)
            index=grade[0]*COLOR_DEGREE*COLOR_DEGREE+grade[1]*COLOR_DEGREE+grade[2]
            colorVec[index]+=1
            j+=1
        i+=1
    return colorVec


def getPixelGrade(pixel):
    grade=[]
    base=int(256/COLOR_DEGREE)+1
    for one in np.array(pixel):
        grade.append(int(one/base))
    return grade

def Bdistance(l1, l2):
    if(len(l1)!=len(l2)):
        raise RuntimeError("计算巴氏距离时，引入长度不相等的向量")
    s1=sum(l1)
    s2=sum(l2)
    BD=0
    for ind in range(0, len(l1)):
        BD+=sqrt((l1[ind]/s1)*(l2[ind]/s2))
    return BD



#logger = logging.getLogger(__name__)
#logger.setLevel(level=logging.INFO)
#handler = logging.FileHandler('output.log')
#formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#handler.setFormatter(formatter)
#logger.addHandler(handler)


def getFileSuffix(filename):
    return os.path.splitext(filename)[-1][1:]
