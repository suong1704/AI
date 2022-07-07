from mimetypes import init
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class k_means:
    def __init__(self, X, K, loop=10) -> None:
        self.X = X
        self.K = K
        self.loop = loop

    def initialize_K_centroids(self, X, K):
        m,n = X.shape
        k_rand = np.ones((K, n))
        k_rand = X[np.random.choice(range(len(X)), K, replace=False),:]
        return k_rand
    #  Compute distances
    def find_closest_centroids(self, X, centroids):
        m = len(X)
        c = np.zeros(m)
        for i in range(m):
            distances = np.linalg.norm(X[i] - centroids, axis=1)
            c[i] = np.argmin(distances)
        return c
    #  Update centroids
    def compute_means(self, X, idx, K):
        m, n = X.shape
        centroids = np.zeros((K, n))
        for k in range(K):
            points_belong_k = X[np.where(idx == k)]
            centroids[k] = np.mean(points_belong_k, axis=0,)
        return centroids

    def find_k_means(self,X, K, max_iters=10):
        _, n = X.shape
        centroids = self.initialize_K_centroids(X, K) 
        centroid_history = np.zeros((max_iters, K, n))
        for i in range(max_iters):
            idx = self.find_closest_centroids(X, centroids)
            centroids = self.compute_means(X, idx, K)
        return centroids, idx

data = pd.read_csv('D:/AI/On CK/Countries-exercise.csv')
data.head(20)

# X = data.iloc[:, 1:3]
# X = np.array(X)
# print(X,len(X))

X = [[3.0, 12],[6.0,9],[4.5,12],[12.0,3],[15.0,6],[12.0,15],[9.0,18],[9.0,12]]
X = np.array(X)
# print(X,type(X))
# plt.scatter(X[:,0], X[:,1])


KMEANS = k_means(X, 4)
centroids, idx = KMEANS.find_k_means(X,4)

print(centroids, idx)


    
