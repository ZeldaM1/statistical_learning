
import numpy as np
import matplotlib.pyplot as plt
def plot_data(x_data, y_data):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_title('Linear training set')
    plt.xlabel('X')
    plt.ylabel('Y')
    x_data1 = x_data[:,0]
    x_data2 = x_data[:, 1]
    # plt.plot(x_data1, y_data)
    labels = np.array(y_data)
    idx_1 = np.where(y_data == 1)[0]
    ax.scatter(x_data1[idx_1], x_data2[idx_1], marker='o', color='g', label=1, s=20)
    idx_2 = np.where(y_data == -1)[0]
    ax.scatter(x_data1[idx_2], x_data2[idx_2],  marker='x', color='r', label=2, s=20)
    plt.legend(loc='upper right')
    plt.show()

def perceptron_fit(x_input, y_lable):
    global w, b
    best_fit = False  #the flag of find the best w and b
    numSamples = x_input.shape[0]
    w = np.zeros(x_input.shape[1])
    b = 0
    while(not best_fit):
        for i in range(numSamples):
            wx_b = np.sum(x_input[i] * w) #+ b
            wx_b *= y_lable[i]
            if wx_b <= 0:
                print(w,b)
                update(x_input[i],y_lable[i])
                break    #end for loop
            elif i == numSamples-1:
                print(w,b)
                best_fit = True   #end while loop
    print('---final results of w and b is:', w, b)
    return w, b

def update(row,trainLabel):
    global w, b
    for i in range(len(row)):
        w[i] += trainLabel * row[i]
    b += trainLabel


if __name__ == '__main__':
    # generating training set
    weights, numLines= [4, 2], 100
    w = np.array(weights)
    numFeatures = len(weights)
    x_train = np.zeros((numLines, numFeatures))
    y_train = np.zeros((numLines, 1))
    for i in range(numLines):
        x_train[i] = np.random.rand(1, numFeatures) * 20 - 10
        innerProduct = np.sum(w * x_train[i])
        y_train[i] = -1 if np.sum(w * x_train[i]) < 0 else 1
    plot_data(x_train, y_train)
    # start to fitting
    w_train, b_train = perceptron_fit(x_train, y_train)


    # test dataset from table 2
    x = np.array([[1, 2], [2, 3], [3, 3], [2, 1], [3, 2]])
    y = np.array([1, 1, 1, -1, -1])
    y_pre_all=[]

    for i in range(x.shape[0]):
        wx_b = np.sum(x[i] * w_train)  + b_train

        y_pre = -1 if np.sum(wx_b) < 0 else 1
        y_pre_all.append(y_pre)

    print('predict results is:', y_pre_all)
    print('error is :', y_pre_all==y)



