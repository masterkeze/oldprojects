# This file is to do linear regression
# on the data set [(x1,y1),(x2,y2),(x3,y3)]
import random

def linear_regression(points):
    'output: theta0, theta1; h(x) = theta0 + theta1 * x'
    learning_rate = 0.01
    num = len(points)
    theta0 = 0
    theta1 = 1
    error = 100
    last_error = 1000
    while abs(last_error-error)>0.0001*last_error:
        last_error = error
        temp = 0
        error = 0
        sum_0 = 0
        sum_1 = 0
        for point in points:
            temp = (theta0+theta1*point[0]-point[1])
            sum_0 = sum_0 + temp
            sum_1 = sum_1 + temp*point[0]
            error = error + temp**2
        theta0 = theta0 - learning_rate/num*sum_0
        theta1 = theta1 - learning_rate/num*sum_1
        error = error/(2*num)

        #print(theta0,theta1)
    return (theta0,theta1)

def get_random(theta0,theta1,num):
    points = []
    for i in range(num):
        temp = theta0+theta1*i
        x_temp = 0.9*i+round(0.2*random.random()*i,2)
        y_temp = 0.9*temp+round(0.2*random.random()*temp,2)
        points.append((x_temp,y_temp))
    return points
    
def main():
    print(linear_regression(get_random(7,4,10)))
        

