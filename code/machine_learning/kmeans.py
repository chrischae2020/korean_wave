import random
import numpy as np
from sklearn.cluster import KMeans


class Kmeans:
    def __init__(self, X, K, max_iters):
        # Data
        self.X = X
        # Number of clusters
        self.K = K
        # Number of maximum iterations
        self.max_iters = max_iters
        # Initialize centroids
        self.centroids = self.init_centroids()

    def init_centroids(self):
        """
        Selects k random rows from inputs and returns them as the chosen centroids.
        You should randomly choose these rows without replacement and only
        choose from the unique rows in the dataset. Hint: look at
        Python's random.sample function as well as np.unique
        :return: a Numpy array of k cluster centroids, one per row
        """
        out = np.array(random.sample(list(np.unique(self.X, axis=0)), self.K))
        # print("Data shape:", self.X.shape)
        # print("intial centroids shape:", out.shape)
        # print("Initial centroids:", out)
        return out


    # not used
    def euclidean_dist(self, x, y):
        """
        Computes the Euclidean distance between two points, x and y

        :param x: the first data point, a Python numpy array
        :param y: the second data point, a Python numpy array
        :return: the Euclidean distance between x and y
        """
        return np.linalg.norm(x - y)

    @staticmethod
    def dist_from_centroids(pt, centroids):
        """
        :param pt: array of shape (n, 1, d,), where d = dimension of each point, n = number of points
        :param centroids: array of shape (1, k, d) representing the centroids
        :return: an array that contains the euclidean distance between the point and each centroid
        """
        return np.sum(np.square(pt - centroids), axis=-1)


    def closest_centroids(self):
        """
        Computes the closest centroid for each data point in X, returning
        an array of centroid indices

        :return: an array of centroid indices
        """

        # reshape data and centroids to allow us to use numpy vectorization and broadcasting
        data = np.expand_dims(self.X, 1)
        centroids = np.expand_dims(self.centroids, 0)

        # get distances from centroids
        distances = Kmeans.dist_from_centroids(data, centroids)
        # get indices of closest centroid to each point (where distance is minimized)
        closest = np.argmin(distances, axis=1)
        return closest



    def compute_centroids(self, centroid_indices):
        """
        Computes the centroids for each cluster, or the average of all data points
        in the cluster. Update self.centroids.

        Check for convergence (new centroid coordinates match those of existing
        centroids) and return a Boolean whether k-means has converged

        :param centroid_indices: a Numpy array of centroid indices, one for each datapoint in X
        :return boolean: whether k-means has converged
        """
        
        old_centroids = np.copy(self.centroids)
        # calculate and assign new centroids
        for ci in range(len(self.centroids)):
            cluster = self.X[centroid_indices == ci]
            new_centroid = cluster.mean(axis=0)
            self.centroids[ci] = new_centroid
        
        # return whether the new centroids are the same as the old
        return np.all(old_centroids == self.centroids)



    def run(self):
        """
        Run the k-means algorithm on dataset X with K clusters for max_iters.
        Make sure to call closest_centroids and compute_centroids! Stop early
        if algorithm has converged.
        :return: a tuple of (cluster centroids, indices for each data point)
        Note: cluster centroids and indices should both be numpy ndarrays
        """
        
        for _ in range(self.max_iters):
            # start_time = time.time()
            centroid_indices = self.closest_centroids()
            # duration = time.time() - start_time
            # print("Determining closest centroids took", duration, "secs")
            if self.compute_centroids(centroid_indices):
                break
        
        return self.centroids, self.closest_centroids()

    @staticmethod
    def inertia(X, centroids, centroid_indices):
        """
        Returns the inertia of the clustering. Inertia is defined as the
        sum of the squared distances between each data point and the centroid of
        its assigned cluster.

        :param centroids - the coordinates that represent the center of the clusters
        :param centroid_indices - the index of the centroid that corresponding data point it closest to
        :return inertia as a float
        """
        total_inertia = 0.0
        for ci, centroid in enumerate(centroids):
            cluster_pts = X[centroid_indices == ci]
            distances = Kmeans.dist_from_centroids(cluster_pts, centroid)
            inertia = np.sum(np.square(distances))
            total_inertia += inertia
        return total_inertia

def sk_learn_cluster(X, K, max_iter=300):
    """
    Performs k-means clustering using library functions (scikit-learn). You can
    experiment with different initialization settings, but please initialize
    without any optional arguments (other than n_clusters) before submitting.

    :param X: 2D np array containing features of the songs
    :param K: number of clusters
    :return: a tuple of (cluster centroids, indices for each data point)
    """
    kmeans = KMeans(n_clusters=K, max_iter=max_iter).fit(X)
    predictions = kmeans.predict(X)
    return kmeans.cluster_centers_, predictions