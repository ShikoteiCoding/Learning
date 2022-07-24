import math
import numpy as np

def euclidian_distance(u, v):
    """ Compute distance between two points. """
    return np.sqrt((u[0] - v[0])**2 + (u[1] - v[1])**2)

def cost(points, clusters):
    """ Cost is sum of distances for each point to the centroid of their cluster """

def compute_centroid(points):
    """ Given points, compute the centroid. """
    x_coordinates = list(map(lambda c: c[0], points))
    y_coordinates = list(map(lambda c: c[1], points))

    return [np.mean(x_coordinates), np.mean(y_coordinates)]

def shorted_centroid(point, centroids):
    min_dist = +np.Inf
    nearest = None
    for centroid in centroids:
        curr_dist = euclidian_distance(centroid, point)
        if curr_dist < min_dist:
            nearest = centroid
            min_dist = curr_dist
    return nearest

def kmeans(points, number_cluster=3, max_iter=100):
    """ Self-made K-means algorithm """
    # Init clusters with random centroids
    centroid_indexes = np.random.randint(0, 50, size=number_cluster)
    centroids = points[centroid_indexes]
    clusters = {}

    # Till convergence or max_iter
    while max_iter < 100:
        max_iter -= 1
        
        # Reset clusters
        clusters = {} 
        for centroid in clusters:
            clusters[str(centroid)] = []

        # Give each point a cluster (nearest centroid)
        for point in points:
            nearest_centroid = shorted_centroid(point, centroids)
            clusters[str(nearest_centroid)].append(point)

        # Compute for each cluster the new centroid
        new_centroids = []
        for _, value in clusters.items():
            new_centroids.append(compute_centroid(value))
        centroids = new_centroids
    
    return clusters, centroids