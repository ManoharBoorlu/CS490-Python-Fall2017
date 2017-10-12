from sklearn.cluster import KMeans
import pandas
import matplotlib.pyplot as p

da = pandas.read_csv('Customers.csv',header=0)
d=da.as_matrix(columns=None)
k = KMeans(n_clusters=5, random_state=0)
k.fit(da)
labels=k.labels_
centroid=k.cluster_centers_
colors = ["r.","g.","b.","c.","y."]

for i in range(len(d)):
    p.plot(d[i][0],d[i][1],colors[labels[i]],markersize=10)  #plotting points

p.scatter(centroid[:,0],centroid[:,1], marker = ".", s=150, linewidths = 5, zorder =10,color='yellow')     #plotting centroids
p.show()