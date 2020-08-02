# This file is going to implement gradient descend method with numpy
import numpy as np


def main():
    n = 2
    variable_list = []
    for i in range(n):
        variable_list.append(np.random.random())

    variables = np.array(variable_list).T

    data = np.vstack((np.ones(20,dtype=int),np.arange(1,21,dtype=int))).T
    target = np.array([np.arange(3,23,1,dtype=int)]).T
    linprog(data,target)

def linprog(data,target):
    learning_rate = 0.01
    n = data.shape[1]
    m = data.shape[0]
    variables = np.random.random((n,1))
    #variables = np.array([[2],[1]])
    print(variables)
    error = 1000
    last_error = 100
    run = 0
    while abs(last_error - error) > 0.001*last_error and error > 10**(-5):
        run = run + 1
        difference = data.dot(variables)-target
        last_error = error
        error = (difference**2).sum()/(2*m)
        
        #update variables
        temp = difference.dot(np.ones((1,n)))
        temp = temp*data
        temp = np.ones((1,m)).dot(temp)
        temp = temp.T * learning_rate/m
        variables = variables - temp
        print(error)
        
    print(variables)
    print("run = ",run)
    return variables
    
    
    
main()
