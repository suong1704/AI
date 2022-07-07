from mimetypes import init
from tokenize import String
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class k_means:
    def __init__(self, X, K) -> None:
        self.X = X
        self.K = K

    def initialize_K_centroids(self, X, K):
        m,n = X.shape
        k_rand = np.ones((K, n))
        k_rand = X[np.random.choice(range(len(X)), K, replace=False),:]
        return k_rand

    def find_closest_centroids(self, X, centroids):
        m = len(X)
        c = np.zeros(m)
        for i in range(m):
            distances = np.linalg.norm(X[i] - centroids, axis=1)
            c[i] = np.argmin(distances)
        return c

    def compute_means(self, X, idx, K):
        m, n = X.shape
        centroids = np.zeros((K, n))
        cum = " "
        tam = " "
        for k in range(K):
            points_belong_k = X[np.where(idx == k)]
            centroids[k] = np.mean(points_belong_k, axis=0,)  
            cum =cum + "\n" + "Cụm " + str(k) + ": \n" + str(points_belong_k )
            tam =tam + "\n" +  "Tâm cụm "+ str(k) + ": \n"+ str(centroids[k])
        return centroids, cum, tam

    def find_k_means(self):
        _, n = X.shape
        tam = ""
        cum = ""
        centroids = self.initialize_K_centroids(self.X, self.K) 
        for i in range(10):
            idx = self.find_closest_centroids(self.X, centroids)
            centroids, cum , tam = self.compute_means(self.X, idx, self.K)
        return centroids, idx, cum , tam

data = pd.read_csv('D:/AI/On CK/Countries-exercise.csv')
data.head(20)

X = [[0.,1.,1.],[1.,1,0],[2,2,0.],[0,1,2.],[2,2,2.],[2,3,0.]]
X = np.array(X)


# K = 3
Kmeans  = k_means(X, K = 3)
centroids, idx, cum, tam = Kmeans .find_k_means()
print("Các đỉnh cần phân cụm: \n", X)
print("Tâm: \n",centroids)
print("Phân cụm theo thứ tự các đỉnh: \n", idx)
print(cum)
print(tam)

    
