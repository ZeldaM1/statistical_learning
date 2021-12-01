from sklearn.ensemble import AdaBoostClassifier
from sklearn import metrics
import numpy as np
##ascii
S = 115
M = 109
L = 108

##data
X_train = np.array([[1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3],[S, M, M, S, S, S, S, S, L, L, L]])
X_train = np.transpose(X_train,[1,0])
X_test = np.array([[1, M]])
y_train = np.array([-1, -1, 1, 1, -1, -1, -1, 1, 1, 1, 1])
y_test = np.array([-1])

# Create adaboost classifer object
AdaBC = AdaBoostClassifier(n_estimators=3,learning_rate=0.01)
# Train Adaboost Classifer
model = AdaBC.fit(X_train, y_train)
# Predict the response for test dataset
y_pred = model.predict(X_test)

# Model Accuracy
print('input X:(1, M), predicted results: {}, GT: {}'.format(y_pred, y_test))
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

