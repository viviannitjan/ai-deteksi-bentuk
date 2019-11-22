import cv2
import numpy as np
import math


def countLengthVector(vec):
    length = math.hypot(vec[0], vec[1])
    return round(length)

def makeVector(point1, point2):
    x = point1[0] - point2[0]
    y = point1[1] - point2[1]
    return [x,y]

def countAngle(v1, v2):
    x1 = v1[0]
    x2 = v2[0]
    y1 = v1[1]
    y2 = v2[1]
    dotprod = x1*x2 + y1*y2 # x1*x2 + y1*y2
    vectormltp = math.sqrt((x1**2 + y1**2) * (x2**2 + y2**2))
    angle = math.acos(dotprod/vectormltp)
    angle = math.degrees(angle)
    if (x1*y2<x2*y1):
        angle = 180 - round(angle, 0)
    else:
        angle = round(angle,0)
    return angle

def counttitikTengah(corners):
    maxX=0
    maxY=0
    minX=1000000
    minY=1000000
    for corner in corners:
        x, y = corner.ravel()
        maxX = max(maxX,x)
        maxY = max(maxY,y)
        minX = min(minX,x)
        minY = min(minY,y)
    return [(maxX+minX)//2, (maxY-minY)//2]

def sortCorner(corner):
    refvec = [0, 1]
    v = makeVector(corner, titikTengah)
    lengthv = countLengthVector(v)
    if lengthv == 0:
        return -math.pi, 0
    normal = [v[0]/lengthv, v[1]/lengthv] #normalize v
    dotprod  = normal[0]*refvec[0] + normal[1]*refvec[1]     # x1*x2 + y1*y2
    diffprod = refvec[1]*normal[0] - refvec[0]*normal[1]     # x1*y2 - y1*x2
    angle = math.atan2(diffprod, dotprod)
    if angle < 0:
        return 2*math.pi+angle, lengthv
    return angle, lengthv

def processImage(fileName):
    img = cv2.imread(fileName, cv2.IMREAD_GRAYSCALE)
    t, tresh = cv2.threshold(img, 210, 250, cv2.THRESH_BINARY_INV)
    return tresh

def findTitikSudut(tresh):
    contours, hierarchy = cv2.findContours(tresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    corners = []
    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
        cv2.drawContours(tresh, [approx], 0, (255,255,255), 5)  
        corners = approx.reshape((len(approx),2))
    return corners

def findVectors(corners):
    vector = []
    for i in range (len(corners)):
        if (i==len(corners)-1):
            next = 0
        else:
            next = i+1
        vektor = makeVector(corners[i], corners[next])
        vector.append(vektor)
    return vector

def findPanjangSemuaSisi(vectors):
    panjang = []
    for v in vectors:
        length = countLengthVector(v)
        panjang.append(length)
    return panjang

def findAllAngles(vector):
    angle=[] #dapetin titik sudut
    for i in range (len(vector)):
        if (i==len(corners)-1):
            next = 0
        else:
            next = i+1
        sudut = countAngle(vector[i], vector[next])
        angle.append(sudut)
    return angle


titikTengah = [] #harus dijadikan variabel global
tresh = processImage('triangle.png')
corners = findTitikSudut(tresh)
titikTengah = counttitikTengah(corners)
# corners = sorted(corners, key=sortCorner)
vector = findVectors(corners)
angles = findAllAngles(vector)
panjangSisi = findPanjangSemuaSisi(vector)

print(corners)
print(panjangSisi)
print(vector)
print(angles)

cv2.imshow('ori', tresh)
cv2.waitKey(0) 
cv2.destroyAllWindows()
