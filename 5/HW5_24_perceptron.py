
import numpy as np


def perceptronClassify(x_input, y_lable):
    global w, b
    best_fit = False  #the flag of find the best w and b
    numSamples = x_input.shape[0]
    w = np.zeros(x_input.shape[1])
    b = 0
    while(not best_fit):
        for i in range(numSamples):
            wx_b = np.sum(x_input[i] * w) + b
            wx_b *= y_lable[i]
            if wx_b <= 0:
                print(w,b)
                update(x_input[i],y_lable[i])
                break    #end for loop
            elif i == numSamples-1:
                print(w,b)
                best_fit = True   #end while loop
    print('---final results', w, b)



def update(row,trainLabel):
    global w, b
    for i in range(len(row)):
        w[i] += trainLabel * row[i]
    b += trainLabel

if __name__ == '__main__':
    # data from table 2
    x = np.array([[1, 2], [2, 3], [3, 3], [2, 1], [3, 2]])
    y = [1, 1, 1, -1, -1]
    perceptronClassify(x, y)

