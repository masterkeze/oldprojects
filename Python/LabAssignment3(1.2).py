import os
os.chdir('C:\\Python35')
def getVocabulary():
    vocabulary = list()
    word = list()
    file = open('TOEFL Vocabulary(updated).txt','r')
    lines = file.readlines()

    lines[len(lines)-1] = lines[len(lines)-1]+'\n'
    lines.append('')
    for line in lines:

        if not(line.startswith('Synonym')) and not(line.startswith('Antonym')):
            if len(word) == 3:
                word.append([])
                word.append([])
            if len(word) == 4:
                word.append([])
            if word != []:
                vocabulary.append(word)
                
            word = list()
            
            wordName = line[:line.find(':')]
            word.append(wordName.strip())
            
            wordMeaning = line[line.find(':')+1:line.find(' - ')]
            word.append(wordMeaning.strip())
            
            wordExample = line[line.find(' - ')+2:len(line)-2]
            word.append(wordExample.strip())
            
        elif line.startswith('Synonym'):
            synonym = line[line.find(':')+2:len(line)-1].split(',')
            for i in range(len(synonym)):
                synonym[i] = synonym[i].strip()
            word.append(synonym)
            
        elif line.startswith('Antonym'):
            if len(word) == 3:
                word.append([])
        
            antonym = line[line.find(':')+2:len(line)-1].split(',')
            for i in range(len(antonym)):
                antonym[i] = antonym[i].strip()
            word.append(antonym)

        
    file.close()
    return vocabulary

def generateFiles(vocabulary):
    
    file = open('TOFEL Vocabulary list No.1.doc','w')
    file.write('\t'*4+'TOFEL Vocabulary Generated by Python\n')
    file.write('\t'*4+'Name: Fei Yun Kai'+'\t'*2+'Student ID:115010139\n\n\n')
    count = 1
    for word in vocabulary:
        file.write('\n%s.%s\n\n'%(count,word[0].lower()))
        file.write('\t\t%s\n\n'%(word[1]))
        file.write('\t\tE.g.: %s\n\n'%(word[2]))
        if word[3] != []:
            
            if len(word[3]) == 1 :
                file.write('\t\tSynonym:\n')
            else:
                file.write('\t\tSynonyms:\n')
                
            for synonym in word[3]:
                file.write('\t\t\t'+synonym+'\n')
        if word[4] != []:
            
            if len(word[4]) == 1 :
                file.write('\t\tAntonym:\n')
            else:
                file.write('\t\tAntonyms:\n')
                
            for antonym in word[4]:
                file.write('\t\t\t'+antonym+'\n')
            
        count = count + 1
    file.close()
    #Create another file
    #Change the order
    reverseOrder = list()
    normalOrder = list()
    for word in vocabulary:
        normalOrder.append(word[0])
        
        temp = list(word[0])
        temp.reverse()
        newstring = ''.join(temp)
        reverseOrder.append(newstring)
        
    reverseOrder.sort()
    del reverseOrder[0]

    newOrder = list()
    for reverseWord in reverseOrder:
        temp = list(reverseWord)
        temp.reverse()
        newstring = ''.join(temp)
        newOrder.append(newstring)

    newVocabulary = list()
    for newWord in newOrder:
        newVocabulary.append(vocabulary[normalOrder.index(newWord)])

        




    rfile = open('TOFEL Vocabulary list No.2.doc','w')
    rfile.write('\t'*2+'TOFEL Vocabulary (Right-To-Left Alphabet Sequence) Generated by Python\n')
    rfile.write('\t'*4+'Name: Fei Yun Kai'+'\t'*2+'Student ID:115010139\n\n\n')
    count = 1
    for word in newVocabulary:
        rfile.write('\n%s.%s\n\n'%(count,word[0].lower()))
        rfile.write('\t\t%s\n\n'%(word[1]))
        rfile.write('\t\tE.g.: %s\n\n'%(word[2]))
        if word[3] != []:
            
            if len(word[3]) == 1 :
                rfile.write('\t\tSynonym:\n')
            else:
                rfile.write('\t\tSynonyms:\n')
                
            for synonym in word[3]:
                rfile.write('\t\t\t'+synonym+'\n')
        if word[4] != []:
            
            if len(word[4]) == 1 :
                rfile.write('\t\tAntonym:\n')
            else:
                rfile.write('\t\tAntonyms:\n')
                
            for antonym in word[4]:
                rfile.write('\t\t\t'+antonym+'\n')
            
        count = count + 1
    rfile.close()



    



generateFiles(getVocabulary())
print('Done.')

