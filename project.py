import sqlite3

con = sqlite3.connect("data.db")
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS users")
cur.execute("DROP TABLE IF EXISTS tweets")


cur.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        location TEXT,
        name TEXT,
        followers_count INTEGER,
        statuses_count INTEGER,
        time_zone TEXT,
        verified BOOLEAN,
        lang TEXT,
        screen_name TEXT,
        description TEXT,
        created_at TEXT,
        favourites_count INTEGER,
        friends_count INTEGER,
        listed_count INTEGER
        
    )
""")


cur.execute("""
    CREATE TABLE tweets (
        user_id TEXT,
        user_key TEXT,
        created_at TEXT,
        created_str TEXT,
        retweet_count INTEGER,
        retweeted TEXT,
        favorite_count INTEGER,
        text TEXT,
        tweet_id TEXT,
        source TEXT,
        hashtags TEXT,
        expanded_urls TEXT,
        posted TEXT,
        mentions TEXT,
        retweeted_status_id TEXT,
        in_reply_to_status_id TEXT
    )
""")




con.commit()

con.close()
