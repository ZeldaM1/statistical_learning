import numpy as np

from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
def svm(C=1.0, kernel="rbf"):
    return SVC(C=C, kernel=kernel, max_iter=-1, random_state=0)


def bayes():
    return GaussianNB()

def train(X, y, classifier):
    return classifier.fit(X, y)

def test(X, classifier):
    return classifier.predict(X)

def acc(X, y, classifier):
    return classifier.score(X, y)

X_train = np.array([[1,2,3,2,3],[2,3,3,1,2]])
X_train = np.transpose(X_train,[1,0])

Y_train = np.array([1,1,1,-1,-1])
X_test = np.array([[1,2],[2,3]])
Y_test = np.array([1,1])

print("training ...")

classifier = train(X_train, Y_train, svm(1.0, "rbf"))     # 96.82%



print('train accuray',acc(X_train, Y_train, classifier))
print("testing ...")
print('test accuray',acc(X_test, Y_test, classifier))