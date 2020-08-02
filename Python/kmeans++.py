import random
testlist = []
anchor = [(10,10),(50,50),(90,90)]
k = 3
temp = (-1,-1)

def distance(p1,p2):
    distance = ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5
    return distance

def mindistance(p1,list1):
    minimun = -1
    for i in range(len(list1)):
        temp = distance(p1,list1[i])
        if temp == -1 or temp < minimun:
            minimun = temp
    return minimun

def kmeans(l,k):
    #print(l)
    center = []
    temp = []
    distance = []
    s = 0
    for i in l:
        temp.append(i)
    random.shuffle(temp)
    center.append(temp[0])
    temp.remove(center[len(center)-1])
    for i in range(1,k):
        for j in range(len(temp)):
            minvalue = mindistance(temp[i],center)
            distance.append(minvalue)
            s += minvalue
    
        s *= random.random()
        for j in range(len(temp)):
            s -= distance[j]
            if s > 0:
                continue
            center.append(temp[j])
            temp.remove(center[len(center)-1])
            break
    return center
    


for i in range(k):
    for r in range(0,100,2):
        for c in range(0,100,2):
            if distance((r,c),anchor[0]) <= 5:
                temp = (r,c)
            elif distance((r,c),anchor[1]) <= 5:
                temp = (r,c)
            elif distance((r,c),anchor[2]) <= 5:
                temp = (r,c)
            if random.random()< 0.3 and temp != (-1,-1) :
                testlist.append(temp)
            temp = (-1,-1)
            
center = kmeans(testlist,k)
print(center)
