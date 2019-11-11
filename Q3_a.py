from sklearn import datasets
import matplotlib.pyplot as plt

iris = datasets.load_iris()
X = iris.data
Y = iris.target
plt.figure(0)
plt.figure(figsize=(1,2))
plt.scatter(X[:,0],X[:,1], c=Y ,s=20)
plt.figure(1)
plt.figure(figsize=(1,2))
plt.scatter(X[:,0],X[:,2], c=Y ,s=20)
plt.figure(2)
plt.figure(figsize=(1,2))
plt.scatter(X[:,1],X[:,3], c=Y ,s=20)
plt.show()
