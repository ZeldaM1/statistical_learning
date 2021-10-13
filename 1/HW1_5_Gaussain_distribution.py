import numpy as np
import math
import matplotlib.pyplot as plt
if __name__ == '__main__':
    mu = 10
    sigmoid = 5
    N = 1
    distribution_set=[]
    mean_set=[]
    var_set=[]

    for indx in range(8):
        N = N * 10
        distribution_set=np.random.normal(loc=mu, scale=sigmoid, size=N)
        print('N: {}, mu: {}/{}, sigmoid: {}/{}'.format(N, mu, distribution_set.mean(),sigmoid, math.sqrt(distribution_set.var())))
        mean_set.append( distribution_set.mean())
        var_set.append(math.sqrt(distribution_set.var()))


    plt.hlines(mu, 10, N, 'red', '-', label='mu')
    plt.hlines(sigmoid, 10, N, 'green', '-', label='sigmoid')

    N_var = np.linspace(10, N, len(mean_set))
    plt.plot(N_var, mean_set, linestyle='--', color='red', label='dis mean')
    plt.plot(N_var, var_set, linestyle='--', color='green', label='dis std')

    plt.legend()
    plt.savefig('./N_{}.png'.format(N))


