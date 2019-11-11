from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np
iris = datasets.load_iris()

Y = iris.target
t_matrix = [[1.2,-0.3],[-1.8,0.6],[1.4,0.5],[-0.5,-1]]
X = [iris.data[:, [0, 1]] , iris.data[:, [0, 2]], iris.data[:, [1, 3]]]
for i in range(0,3) :
    fig , myplt = plt.subplots(4)
    for j in range(0,4):
        dot = np.dot(X[i],t_matrix[j])
        myplt[j].scatter(dot,dot,c=Y ,s=20)
plt.show()
