from textblob import Blobber
from textblob.sentiments import NaiveBayesAnalyzer
from tweets import get_tweets
import pandas as pd

def analyze_tweets(tweets):
    public_tweets = []
    tb = Blobber(analyzer=NaiveBayesAnalyzer())
    for tweet in tweets:
        blob = tb(str(tweet.text))
        print(tweet.user.name)
        score = {
            "tweet": tweet.text,
            "name": tweet.user.name,
            "screen_name": tweet.user.screen_name,
            "profile_pic": tweet.user.profile_image_url,
            "verified": tweet.user.verified,
            "created_at": tweet.created_at,
            "retweets": tweet.retweet_count,
            "favorites": tweet.favorite_count,
            "classification": blob.sentiment[0],
            "p_pos": blob.sentiment[1],
            "p_neg": blob.sentiment[2],
        }
        public_tweets.append(score)
    df = pd.DataFrame(public_tweets)
    return df

def get_classification(tweet_data):
    pos_sentiments = sum(tweet_data["p_pos"].tolist())
    neg_sentiments = sum(tweet_data["p_neg"].tolist())
    if neg_sentiments == 0:
        return pos_sentiments
    ratio = pos_sentiments/neg_sentiments
    return ratio

