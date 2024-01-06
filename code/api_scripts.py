import googleapiclient.discovery
import pandas
from typing import Dict, List
from utils import get_db_connection, parse_id
from keys import YT_API_KEY

def read_yt_video_ids(file_name: str) -> List[str]:
    """
    Reads in a list of youtube video ids from a CSV file with each video's url.
    """
    # the column name that the video urls are stored under in the CSV file
    URL_COL_NAME = "Video"
    
    df = pandas.read_csv(file_name)
    urls = df[URL_COL_NAME]
    return [parse_id(url) for url in urls]

# Create a YouTube API client
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=YT_API_KEY)

def get_yt_videos_views(video_ids: List[str]) -> Dict[str, int]:
    """
    Given a list of youtube video ids, returns a dictionary that maps each of the
    ids to that video's number of views.
    """
    views_dict: Dict[str, int] = {}
    # Since YT API caps at 50 videos per request, we need to batch our calls
    num_vids = len(video_ids)
    batch_size = 50
    for i in range(0, num_vids, batch_size):
        vid_batch = video_ids[i : i+batch_size]

        # create and execute the request
        serialized_ids = ','.join(vid_batch)
        request = youtube.videos().list(
            part="statistics",
            id=serialized_ids
        )
        response = request.execute()

        # Extract the number of views from the returned video resource and append to dictionary
        vids = response["items"][:]
        for vid in vids:
            id = vid["id"]
            views = vid["statistics"].get("viewCount")
            if views:
                # Vids excluded: ycYLPbtxU1Q, pBqR8vhBJlo
                views_dict[id] = views
    
    return views_dict

def add_yt_views_to_db(views_dict: Dict[str, int]) -> None:
    conn = get_db_connection()
    c = conn.cursor()
    for id in views_dict:
        views = views_dict.get(id)
        c.execute('''UPDATE mvs SET views = ? WHERE id = ?''',
                   (views, id))

    conn.commit()


def main():
    MV_CSV_FILE_NAME = "data/kpop_music_videos.csv"
    ids = read_yt_video_ids(MV_CSV_FILE_NAME)
    views = get_yt_videos_views(ids)

    # TODO: determine what we should do with old video statistics. Might not be representative due to being uploaded at a later date (for example, https://www.youtube.com/watch?v=KGcwGoXfUDk was originally released 1992-03-23, but listed mv was uploaded Oct 11, 2013. Same would apply to other data sources like spotify data).

    # print(percent_english)
    # print(views)
    add_yt_views_to_db(views)

if __name__ == "__main__":
    main()
