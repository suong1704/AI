from mimetypes import init
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class k_means:
    def __init__(self, X, K, loop) -> None:
        self.X = X
        self.K = K
        self.loop = loop

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
        for k in range(K):
            points_belong_k = X[np.where(idx == k)]
            centroids[k] = np.mean(points_belong_k, axis=0,)
        return centroids

    def find_k_means(self):
        _, n = X.shape
        centroids = self.initialize_K_centroids(self.X, self.K) 
        centroid_history = np.zeros((self.loop, self.K, n))
        for i in range(self.loop):
            idx = self.find_closest_centroids(self.X, centroids)
            centroids = self.compute_means(self.X, idx, self.K)
        return centroids, idx

data = pd.read_csv('D:/AI/On CK/Countries-exercise.csv')
data.head(20)

# X = data.iloc[:, 1:3]
# X = np.array(X)
# print(X,type(X))

X = [[0.,1.,1.],[1.,1,0],[2,2,0.],[0,1,2.],[2,2,2.],[2,3,0.]]
X = np.array(X)
# plt.scatter(X[:,0], X[:,1])


KMEANS = k_means(X, 3, 10)
centroids, idx = KMEANS.find_k_means()
print("Tam cac cum: \n", centroids)
print("Kết quả phân cụm: \n" , idx)


    
