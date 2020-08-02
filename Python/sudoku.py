import copy
##
##puzzle =[[9,1,0,7,0,0,0,0,0],
##         [0,3,2,6,0,9,0,8,0],
##         [0,0,7,0,8,0,9,0,0],
##         [0,8,6,0,3,0,1,7,0],
##         [3,0,0,0,0,0,0,0,6],
##         [0,5,1,0,2,0,8,4,0],
##         [0,0,9,0,5,0,3,0,0],
##         [0,2,0,3,0,1,4,9,0],
##         [0,0,0,0,0,2,0,6,1]]
##puzzle = [[0,0,0,0,6,1,0,0,5],
##          [8,0,0,0,5,0,0,0,0],
##          [0,0,0,0,0,0,8,4,7],
##          [0,5,0,0,0,0,9,0,0],
##          [6,0,0,9,0,4,0,0,8],
##          [0,0,3,0,0,0,0,1,0],
##          [7,9,1,0,0,0,0,0,0],
##          [0,0,0,0,8,0,0,0,2],
##          [5,0,0,7,3,0,0,0,0]]
##puzzle = [[0,0,1,8,3,0,0,0,0],
##          [9,6,5,0,0,0,0,0,0],
##          [0,0,0,0,1,0,9,0,0],
##          [4,0,0,0,0,0,0,1,0],
##          [0,0,9,6,0,4,3,0,0],
##          [0,8,0,0,0,0,0,0,2],
##          [0,0,7,0,9,0,0,0,0],
##          [0,0,0,0,0,0,5,4,8],
##          [0,0,0,0,2,5,1,0,0]]
##puzzle = [[0,4,0,0,6,8,0,0,0],
##          [7,0,0,0,0,9,0,0,8],
##          [0,6,2,0,0,0,0,4,0],
##          [0,0,0,5,0,6,0,0,4],
##          [0,7,0,0,0,0,0,8,0],
##          [9,0,0,1,0,7,0,0,0],
##          [0,5,0,0,0,0,3,9,0],
##          [3,0,0,9,0,0,0,0,1],
##          [0,0,0,6,5,0,0,2,0]]
puzzle = [[0,5,0,0,0,2,0,4,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,5,8,0,0,0],
          [0,0,6,0,0,4,7,8,0],
          [0,1,9,0,0,0,0,0,6],
          [8,0,5,0,0,0,0,3,0],
          [0,2,0,9,0,0,0,0,0],
          [3,6,0,1,0,0,5,0,9],
          [0,0,0,0,8,0,6,0,0]]

global t
t = 0

temp = copy.deepcopy(puzzle)


def row(temp,x,y,n):
    for i in range(9):
        #print("scan",temp[x][i])
        if temp[x][i] == n and y != i:
            return False
    return True

def column(temp,x,y,n):
    for i in range(9):
        #print("scan",temp[i][y])
        if temp[i][y] == n and x != i:
            return False
    return True

def square(temp,x,y,l):
    j = (x//3)*3
    i = (y//3)*3

    for m in range(j,j+3):
        for n in range(i,i+3):
##            print("scan",temp[m][n])
##            print('x = ',x,'y = ',y)
##            print('temp[m][n] = ',temp[m][n],'m = ',m,'n = ',n)
            if m == x and n == y:
                continue
            if temp[m][n] == l:
                return False
    return True

def place(temp,x,y,n):
    if row(temp,x,y,n) and column(temp,x,y,n) and square(temp,x,y,n):
        return True
    else:
        return False
    
def getchoice():
    choice = list()
    for i in range(9):
        for j in range(9):
            if temp[i][j] == 0:
                exec("choice%s%s = list()"%(i,j))
                for k in range(1,10):
                    if place(temp,i,j,k):
                        exec("choice%s%s.append(%s)"%(i,j,k))
                exec("choice.append([len(choice%s%s),%s,%s,choice%s%s])"%(i,j,i,j,i,j))
    return choice

##choice = getchoice()
##choice.sort()
#print(choice)
def leftzero(temp):
    for i in range(9):
        for j in range(9):
            if temp[i][j] == 0:
                return True
    return False

def iscorrect(a):
    for i in range(9):
        for j in range(9):
            if not(place(a,i,j,a[i][j])):
                print('False at ('+str(i)+','+str(j)+')')
                return False
            if leftzero(a):
                print('Left zero')
                return False
    return True

def solve():
    global temp
    global t
    choice = getchoice()
    choice.sort()
    print('called')
    while not(iscorrect(temp)):
        t = t + 1
        #print(choice)
        for item in choice:
            if item[0] == 1:
                i = item[1]
                j = item[2]
                n = item[3][0]
                if place(temp,i,j,n):
                    temp[i][j] = n
                    print("change ("+str(i+1)+','+str(j+1)+') to '+str(n))
                else:
                    print("seem to be wrong")
                    return False
            else:
                break
        newchoice = getchoice()
        newchoice.sort()
        if newchoice==choice and choice != []:
            if choice[0][0] == 0:
                print("can't continue")
                return False
            if choice[0][0] >= 2:
                for l in choice[0][3]:
                    i = choice[0][1]
                    j = choice[0][2]
                    temp1 = copy.deepcopy(temp)
                    temp[i][j] = l
                    print("try: ("+str(i+1)+','+str(j+1)+') to '+str(l))
                    if not(solve()):
                        temp =copy.deepcopy(temp1)
                    else:
                        return True
                    
                print("can't solve")
                return False
        if iscorrect(temp):
            print(temp)
            print('Solved')
            return True
        choice = newchoice

solve()
print("step = ",t)



    
