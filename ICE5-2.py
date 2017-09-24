import numpy as np
import matplotlib.pyplot as plt
import random

def cluster_content(X, mu):
    cluster = {}
    for x in X:
        value = min([(i[0],np.linalg.norm(x - mu[i[0]]))for i in enumerate(mu)], key=lambda s:s[1])[0]
        try:
            cluster[value].append(x)
        except:
            cluster[value] = [x]
    return cluster


def new_center(mu, cluster):
    keys =sorted(cluster.keys())
    newmu = np.array([(np.mean(cluster[k],axis = 0))for k in keys])
    #for k in keys:
    #    newmu.append(np.mean(cluster[k],axis = 0))
    return newmu

def matched(newmu, oldmu):
    return (set([tuple(a)for a in newmu]) == set([tuple(a)for a in oldmu]))

def Apply_Kmeans(X, K, N):
    temp1 = np.random.randint(N, size = K)
    oldmu = np.array([X[i]for i in temp1])
    temp2 = np.random.randint(N, size=K)
    newmu = np.array([X[i] for i in temp2])
    cluster = cluster_content(X, oldmu)
    itr = 0
    plot_cluster(oldmu,cluster,itr)
    while not matched(newmu, oldmu):
        itr = itr + 1
        oldmu = newmu
        cluster = cluster_content(X,newmu)
        plot_cluster(newmu, cluster,itr)
        newmu = new_center(newmu, cluster)
    plot_cluster(newmu, cluster, itr)
    return

def plot_cluster(mu,cluster, itr):
    color = 10 * ['r.','g.','k.','c.','b.','m.']
    print('Iteration number : ',itr)
    for l in cluster.keys():
        for m in range(len(cluster[l])):
            plt.plot(cluster[l][m][0], cluster[l][m][1], color[l], markersize=10)
    plt.scatter(mu[:,0],mu[:,1],marker = 'x', s = 150, linewidths = 5, zorder = 10)
    plt.show()

def init_graph():
    Height=np.array([6,5,6,6,4,5,4,6,6,5])
    Weight=np.array([90,65,85,100,45,70,50,67,86,60])
    X=np.column_stack([Height,Weight])
    return X


def Simulate_Clusters():
    print(".........Starting Cluster Simulation.........")
    K = 3
    X = init_graph()
    #for x in X:
    #    plt.plot(x[0],x[1])
    plt.scatter(X[:, 0], X[:, 1])
    plt.show()
    temp = Apply_Kmeans(X, K, 10)

if __name__ == '__main__':
    Simulate_Clusters()