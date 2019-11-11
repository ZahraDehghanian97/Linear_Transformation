from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np
iris = datasets.load_iris()
Y = iris.target
t_matrix = [[1,-3],[-1,1],[3,-1]]
X = [iris.data[:, [0, 3]] , iris.data[:, [1, 2]], iris.data[:, [2, 3]]]
for i in range(0,3) :
    plt.figure(figsize=(1,2))
    dot = np.dot(X[i], t_matrix[i])
    plt.scatter(dot, dot, c=Y, s=20)
plt.show()
