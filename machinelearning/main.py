from functools import reduce
import numpy as np
import matplotlib.pyplot as plt

from lib import kmeans
from lib import utils

if __name__ == "__main__":
    """  """
    points = utils.generate_random_2d_clusters(100, 3, 5)
    points_to_cluster, centroids = kmeans.kmeans(points)
    utils.scatter_plot_coordinates(points, points_to_cluster)