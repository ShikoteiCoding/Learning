import numpy as np

from lib import kmeans

def generate_random_2d_clusters(number_points=100, number_centroids=3):
    """ Generate in 2D space random points. """
    # Assert here
    # Generate k number of "centroids"
    centroids = np.random.randint(0, 50, size=(number_centroids, 2))
    # Make those as coordinates
    points = centroids

    deltas = np.random.randint(-10, 10, size=(number_points - number_centroids, 2))

    for delta in deltas:
        # Pick one centroid
        one_centroid = centroids[np.random.randint(0, number_centroids)]
        # Create new coordinates from delta and centroid
        new_coordinates = one_centroid + delta
        # Add new coordinates to points
        points = np.append(points, [new_coordinates], axis=0)

    return points

if __name__ == "__main__":
    """  """
    points = generate_random_2d_clusters(100, 2)