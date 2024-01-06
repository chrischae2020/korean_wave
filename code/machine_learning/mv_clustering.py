from typing import List, Tuple
import numpy as np
from scipy import stats
from clustering_utils import min_max_scale, visualize_songs_clusters, elbow_point_plot, get_db_connection
from kmeans import sk_learn_cluster, Kmeans


def read_data(table: str) -> List[Tuple[str]]:
    conn = get_db_connection()
    cur = conn.cursor()
    if table == "mvs":
        cur.execute('''SELECT artist, song_name, views, percent_english FROM mvs
            WHERE percent_english IS NOT NULL AND views IS NOT NULL
            ''')
    elif table == "boy_mvs":
        cur.execute('''SELECT artist, song_name, percent_english, num_members, views FROM boy_mvs
            WHERE percent_english IS NOT NULL AND views IS NOT NULL
            ''')
    elif table == "girl_mvs":
        cur.execute('''SELECT artist, song_name, percent_english, num_members, views FROM girl_mvs
            WHERE percent_english IS NOT NULL AND views IS NOT NULL
            ''')

    rows = np.array(cur.fetchall())
    numeric_data = rows[:, 2:].astype(np.float)

    # Calculate z-score for all data points (how many standard deviations away from mean) for each column
    z = np.abs(stats.zscore(numeric_data))
    # Find all the rows where all values in each row have a z-score less than 3
    ind = np.all((z < 3), axis=1)
    data = numeric_data[ind]

    print(data.shape)
    print(type(data))
    print(type(data[0]))
    for d in data[:20]:
        print(d)
    cur.close()

    return data

def make_elbow_plot(data, max_iters):
    num_clusters = range(1, 10)
    inertias = []
    for k in num_clusters:
        centroids, idx = sk_learn_cluster(data, k, max_iters)
        inertias.append(Kmeans.inertia(data, centroids, idx))
    elbow_point_plot(num_clusters, inertias)



def cluster_mvs(data, max_iters=300):
    # perform clustering on last 2 columns (views and percent_english)
    # feature_data = data[:, 2:].astype(np.float)
    scaled_data = min_max_scale(data)
    # visualize_songs_clusters(scaled_data)

    make_elbow_plot(scaled_data, max_iters);
    # determined ideal k based on elbow plot
    k = 4
    centroids, idx = sk_learn_cluster(scaled_data, k, max_iters)

    visualize_songs_clusters(scaled_data, centroids, idx)

    print(centroids)


def main():
    """
    Main function for running mv clustering.
    """
    data = read_data("girl_mvs")
    max_iters = 300  # Number of times the k-mean should run
    cluster_mvs(data, max_iters)


if __name__ == '__main__':
    main()
