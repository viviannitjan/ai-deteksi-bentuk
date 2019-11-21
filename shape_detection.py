import cv2
import numpy as np
import math


def countLineLength(point1, point2):
    length = math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)
    return length

# def gradient(point1, point2):
#     return (point2[1]-point1[1])/(point2[0]-point1[0])

# def countAngle(point1, point2, point3):
#     m1 = gradient(point1, point2)
#     m2 = gradient(point2, point3)
#     print(point1, point2, point3)
#     print(m1,m2)
#     angle = (m1-m2)/(1+(m1*m2))
#     angle = math.atan(angle)
#     return math.degrees(angle)

def makeVector(point1, point2):
    print(point1, point2)
    x = point1[0] - point2[0]
    y = point1[1] - point2[1]
    return [x,y]

def countAngle(v1, v2):
    # print(v1, v2)
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

img = cv2.imread('rectangle.png', cv2.IMREAD_GRAYSCALE)
t, tresh = cv2.threshold(img, 210, 250, cv2.THRESH_BINARY_INV)
# dst = cv2.Canny(tresh, 100, 200, None, 3)


# cdst = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)


# corners = cv2.goodFeaturesToTrack(img,25,0.01,10)
# corners = np.int0(corners)
# corners = corners.reshape((len(corners),2))
# print(corners)
'''
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
    cv2.circle(img, (x,y), 5, (255,255,255), -1)

origin = [(maxX+minX)//2, (maxY-minY)//2]
refvec = [0, 1]

def clockwiseangle_and_distance(point):
    # Vector between point and the origin: v = p - o
    vector = [point[0]-origin[0], point[1]-origin[1]]
    # Length of vector: ||v||
    lenvector = math.hypot(vector[0], vector[1])
    # If length is zero there is no angle
    if lenvector == 0:
        return -math.pi, 0
    # Normalize vector: v/||v||
    normalized = [vector[0]/lenvector, vector[1]/lenvector]
    dotprod  = normalized[0]*refvec[0] + normalized[1]*refvec[1]     # x1*x2 + y1*y2
    diffprod = refvec[1]*normalized[0] - refvec[0]*normalized[1]     # x1*y2 - y1*x2
    angle = math.atan2(diffprod, dotprod)
    # Negative angles represent counter-clockwise angles so we need to subtract them 
    # from 2*pi (360 degrees)
    if angle < 0:
        return 2*math.pi+angle, lenvector
    # I return first the angle because that's the primary sorting criterium
    # but if two vectors have the same angle then the shorter distance should come first.
    return angle, lenvector

print(sorted(corners, key=clockwiseangle_and_distance))
'''
# print(maxX,maxY)
# print(minX,minY)
# print((maxX+minX)//2,(maxY-minY)//2)
# cv2.circle(img, ((maxX+minX)//2,(maxY+minY)//2), 5, (255,255,255), -1)
# tresh = np.float32(tresh)
# dst = cv2.cornerHarris(tresh,2,3,0.04)
# dst_norm = np.empty(dst.shape, dtype=np.float32)
# cv2.normalize(dst, dst_norm, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
# dst_norm_scaled = cv2.convertScaleAbs(dst_norm)

# points=np.unravel_index(dst.argmax(),dst.shape)

# print (list(points))

# for i in range(dst_norm.shape[0]):
#     for j in range(dst_norm.shape[1]):
#         if int(dst_norm[i,j]) > 200:
#             cv2.circle(dst_norm_scaled, (j,i), 5, (0), 2)
#             print(j,i)


# img[dst>0.01*dst.max()]=[0,0,255]
# linesP = cv2.HoughLinesP(dst, 1, np.pi / 180, 50, None, 50, 10)
# print(len(linesP))
    
# if linesP is not None:
#     for i in range(0, len(linesP)):
#         l = linesP[i][0]
#         print(l)
#         cv2.line(cdst, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv2.LINE_AA)

contours, hierarchy = cv2.findContours(tresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
corners = []

for cnt in contours:
    print(len(cnt))
    approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
    print(cv2.arcLength(cnt, True))
    cv2.drawContours(tresh, [approx], 0, (255,255,255), 5)  
    corners = approx.reshape((len(approx),2))
    print(approx)
print(corners)

panjang = []
vector = []
for i in range (len(corners)):
    print(i)
    if (i==len(corners)-1):
        next = 0
    else:
        next = i+1
    length = countLineLength(corners[i], corners[next])
    vektor = makeVector(corners[i], corners[next])
    panjang.append(length)
    vector.append(vektor)
print(panjang)
print(vector)

angle=[]
for i in range (len(vector)):
    if (i==len(corners)-1):
        next = 0
    else:
        next = i+1
    sudut = countAngle(vector[i], vector[next])
    angle.append(sudut)
    # if (i==len(corners)-2):
    #     print("masuk sini1 ")
    #     next1 = i+1
    #     next2 = 0
    # elif (i==len(corners)-1):
    #     print("masuk sini2 ")
    #     next1 = 0
    #     next2 = 1
    # else:
    #     next1 = i+1
    #     next2 = i+2
    # hasil_sudut = countAngle(corners[i], corners[next1], corners[next2])
    # angle.append(hasil_sudut)

print(angle)

# cv2.imshow('triangle', dst)
cv2.imshow('ori', tresh)
cv2.waitKey(0) 
cv2.destroyAllWindows()
