from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier,export_graphviz, export_text
from sklearn.model_selection import train_test_split
import graphviz
import numpy as np
# from IPython.display import Image
from PIL import Image
import pydotplus


def createDataSet():
    x_arange1 = 0.041 * np.arange(0, 25, 1)
    y_True1 = np.sin(2 * np.pi * x_arange1)

    x_arange1 = np.arange(0, 25, 1)
    y_True2 = np.sin(2 * np.pi * x_arange1) + 0.1

    x_s = np.concatenate((x_arange1, x_arange1), axis=0).reshape(50, 1)
    y_s = np.concatenate((y_True1, y_True2), axis=0).reshape(50, 1)
    x = np.concatenate((x_s, y_s), axis=1).reshape(50, 2)

    y = np.concatenate((np.ones(25), np.zeros(25)), axis=0)

    feature_names = ["x","y"]
    return x, y, feature_names

def load_data(scale=True):
    x, y, feature_names = createDataSet()
    x_train, x_test, y_train, y_test = \
        train_test_split(x, y, test_size=0.3,
                         shuffle=True, random_state=20)
    if scale:
        ss = StandardScaler()
        x_train = ss.fit_transform(x_train)
        x_test = ss.transform(x_test)
    return x_train, x_test, y_train, y_test,feature_names


def train(x_train, x_test, y_train, y_test):
    model = DecisionTreeClassifier(criterion="entropy",max_depth=3)
    model.fit(x_train, y_train)
    print("Accuracy: ", model.score(x_test, y_test))
    with open("tree.dot", 'w') as f:
        f = export_graphviz(model, out_file=f)

    r=export_text(model)
    print('decision tree',r)





if __name__ == '__main__':
    x_train, x_test, y_train, y_test, feature_names = load_data()
    print('training data')
    print(x_train, y_train)
    print('testing data')
    print(x_test, y_test)
    train(x_train, x_test, y_train, y_test)

