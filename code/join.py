import sqlite3

from utils import get_db_connection, parse_id

path = '.\data\kpop.db'

def join_tables():
	conn = sqlite3.connect(path)
	c = conn.cursor()

	c.execute('DROP TABLE IF EXISTS solo_mvs;')
	c.execute('DROP TABLE IF EXISTS boy_mvs;')
	c.execute('DROP TABLE IF EXISTS girl_mvs;')

	create_solos_table = '''
		CREATE TABLE IF NOT EXISTS solo_mvs (
			id VARCHAR(255) PRIMARY KEY NOT NULL,
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
			stage_name VARCHAR(255) NOT NULL,
			full_name VARCHAR(255),
			k_name VARCHAR(255),
			k_stage_name VARCHAR(255),
			dob VARCHAR(255),
			group_name VARCHAR(255),
			country VARCHAR(255),
			birthplace VARCHAR(255),
			other_group VARCHAR(255),
			gender VARCHAR(255)
		);
		'''

	create_boys_table = '''
		CREATE TABLE IF NOT EXISTS boy_mvs (
			id VARCHAR(255) PRIMARY KEY NOT NULL,
			release_date VARCHAR(255),
			artist VARCHAR(255) NOT NULL,
			song_name VARCHAR(255),
			k_song_name VARCHAR(255),
			director_name VARCHAR(255),
			video_url VARCHAR(255) NOT NULL,
			type VARCHAR(255),
			release VARCHAR(255),
			views INTEGER,
			percent_english REAL,
			name VARCHAR(255) NOT NULL,
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
		CREATE TABLE IF NOT EXISTS girl_mvs (
			id VARCHAR(255) PRIMARY KEY NOT NULL,
			release_date VARCHAR(255),
			artist VARCHAR(255) NOT NULL,
			song_name VARCHAR(255),
			k_song_name VARCHAR(255),
			director_name VARCHAR(255),
			video_url VARCHAR(255) NOT NULL,
			type VARCHAR(255),
			release VARCHAR(255),
			views INTEGER,
			percent_english REAL,
			name VARCHAR(255) NOT NULL,
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
		
	c.execute(create_solos_table)
	c.execute(create_boys_table)
	c.execute(create_girls_table)

	# conn.commit()

	command1 = '''
		with solo as (SELECT * from idols
		WHERE group_name is NULL)

		SELECT * from mvs
		inner join solo on mvs.artist=solo.stage_name;
	'''
	command2 = '''
		select * from mvs inner join boy_groups on mvs.artist=boy_groups.name;
	'''

	command3 = '''
		select * from mvs inner join girl_groups on mvs.artist=girl_groups.name;
	'''

	c.execute(command1)
	for i in c.fetchall():
		c.execute('''INSERT INTO solo_mvs VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);''', tuple(i))

	c.execute(command2)
	for i in c.fetchall():
		c.execute('''INSERT INTO boy_mvs VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);''', tuple(i))

	c.execute(command3)
	for i in c.fetchall():
		c.execute('''INSERT INTO girl_mvs VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);''', tuple(i))

	conn.commit()

if __name__=='__main__':
  join_tables()