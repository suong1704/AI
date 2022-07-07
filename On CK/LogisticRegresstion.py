
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def prod(w, X):
   return np.dot(w.T, X)


def sigmoid(s):
   return 1 / (1 + np.exp(-s))


def my_logistic_sigmoid_regression(X, y, w_init, eta, epsilon=1e-3, M=10000):
   w = [w_init]
   N = X.shape[1]
   d = X.shape[0]
   count = 0
   check_w_after = 20
   while count < M:
       # mix data
       mix_id = np.random.permutation(N)
       for i in mix_id:
           xi = X[:, i].reshape(d, 1)
           yi = y[i]
           zi = sigmoid(np.dot(w[-1].T, xi))
           w_new = w[-1] + eta * (yi - zi) * xi
           count += 1
           # stopping criteria
           if count % check_w_after == 0:
               if np.linalg.norm(w_new - w[-check_w_after]) < epsilon:
                   return w
           w.append(w_new)
   return w

# method display
def display(w):
   # old
   # X0 = X[0, np.where(y == 0)][0]
   # new
   X0 = X[0, np.where(y == 0)][0]
   y0 = y[np.where(y == 0)]
   # old
   # X1 = X[0, np.where(y == 1)][0]
   X1 = X[0, np.where(y == 1)][0]
   y1 = y[np.where(y == 1)]

   plt.plot(X0, y0, 'ro', markersize=8)
   plt.plot(X1, y1, 'bs', markersize=8)
   xx = np.linspace(0, 6, 1000)
   w0 = w[-1][0][0]
   w1 = w[-1][1][0]
   threshold = -w0 / w1
   yy = sigmoid(w0 + w1 * xx)
   plt.axis([-2, 8, -1, 2])
   plt.plot(xx, yy, 'g-', linewidth=2)
   plt.plot(threshold, .5, 'y^', markersize=8)
   plt.xlabel('')
   plt.ylabel('')
   plt.show()

if __name__ == '__main__':
   print("ok")
   X1 = pd.read_csv('D:/AI/On CK/input.csv')
   X2 = X1[['sepal_length','sepal_width','petal_length','petal_width']]
   X = [X2['sepal_length'],X2['sepal_width'],X2['petal_length'],X2['petal_width']]
   X = np.array(X)
   y1 = X1[['Labeling']]
   y = y1['Labeling'].replace({'Iris-setosa' : 1 , 'Iris-versicolor' : 0})
   y = np.array(y)
   Xbar = np.concatenate((np.ones((1, X.shape[1])), X), axis=0)
   epsilon = .05
   d = Xbar.shape[0]
   w_init = np.random.randn(d, 1)
   w = my_logistic_sigmoid_regression(Xbar, y, w_init, epsilon)
   print(w[-1].T)
   print(sigmoid(np.dot(w[-1].T, Xbar)))
   display(w)

