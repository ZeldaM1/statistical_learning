import numpy as np
import matplotlib.pyplot as plt
from tkinter import _flatten


if __name__ == '__main__':


    x_all = np.arange(0, 25, 1) * 0.041
    y_all = np.sin(2 * np.pi * x_all)
    x_Prec = np.linspace(0, 24 * 0.041, 100)


    order = 8  # set order as 7
    lamda = [np.exp(1.6), np.exp(-1.3), np.exp(-2.4), np.exp(-10)] #lambda

    phi = np.mat(np.zeros((x_all.size, order)))  # phi
    x = np.mat(x_all).T


    for i_n in range(order):
        for y_n in range(x_all.size):
            phi[y_n, i_n] = x[y_n, 0] ** i_n


    color = ['red','green','blue','purple']
    y_all_noise = np.zeros(y_all.shape)
    sub_fig=221
    for lamda_indx in range(len(lamda)):
        plt.subplot(sub_fig)
        sub_fig+=1
        plt.title("lambda = %f" % lamda[lamda_indx])
        plt.plot(x_Prec, np.sin(2 * np.pi * x_Prec), color='black')
        for k in range(100):
            for i in range(x_all.size):
                y_all_noise[i] = y_all[i] + np.random.normal(0, 0.3)
            y = np.mat(y_all_noise).T

            W = (phi.T * phi + lamda[lamda_indx] * np.eye(order)).I * phi.T * y

            ploy = list(_flatten(W.T.tolist()))
            ploy.reverse()
            p = np.poly1d(ploy)
            if k % 10 == 0:
                plt.plot(x_Prec, p(x_Prec), color=color[lamda_indx])

    plt.subplots_adjust(hspace=0.6)
    plt.savefig('./lambda.png')



