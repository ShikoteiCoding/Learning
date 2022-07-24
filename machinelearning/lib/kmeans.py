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
    nearest = None
    for centroid in centroids:
        curr_dist = dist_func(centroid, point)
        if curr_dist < min_dist:
            nearest = centroid
            min_dist = curr_dist
    return nearest

def kmeans(points, number_cluster=3, max_iter=100, dist_func=euclidian_distance):
    """ Self-made K-means algorithm """
    # Init clusters with random centroids
    centroid_indexes = np.random.randint(0, 50, size=number_cluster)
    centroids = points[centroid_indexes]
    clusters = {}

    # Till convergence or max_iter
    while max_iter > 0:
        max_iter -= 1
        
        # Reset clusters
        clusters = {} 
        for centroid in centroids:
            clusters[str(centroid)] = []
        # Give each point a cluster (nearest centroid)
        for point in points:
            nearest_centroid = shortest_centroid(point, centroids, dist_func)
            clusters[str(nearest_centroid)].append(point)

        # Compute for each cluster the new centroid
        new_centroids = []
        for _, value in clusters.items():
            new_centroids.append(compute_centroid(value))
        centroids = new_centroids
    
    return clusters, centroids