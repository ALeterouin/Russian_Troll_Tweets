import sqlite3
import csv
import os

def import_from_csv(tweets = "/Users/mac/Downloads/archive/data/tweets_filtered.csv") -> list[tuple]:
    data = []
    with open(tweets,"r") as f:
        reader = csv.reader(f)
        data = list(reader)
    return data

def import_from_csv(users = "/Users/mac/Downloads/archive/data/users_Update.csv")-> list[tuple]:
    data = []
    with open(users,"r") as f:
        reader = csv.reader(f)
        next(reader)
        data = list(reader)
    return data

conn = sqlite3.connect ("data.db")
cursor = conn.cursor()

def insert_into_tweets(tweets_data: list[tuple]):
    cursor.executemany("""
        INSERT INTO tweets (
            user_id, 
            user_key, 
            created_at, 
            created_str, 
            retweet_count, 
            retweeted, 
            favorite_count, 
            text, 
            tweet_id, 
            source, 
            hashtags, 
            expanded_urls, 
            posted, 
            mentions, 
            retweeted_status_id, 
            in_reply_to_status_id 
        ) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, tweets_data)

def insert_into_users(users_data: list[tuple]):
    cursor.executemany("""
        INSERT INTO users (
            id, 
            location, 
            name, 
            followers_count, 
            statuses_count, 
            time_zone, 
            verified, 
            lang, 
            screen_name, 
            description,
            created_at,
            favourites_count,
            friends_count,
            listed_count 
        ) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )
    """, users_data)
    


tweets_data = import_from_csv(os.path.abspath("/Users/mac/Downloads/archive/data/tweets_filtered.csv"))
users_data = import_from_csv(os.path.abspath("/Users/mac/Downloads/archive/data/users_Update.csv"))

insert_into_tweets(tweets_data)
insert_into_users(users_data)

conn.commit()
conn.close()
