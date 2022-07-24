import numpy as np
import matplotlib.pyplot as plt

from lib import kmeans
from lib import utils

if __name__ == "__main__":
    """  """
    points = utils.generate_random_2d_clusters(100, 3, 6)

    print(kmeans.kmeans(points))

    #utils.scatter_plot_coordinates(points)

    #print(kmeans.euclidian_distance([0, 0], [1, 1]))
    #print(kmeans.compute_centroid(points))