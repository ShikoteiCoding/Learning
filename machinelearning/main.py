from functools import reduce
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from lib import kmeans
from lib import utils
from lib import pca

def demo_kmeans():
    points = utils.generate_random_2d_clusters(100, 3, 5)
    points_to_cluster, centroids = kmeans.kmeans(points)
    utils.scatter_plot_coordinates(points, points_to_cluster)

def demo_pca():
    df = pd.read_csv("data/devices_stats.csv")

    standard_df = pd.DataFrame()

    numeric_columns = [col for col in df.columns if df[col].dtype == float]

    for col in numeric_columns:
        standard_df[col + "_norm"] = pca.normalize_standard(df[col])
    
    print(standard_df)

if __name__ == "__main__":
    """  """
    demo_pca()