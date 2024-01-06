
'''
 You must only run this file once you have ran api_scripts.py so that you can query the ids 
'''
 
import string
from youtube_transcript_api import YouTubeTranscriptApi
from utils import get_db_connection, parse_id
import sqlite3
from typing import Dict, List
import json


def get_percent_english(video_ids: List[str]) -> Dict[str, int]:
    """
    Given a list of youtube video ids, returns a dictionary that maps each of the
    ids to the percentage of the video that is english
    """
    count_dict: Dict[str, int] = {}
    total = 0
    for id in video_ids:
        total += 1
        print(total)
        # iterates through the ids to  find the korean subtitles for each youtube video
        try:
            transcript_list = YouTubeTranscriptApi.get_transcript(id, languages=['ko', 'ja'])
            count = 0
            total_count = 0

            # finds ths text within the video that is english 
            for t in transcript_list:
                text = t["text"]
                arr_words = text.split()
                for w in arr_words:
                    total_count += 1
                    for l in w:
                        if l in string.ascii_letters:
                            count += 1
                            break
            count_dict[id] = count/total_count
        except:
            count_dict[id] = None
    return count_dict

def add_percent_to_db(percent_dict) -> None:
    conn = get_db_connection()
    c = conn.cursor()
    for id in percent_dict:
        percent = percent_dict[id]
        if percent:
            percent = round(percent, 2) * 100
        print(id, percent)
        c.execute('''UPDATE mvs SET percent_english = ? WHERE id = ?''',
                   (percent, id))
    
    conn.commit()
    

def main():
    # # This queries all the ids from the movie list
    # conn = get_db_connection()
    # c = conn.cursor()
    # c.execute("SELECT id FROM mvs")
    # results = c.fetchall()
    # ids = []
    # for r in results:
    #     ids.append(r[0])
        
        
    # # Run this command to get a dictionary of id and percentages
    # percent_english = get_percent_english(ids)
    
    
    # Run this command by uncommenting this section and only run once to save the percentage
    # with open('../data/percent_english.json', 'w') as out_file:
    #     json.dump(percent_english, out_file, sort_keys = True, indent = 4,
    #             ensure_ascii = False)
    # percent_dict = percent_english
    
    # Run this command instead of saving to the percent_dict to capture data from the json file 
    with open('../data/percent_english.json') as json_file:
        percent_dict = json.load(json_file)
    add_percent_to_db(percent_dict)

main()