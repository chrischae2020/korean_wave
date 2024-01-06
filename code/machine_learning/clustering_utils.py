import os
import sqlite3
from matplotlib import cm, pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import Axes3D  # Not used but needed to make 3D plots

def get_db_connection(path = 'data/kpop.db') -> sqlite3.Connection:
    conn = sqlite3.connect(path)
    return conn


feature_columns = ["artist", "title", "percent_english", "num_members", "views"]
MAX_CLUSTERS = 10
cmap = cm.get_cmap('tab10', MAX_CLUSTERS)
output_dir = "output"

def elbow_point_plot(cluster, errors):
    """
    This function helps create a plot representing the tradeoff between the
    number of clusters and the inertia values.

    :param cluster: 1D np array that represents K (the number of clusters)
    :param errors: 1D np array that represents the inertia values
    """

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    plt.clf()
    plt.plot(cluster, errors)
    plt.xlabel('Number of Clusters')
    plt.ylabel('Inertia')
    plt.title('elbow_plot')
    plt.savefig(output_dir + "/elbow_plot.png")
    plt.show()

def visualize_songs_clusters(data, centroids=None, centroid_indices=None,
                             is_lib_kmean=False):
    """
    Visualizes the song data points and (optionally) the calculated k-means
    cluster centers.
    Points with the same color are considered to be in the same cluster.

    Optionally providing centroid locations and centroid indices will color the
    data points to match their respective cluster and plot the given centroids.
    Otherwise, only the raw data points will be plotted.

    :param data: 2D numpy array of song data
    :param centroids: 2D numpy array of centroid locations
    :param centroid_indices: 1D numpy array of centroid indices for each data point in data
    :return:
    """
    def plot_songs(fig, color_map=None):
        x, y, z = np.hsplit(data, 3)
        fig.scatter(x, y, z, c=color_map)

    def plot_clusters(fig):
        x, y, z = np.hsplit(centroids, 3)
        fig.scatter(x, y, z, c="black", marker="x", alpha=1, s=200)

    plt.clf()
    cluster_plot = centroids is not None and centroid_indices is not None

    ax = plt.figure(num=1).add_subplot(111, projection='3d')
    colors_s = None

    if cluster_plot:
        if max(centroid_indices) + 1 > MAX_CLUSTERS:
            print(f"Error: Too many clusters. Please limit to fewer than {MAX_CLUSTERS}.")
            exit(1)
        colors_s = [cmap(l / MAX_CLUSTERS) for l in centroid_indices]
        plot_clusters(ax)

    plot_songs(ax, colors_s)

    ax.set_xlabel(feature_columns[2])
    ax.set_ylabel(feature_columns[3])
    ax.set_zlabel(feature_columns[4])

    plot_name = "Girl MV clusterings"
    ax.set_title(plot_name)
    
    # Helps visualize clusters
    plt.gca().invert_xaxis()
    plt.savefig(output_dir + "/" + plot_name + ".png")
    plt.show()


def min_max_scale(data):
    """
    Pre-processes the data by performing MinMax scaling.

    MinMax scaling prevents different scales of the data features from
    influencing distance calculations.

    MinMax scaling is performed by
        X_new = (X - X_min) / (X_max - X_min),

    where X_new is the newly scaled value, X_min is the minimum and X_max is the
    maximum along a single feature column.

    :param data: 2D numpy array of raw data
    :return: preprocessed data
    """
    col_mins = np.min(data, axis=0)
    col_maxes = np.max(data, axis=0)
    return (data - col_mins) / (col_maxes - col_mins)
