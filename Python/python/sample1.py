#coding=utf-8
# 本题为考试单行多行输入输出规范示例，无需提交，不计分。
##import sys 
##for line in sys.stdin:
##    a = line.split()
##    print(int(a[0]) + int(a[1]))

##import sys
##line = sys.stdin.readline().strip()
##output = eval(line)
##print(output)

import sys
inputString = sys.stdin.readline().strip()
#inputString = "SxxsrR^AaSs"
#First remove special characters
newString = ""
for s in inputString:
    if (s.isalpha()):
        newString += s
#print(newString)
searchRange = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Find pairs
pairs = []

def removeByIndex(string,index):

    string = string[:index] + string[index+1:]
    return string

def nextCharacter(char):
    searchRange = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if char == "Z":
        return "*"
    else:
        return searchRange[searchRange.find(char)+1]
for c in searchRange:
    temp = newString
    minCount = min(temp.count(c),temp.count(c.lower()))
    if minCount > 0:
        for i in range(minCount):
            pairs.append(c)

#print(pairs)
solutions = []

while len(pairs) > 0:
    pairs.sort()
    #Search through pairs, for each character in pairs find the longest snake string
    solutionSet = []
    solution = ""
    for i in range(len(pairs)):
        length = 1
        c = pairs[i]
        #print(c)
        while (True):
            if c == "Z" or pairs.count(nextCharacter(c)) == 0:
                break
            else:
                c = nextCharacter(c)
                length += 1
        solutionSet.append(length)
    #print(pairs)
    #print(solutionSet)
    #Merge pairs into strings
    largest = solutionSet.index(max(solutionSet))
    count = solutionSet[largest]
    char = pairs[largest]
    for i in range(count):
        solution += char
        solution += char.lower()
        #print("remove",char)
        pairs.remove(char)
        char = nextCharacter(char)
    if solution == "":
        
        break
    solutions.append((solution[0],-1*len(solution),solution))

if len(solutions) == 0:
    print("Not Found")
else:
    solutions.sort()
    for i in range(len(solutions)):
        print(solutions[i][2])

            









        
    
