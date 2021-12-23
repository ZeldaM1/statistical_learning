import numpy as np
import pandas as pd


# 带有拉普拉斯平滑的朴素贝叶斯计算过程
def train(test, Alpha):
    if test['X2'] == 'S':
        i = 0
    elif test['X2'] == 'M':
        i = 1
    elif test['X2'] == 'L':
        i = 2

    j = test['X1'] -1


    p_y11 = ((count_x1[j][0] + Alpha) / (count_x1.sum(axis=0)[0] + 3 * Alpha)) * (
            (count_x2[i][0] + Alpha) / (count_x1.sum(axis=0)[0] + 3 * Alpha)) * (
                        (count_x1.sum(axis=0)[0] + Alpha) / (11 + 2 * Alpha))
    p_y12 = ((count_x1[j][1] + Alpha) / (count_x2.sum(axis=0)[1] + 3 * Alpha)) * (
            (count_x2[i][1] + Alpha) / (count_x2.sum(axis=0)[1] + 3 * Alpha)) * (
                        (count_x1.sum(axis=0)[1] + Alpha) / (11 + 2 * Alpha))

    p_y1 = p_y11 / (p_y11 + p_y12)
    p_y2 = p_y12 / (p_y11 + p_y12)
    print("Y=1：", p_y1)
    print("Y=-1：", p_y2)
    if p_y1 > p_y2:
        print("test dataset is categorized into 1 class")
    else:
        print("test dataset is categorized into -1 class")

if __name__ == '__main__':
    #  训练集11组（X1,X2,Y）
    a = np.array([[1, "S", -1], [1, "M", -1], [1, "M", 1],
                  [1, "S", 1], [1, "S", -1], [2, "S", -1],
                  [2, "M", -1], [2, "M", 1], [2, "L", 1],
                  [2, "L", 1], [3, "L", 1]])
    b = pd.DataFrame(a, columns=['X1', 'X2', 'Y'])

    # 多计数器
    count_x1 = np.zeros((3, 2))
    count_x2 = np.zeros((3, 2))
    # 概率值(1,-1)
    p_y1 = 0
    p_y2 = 0
    # 测试集
    test = pd.Series({'X1': 1, 'X2': 'M'})

    # P(YK|X1,X2)=P(X1|YK)*P(X2|YK)*P(YK)/P(X)
    # 计数器统计训练集相应数据
    for index, row in b.iterrows():
        if row['Y'] == "1":
            if row['X1'] == "1":
                count_x1[0][0] += 1
            elif row['X1'] == "2":
                count_x1[1][0] += 1
            else:
                count_x1[2][0] += 1

            if row['X2'] == "S":
                count_x2[0][0] += 1
            elif row['X2'] == "M":
                count_x2[1][0] += 1
            else:
                count_x2[2][0] += 1
        else:
            if row['X1'] == "1":
                count_x1[0][1] += 1
            elif row['X1'] == "2":
                count_x1[1][1] += 1
            else:
                count_x1[2][1] += 1

            if row['X2'] == "S":
                count_x2[0][1] += 1
            elif row['X2'] == "M":
                count_x2[1][1] += 1
            else:
                count_x2[2][1] += 1


    print('alpha = 0:')
    train(test, 0)
    print('\n')
    print('alpha = 1:')
    train(test, 1)
