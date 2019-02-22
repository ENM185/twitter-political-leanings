import tweepy
import json
import os.path
from collections import Counter
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

with open(os.path.dirname(__file__)+"politicians/politicians.json") as politicians_file:
    politicians = json.load(politicians_file)

with open(os.path.dirname(__file__) + "twitter_keys.json") as keys_file:
    keys = json.load(keys_file)

consumer_key = keys["consumer_key"]
consumer_secret = keys["consumer_secret"]
access_token = keys["access_token"]
access_token_secret = keys["access_token_secret"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

stop_words = set(stopwords.words("english"))
republican_counter = Counter()
democrat_counter = Counter()

for politician in filter(lambda x: x["party"]=="Republican", politicians["senators"]):
    print(politician["twitter-handle"]) #for logging
    tweets = api.user_timeline(id=politician["twitter-handle"], count=100)
    for tweet in tweets:
        arr = filter(lambda x: x not in stop_words, tweet.text.lower().split())
        for word in arr:
            republican_counter[word] += 1


for politician in filter(lambda x: x["party"]=="Democrat", politicians["senators"]):
    print(politician["twitter-handle"]) #for logging
    tweets = api.user_timeline(id=politician["twitter-handle"], count=100)
    for tweet in tweets:
        arr = filter(lambda x: x not in stop_words, tweet.text.lower().split())
        for word in arr:
            democrat_counter[word] += 1

sum = republican_counter + democrat_counter
for word in sum.most_common(1000):
    print("\"" + word[0] + "\"" + ",")