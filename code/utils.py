import sqlite3

def parse_id(url: str) -> str:
    """
    Given youtube video's url, returns that video's id
    """
    # prefix of vid urls to remove
    URL_PREFIX = "https://youtu.be/"
    return url[len(URL_PREFIX):]

def get_db_connection(path = 'data/kpop.db') -> sqlite3.Connection:
    conn = sqlite3.connect(path)
    return conn
