from flask_executor import Executor
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from flask import current_app as app
from random import randint
import time
import matplotlib
matplotlib.use('TkAgg')
#-------------------------------- KMEANS ALGO CODE---------------->
class KMeansAlgo:
    def __init__(self):
        self.executor = Executor(app)
    def barplot(self, clusters, counts, centroids):
        x_pos = np.arange(clusters)
        suma = sum(counts)
        height = [int(x*100/suma) for x in counts]
        colors = []
        for tup in centroids:
            colors.append((tup[0]/255.0, tup[1]/255.0, tup[2]/255.0, 1.0))
        plt.bar(x_pos, height=height, color=colors, edgecolor='k')
        plt.title('Bar Plot for dominant colors Vs percentage of their distribution')
        plt.xticks(range(clusters))
        plt.xlabel('Num of Dominant colors')
        plt.ylabel('Percentage of Acquired Distribution')
        output_file_name = f'output-{randint(1, 1000)}.png'
        plt.savefig(f'app/static/{output_file_name}', dpi=400)
        plt.close()
        return output_file_name

    def kmeansalgo(self, img, max_Itr=500):
        im = np.array(img)[:, :, :3]
        m, n, c = im.shape[0], im.shape[1], im.shape[2]
        im = im.reshape(m*n,3)
        clusters = self.WCSS(im)
        kmean_obj = KMeans(n_clusters=clusters, n_init=1, max_iter=max_Itr, init='k-means++')
        kmean_obj.fit(im)
        labels = kmean_obj.labels_
        centroids = kmean_obj.cluster_centers_
        labels = labels.reshape(m,n)
        new_img = np.zeros((m,n,c))
        counts = [0]*clusters
        for i in range(m):
            for j in range(n):
                counts[labels[i, j]] += 1
                new_img[i,j] = centroids[labels[i,j]]
        return self.barplot(clusters, counts, centroids)

    def WCSS(self, image_array):
        wcss = []
        for i in range(1, 11):
            wcss.append(self.wcss_calculator(i, image_array))
        dominant_colors = 1
        avg_inertia = (sum(wcss) - max(wcss))/(len(wcss)-1)
        mini = max(wcss)
        for i in range(len(wcss)):
            if abs(wcss[i]-avg_inertia) < mini:
                mini = abs(wcss[i]-avg_inertia)
                dominant_colors = i+1
        return dominant_colors


    def wcss_calculator(self, n_clusters, image_array):
        kmeans = KMeans(n_clusters=n_clusters, init='k-means++', random_state=42, max_iter=10)
        kmeans.fit(image_array)
        return kmeans.inertia_
