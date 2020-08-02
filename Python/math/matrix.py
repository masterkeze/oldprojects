class matrix():
    def __init__(self,content = [[0]]):
        if not(type(content) == list):
            print('Invalid Input.')
            content = [[0]]
        self.content = content
        self.rows = len(self.content)
        self.columns = len(self.content[0])
        print(self.rows,'X',self.columns,'matrix is created.')
        
    def add(self,B):
        s = list()
        if self.rows == B.rows and self.columns == B.columns:
            for r in range(self.rows):
                s.append([])
                for c in range(self.columns):
                    s[r].append(self.content[r][c]+B.content[r][c])
            S = matrix(s)
            #S.show()
            return S
        else:
            print('Unmatched format.')
            return []
        
    def multiply_num(self,n):
        S = matrix(self.content)
        for r in range(self.rows):
            S.multiply_rows(n,r)
        return S

    def multiply_matrix(self,A):
        if self.columns == A.rows:
            n = self.columns
            s = list()
            for r in range(self.rows):
                s.append([])
                for c in range(A.columns):
                    temp = 0
                    for i in range(n):
                        temp = temp + self.content[r][i] * A.content[i][c]
                    s[r].append(temp)
            S = matrix(s)
            return S
        else:
            print('Unmatched format.')
            return []
    
    def show(self):
        output = list()
        for r in range(self.rows):
            output.append([])
            for c in range(self.columns):
                output[r].append(round(self.content[r][c],2))
        print(output)
        
    def swap_rows(self,a,b):
        if a < self.rows and b < self.rows:
            temp = list()
            for item in self.content[a]:
                temp.append(item)
            self.content[a] = self.content[b]
            self.content[b] = temp
            return self.content
        else:
            print('Invalid input.')

    def multiply_rows(self,n,r):
        for i in range(self.columns):
            self.content[r][i] = self.content[r][i] * n
        return self.content

    def add_rows(self,r,multiplier1,r1,multiplier2,r2):
        for i in range(self.columns):
            self.content[r][i] = multiplier1*self.content[r1][i] + multiplier2*self.content[r2][i]
        return self.content
            
    def reduce(self):
        'Reduce the original matrix to its reduced row echelon form.'
        #self.multiply_rows(5,1)
        r = 0
        c = 0
        p = 0#The column that is under formatting.
        leading_ones = list()
        while c < self.columns:
            zeros = list()
            nonzeros = list()
            for r in range(len(leading_ones),self.rows):
                if self.content[r][c] == 0:
                    zeros.append(r)
                else:
                    nonzeros.append(r)
            #print(zeros,nonzeros)
            if len(zeros)>0 and len(nonzeros)>0:
                for i in range(len(nonzeros)):
                    if len(zeros)>0  and zeros[0]<nonzeros[i]:
                        self.swap_rows(zeros[0],nonzeros[i])
                        nonzeros[i] = zeros[0]
                        zeros.pop(0)

            if len(nonzeros)>0:
                n = self.content[nonzeros[0]][c]
                self.multiply_rows(1/n,nonzeros[0])
                if len(nonzeros)>1:
                    for rest in nonzeros[1:]:
                        n1 = -1*self.content[rest][c]
                        n2 = 1
                        self.add_rows(rest,n1,nonzeros[0],n2,rest)
                if len(leading_ones) > 0:
                    for first_rows in leading_ones:
                        n1 = -1*self.content[first_rows][c]
                        n2 = 1
                        self.add_rows(first_rows,n1,nonzeros[0],n2,first_rows)
                leading_ones.append(nonzeros[0]) 

                self.show()
            c = c + 1
        return self.content
    
    def isreduced(self):
        #zero rows below all nonzero rows.
        zero_rows = list()
        nonzero_rows = list()
        leading_ones = list()
        for r in range(self.rows):
            leading_ones.append(-1)
            zeros = 0
            for c in range(self.columns):
                if self.content[r][c] == 0:
                    zeros += 1
                if self.content[r][c] == 1 and leading_ones[r] == -1:
                    leading_ones[r] = c
                if self.content[r][c] != 0 and self.content[r][c] !=1 and leading_ones[r] == -1:
                    print(r+1,'th row is not led by one.')
                    return False
            if zeros == self.columns :
                zero_rows.append(r)
            else:
                nonzero_rows.append(r)

        if zero_rows != [] and nonzero_rows != []:
            if zero_rows[0] < nonzero_rows[len(nonzero_rows)-1]:
                print('This matrix has some zero rows above nonzero rows.')
                return False

        for i in range(len(leading_ones)):
            one = leading_ones[i]
            if one == -1:
                continue
            else:
                index = one
            for r in range(self.rows):
                #print('r=',r,'index=',index)
                if self.content[r][index] != 0 and r != i:
                    print('Column '+str(index+1)+' is not pivot.')
                    return False
                
        #check the sequence
        for i in range(len(leading_ones)):
            try:
                if leading_ones[i] > leading_ones[i+1] and leading_ones[i+1] != -1:
                    print('The order of leading ones is not right.')
                    return False
            except:
                break
        return True


def main():
    a = [[1,2,3],[4,5,6]]
    b = [[7,8,9],[10,11,12],[13,14,15]]
    A = matrix(a)
    B = matrix(b)
    C = A.multiply_matrix(B)
    C.show()


