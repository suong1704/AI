import numpy as np

def pred (w, x):
    return np.sign(np.dot(w.T, x))

def has_converged (x, y, w): 
    return np.array_equal(pred (w, x), y)

def perceptron (x, y, w_init):
    w = [w_init]
    d = x.shape[0]
    mis_points = []
    while True:
    # mix data
        mix_id = np.random.permutation (x.shape[1])
        for i in range(x.shape[1]): 
            xi = x[:, mix_id[i]].reshape(d, 1)
            yi = y[0, mix_id[i]]
            if pred(w[-1], xi)[0] != yi:
                mis_points.append(mix_id[i]) 
                w_new = w[-1] + yi * xi
                w.append(w_new)
        if has_converged(x, y, w[-1]):
            break
    return (w, mis_points)

if __name__ == '__main__':
    means = [[-1, 0], [1, 0]] 
    cov = [[.3, .2], [.2, .3]]
    N = 18
    X0= np.random.multivariate_normal (means[0], cov, N).T
    X1 = np.random.multivariate_normal (means[1], cov, N).T 
    X = np.concatenate((X0, X1), axis=1)
    y = np.concatenate((np.ones((1, N)), -1 * np.ones((1, N))), axis=1)
    #Xbar
    Xbar = np.concatenate((np.ones((1, 2 * N)), X), axis=0)
    w_init = np.random.randn(Xbar.shape[0], 1)
    (w, m) = perceptron(Xbar, y, w_init)
    print (w[-1].T)