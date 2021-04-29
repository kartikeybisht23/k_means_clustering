import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from copy import deepcopy

x=load_iris()
data=x["data"]
labels=x["target"]

class Kmeans():
    def __init__(self,k=3,tolerance=0.1,max_iter=100):
        self.max_iter=max_iter
        self.k=k
        self.tolerance=tolerance
    def calc_dist(self,a,b):
        return (np.sum((a-b)**2))**0.5
    
    def fit(self,data):
        #self.centroid=data[:self.k]
        colours=["red","green","blue"]
        np.random.shuffle(data)
        self.centroids=np.array([data[i] for i in range(self.k)])

        a=0
        while a<self.max_iter:
            clusters={}
        
           
        
            for i in range(self.k):
                clusters[i]=[]
        

            for pt in data:
                #dist=np.array([calc_dist(pt,self.centroids[i]) for i in range(self.k)])
                dist=np.array([self.calc_dist(pt,self.centroids[i])for i in range(self.k)])
                #print(dist)
                print(clusters)
                clusters[dist.argsort()[0]].append(pt)
        #print(clusters)
         
            init_centroids=deepcopy(self.centroids)
            for i in range(self.k):
                clusters[i]=np.array(clusters[i])
                self.centroids[i]=np.average(clusters[i],axis=0)
            value=[self.calc_dist(init_centroids[i],self.centroids[i])<self.tolerance for i in range(self.k)]
            print(value)
            if sum(value)==3:
                break
            a=a+1    
            
        for i in range(self.k):
            plt.scatter(init_centroids[i,0],init_centroids[i,1],color=colours[i],marker="*",s=300)   
        #for i in range(len(data)):
            #plt.scatter(data[i,0],data[i,1],color="black")
        for i in range(self.k):
            for j in range(len(clusters[i])):
                plt.scatter(clusters[i][j,0],clusters[i][j,1],color=colours[i])
        for i in range(len(self.centroids)):
            plt.scatter(self.centroids[i,0],self.centroids[i,1],color=colours[i],marker="+",s=400)
        plt.show()        

    def predict(self,test):
        print(hasattr(self,"centroids"))
        pred=[]
        for i in test:
            test_dist=np.array([self.calc_dist(test,self.centroids[i])for i in range(self.k)])
            test_cluster=np.argsort(test_dist)[0]
            pred.append(test_cluster)
        return pred        
            
