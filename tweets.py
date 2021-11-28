from dotenv import load_dotenv
import os
import tweepy

load_dotenv()

consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def get_tweets(query, count):
    try:
        tweet_list = api.search_tweets(q=query,lang="en", result_type="mixed",count=count)
        return tweet_list
    except tweepy.TweepyException as e:
        print("Error",e)
        return None

    