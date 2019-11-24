import cv2
import numpy as np
import math
import clips
import inflect

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
    vectormltp = math.sqrt(np.float64(x1**2 + y1**2) * np.float64(x2**2 + y2**2))
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

def add_fact(env, tipe, value):
    fact_string = "(" + tipe + " " + value + ")"
    fact = env.assert_string(fact_string)
    template = fact.template
    assert template.implied == True
    new_fact = template.new_fact()
    new_fact.assertit()
    return env

def get_vertices(corners):
    vertices = len(corners)
    # Ubah
    if vertices>=7 or vertices<=2:
        return 'other'
    return inf.number_to_words(vertices)

def get_same_edges(panjangSisi):
    if len(panjangSisi) >= 5:
        equal = True
        for i in range(len(panjangSisi)):
            if panjangSisi[0] != panjangSisi[i]:
                equal = False
                break
        
        if equal:
            return inf.number_to_words(len(panjangSisi))
        else:
            return 'other'
    else:
        if panjangSisi[0]==panjangSisi[1] and panjangSisi[0]==panjangSisi[2]:
            return 'three'
        elif panjangSisi[0]==panjangSisi[1] or panjangSisi[0]==panjangSisi[2] or panjangSisi[1]==panjangSisi[2]:
            return 'two'
        else:
            return 'none'

def get_angles_type(angles):
    if 90 in angles:
        return 'right'
    elif max(angles) > 90:
        return 'obtuse'
    else:
        return 'acute'

def get_acute_angles(angles):
    if max(angles) < 90:
        return 'three'
    else:
        return 'two'

def get_right_angles(angles):
    if 90 in angles:
        return 'one'
    else:
        return 'none'

# Perlu diubah
def get_parallel(vector):
    if cmp(vector[0],vector[2]) and cmp(vector[1],vector[3]):
        return 'two'
    elif cmp(vector[0],vector[2]) or cmp(vector[1],vector[3]):
        return 'one'
    else:
        return 'none'

def get_congrent():
    # Mohon bantuannya
    return 'two'

def get_congruent():
    # Mohon bantuannya
    return 'yes'

def get_right_angle_position():
    # Mohon bantuannya
    return 'right'


titikTengah = [] #harus dijadikan variabel global
tresh = processImage('square.png')
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

# Inisiasi awal clipspy
env = clips.Environment()
env.load("shape_rule.clp")

print("Agendas")
agendas = list(env.activations())
for agenda in agendas:
    print(agenda)

inf = inflect.engine()

number_of_vertices = get_vertices(corners)
env = add_fact(env,"number-of-vertices",number_of_vertices)

if number_of_vertices=='three' or number_of_vertices=='five' or number_of_vertices=='six':
    number_of_same_edges = get_same_edges(panjangSisi)
    env = add_fact(env,"number-of-same-edges",number_of_same_edges)

    if number_of_same_edges=='two':
        angles_type = get_angles_type(angles)
        env = add_fact(env,"angles-type",angles_type)

    if number_of_same_edges=='none':
        number_acute_angles = get_acute_angles(angles)
        env = add_fact(env,"number-acute-angles",number_acute_angles)

        if number_acute_angles=='two':
            number_right_angles = get_right_angles(angles)
            env = add_fact(env,"number-right-angles",number_right_angles)

if number_of_vertices=='four':
    number_of_parallel = get_parallel(vector)
    env = add_fact(env,"number-of-parallel",number_of_parallel)

    if number_of_parallel=='two':
        number_of_congrent_side = get_congrent()
        env = add_fact(env,"number-of-congrent-side",number_of_congrent_side)

    elif number_of_parallel=='one':
        is_congruent = get_congruent()
        env = add_fact(env,"is-the-legs-congruent",is_congruent)

        if is_congruent=='no':
            right_angle_position = get_right_angle_position()
            env = add_fact(env,"right-angle-position",right_angle_position)

agendas = list(env.activations())
agendas = reversed(agendas)
for agenda in agendas:
    print(agenda)

# Untuk menjalankan clips dan mendapatkan hasil
env.run()
# Untuk mendapatkan hasil shape
# print("Facts")
# facts = list(env.facts())
# for fact in facts:
#     if len(fact)!=0:
#         print(fact)
# shape = facts[-1]
# print(shape[0])
# print()

# print("Rules")
# rules = list(env.rules())
# for rule in rules:
#     print(rule)
# print()

print("Agendas")
agendas = list(env.activations())
for agenda in agendas:
    print(agenda)


# cv2.namedWindow('image',cv2.WINDOW_NORMAL)
# cv2.resizeWindow('image', 600,400)
# cv2.imshow('image', tresh)
# cv2.waitKey(0) 
# cv2.destroyAllWindows()
