import numpy as np
import matplotlib.pyplot as plt

from lib import kmeans
from lib import utils

if __name__ == "__main__":
    """  """
    points = utils.generate_random_2d_clusters(100, 3, 6)

    clusters, centroids = kmeans.kmeans(points)

    print(len(clusters))
    print(centroids)

    utils.scatter_plot_coordinates(points)