import numpy as np

import matplotlib.pyplot as plt

def scatter_plot_coordinates(points):

    x_coordinates = list(map(lambda c: c[0], points))
    y_coordinates = list(map(lambda c: c[1], points))

    plt.scatter(x_coordinates, y_coordinates)
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