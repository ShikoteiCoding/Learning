import math
import numpy as np

def euclidian_distance(u, v):
    """ Compute distance between two points. """
    return np.sqrt((u[0] - v[0])**2 + (u[1] - v[1])**2)

def cost(points, clusters):
    """ Cost is sum of distances for each point to the centroid of their cluster """

def compute_centroid(points):
    """ Given points, compute the centroid. """
    return np.mean(points, axis=0)

def shortest_centroid(point, centroids, dist_func=euclidian_distance):
    min_dist = +np.Inf
    nearest_index = 0
    for i in range(len(centroids)):
        curr_dist = dist_func(centroids[i], point)
        if curr_dist < min_dist:
            nearest_index = i
            min_dist = curr_dist
    return nearest_index

def kmeans(points, number_cluster=3, max_iter=100, dist_func=euclidian_distance):
    """ Self-made K-means algorithm """
    n = len(points)

    # Init clusters with random centroids
    centroid_indexes = np.random.randint(0, 50, size=number_cluster)
    centroids = points[centroid_indexes]

    # Each point position is labeled with the cluster 
    points_to_cluster = [0] * n
    # Each cluster stores it's points
    clusters_to_point = []

    # Till convergence or max_iter
    while max_iter > 0:
        max_iter -= 1

        # Reset the clusters for each iteration
        clusters_to_point = [[] for _ in range(number_cluster)]

        # Give each point a cluster (nearest centroid)
        for i in range(n):
            nearest_centroid_index = shortest_centroid(points[i], centroids, dist_func)
            points_to_cluster[i] = nearest_centroid_index
            clusters_to_point[nearest_centroid_index].append(points[i])

        # Compute for each cluster the new centroid
        new_centroids = []
        for cluster in clusters_to_point:
            new_centroids.append(compute_centroid(cluster))
        centroids = new_centroids
    
    return points_to_cluster, centroids