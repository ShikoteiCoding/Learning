import numpy as np
import matplotlib.pyplot as plt

from lib import kmeans
from lib import utils

def scatter_plot_coordinates(points):

    x_coordinates = list(map(lambda c: c[0], points))
    y_coordinates = list(map(lambda c: c[1], points))


    plt.scatter(x_coordinates, y_coordinates)
    plt.show()

if __name__ == "__main__":
    """  """
    points = utils.generate_random_2d_clusters(100, 3, 6)
    scatter_plot_coordinates(points)