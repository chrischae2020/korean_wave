import pandas as pd
import sqlite3

from utils import get_db_connection, parse_id

path = 'data/'

def get_data():

  df_idols_all = pd.read_csv(path+'kpop_idols.csv')
  df_idols_boys = pd.read_csv(path+'kpop_idols_boy_groups.csv')
  df_idols_girls = pd.read_csv(path+'kpop_idols_girl_groups.csv')
  df_mvs = pd.read_csv(path+'kpop_music_videos.csv')

  df_mvs['Artist'] = df_mvs['Artist'].apply(lambda x: x.split(', ')[0]) # grab only first artist
  df_mvs.drop_duplicates(subset=['Video'], inplace=True, keep='last')
  df_mvs = df_mvs[df_mvs['Song Name'].notna()]


  conn = get_db_connection()
  c = conn.cursor()

  c.execute('DROP TABLE IF EXISTS idols;')
  c.execute('DROP TABLE IF EXISTS boy_groups;')
  c.execute('DROP TABLE IF EXISTS girl_groups;')
  c.execute('DROP TABLE IF EXISTS mvs;')
  # conn.commit()
  create_idols_table = '''
  CREATE TABLE IF NOT EXISTS idols (
    stage_name VARCHAR(255) NOT NULL,
    full_name VARCHAR(255),
    k_name VARCHAR(255),
    k_stage_name VARCHAR(255),
    dob VARCHAR(255),
    group_name VARCHAR(255),
    country VARCHAR(255),
    birthplace VARCHAR(255),
    other_group VARCHAR(255),
    gender VARCHAR(255),
    PRIMARY KEY (stage_name, group_name)
  );
  '''

  create_boys_table = '''
  CREATE TABLE IF NOT EXISTS boy_groups (
    name VARCHAR(255) PRIMARY KEY NOT NULL,
    short_name VARCHAR(255),
    k_name VARCHAR(255),
    debut VARCHAR(255),
    company VARCHAR(255),
    num_members INTEGER,
    num_members_og INTEGER,
    fanclub_name VARCHAR(255),
    active VARCHAR(255)
  );
  '''

  create_girls_table = '''
  CREATE TABLE IF NOT EXISTS girl_groups (
    name VARCHAR(255) PRIMARY KEY NOT NULL,
    short_name VARCHAR(255),
    k_name VARCHAR(255),
    debut VARCHAR(255),
    company VARCHAR(255),
    num_members INTEGER,
    num_members_og INTEGER,
    fanclub_name VARCHAR(255),
    active VARCHAR(255)
  );
  '''

  create_mvs_table = '''
  CREATE TABLE IF NOT EXISTS mvs (
    id VARCHAR(255) NOT NULL,
    release_date VARCHAR(255),
    artist VARCHAR(255) NOT NULL,
    song_name VARCHAR(255) NOT NULL,
    k_song_name VARCHAR(255),
    director_name VARCHAR(255),
    video_url VARCHAR(255) NOT NULL,
    type VARCHAR(255),
    release VARCHAR(255),
    views INTEGER,
    percent_english REAL,
    PRIMARY KEY (song_name, artist, video_url)
  );
  '''

  c.execute(create_idols_table)
  c.execute(create_boys_table)
  c.execute(create_girls_table)
  c.execute(create_mvs_table)

  for i in df_idols_all.values.tolist():
    c.execute('''INSERT INTO idols VALUES (?,?,?,?,?,?,?,?,?,?);''', tuple(i))

  for i in df_idols_boys.values.tolist():
    c.execute('''INSERT INTO boy_groups VALUES (?,?,?,?,?,?,?,?,?)''', tuple(i))

  for i in df_idols_girls.values.tolist():
    c.execute('''INSERT INTO girl_groups VALUES (?,?,?,?,?,?,?,?,?)''', tuple(i))

  for i in df_mvs.values.tolist():
    cols_to_insert = "id, release_date, artist, song_name, k_song_name, director_name, video_url, type, release"
    id = parse_id(i[5])
    data = (id,) + tuple(i)

    c.execute(f'''INSERT INTO mvs ({cols_to_insert})
    VALUES (?,?,?,?,?,?,?,?,?)''', data)

  conn.commit()

if __name__=='__main__':
  get_data()