import numpy as np
import matplotlib.pyplot as plt

from lib import kmeans
from lib import utils

def plot_points(points):

    plt.plot(points)

if __name__ == "__main__":
    """  """
    points = utils.generate_random_2d_clusters(100, 2)
    plot_points(points)