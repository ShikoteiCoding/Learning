import numpy as np

from functools import reduce
import matplotlib.pyplot as plt

def scatter_plot_coordinates(points, points_to_cluster):
    """ Plot coordinates as a scatter. """

    #points = np.array(reduce(lambda prev, next: prev + next, clusters.values(), []))
    #colors = np.array(reduce(lambda prev, next: prev + [next[0]] * len(next[1][1]), enumerate(clusters.items()), []))

    plt.scatter(points[:,0], points[:,1], c=points_to_cluster) # type: ignore
    plt.show()

def generate_random_2d_clusters(number_points=100, number_centroids=3, max_delta=5):
    """ Generate in 2D space random points. """
    # Assert here
    assert number_points >= number_centroids, \
        "Please make the number of point greater or equal to the number of centroid."
    # Generate k number of "centroids"
    centroids = np.random.randint(0, 50, size=(number_centroids, 2))
    # Make those as coordinates
    points = centroids
    deltas = np.random.randint(-max_delta, max_delta, size=(number_points - number_centroids, 2))

    for delta_point in deltas:
        # Pick one centroid
        one_centroid = centroids[np.random.randint(0, number_centroids)]
        # Create new coordinates from delta and centroid
        new_coordinates = one_centroid + delta_point
        # Add new coordinates to points
        points = np.append(points, [new_coordinates], axis=0)

    return points