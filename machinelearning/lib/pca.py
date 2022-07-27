import pandas as pd

def normalize_standard(serie):
    """ Normalize a variable through standard score. """

    mu = serie.mean()
    sigma = serie.std()

    return (serie - mu) / sigma


def pca(dataset, standard_func = normalize_standard):
    """ Custom simple PCA algorithm """
    # Standardization

    # Covariance matrix

    # Eigen vectors + Eigen values of covariance matrix

    # Feature vector
 