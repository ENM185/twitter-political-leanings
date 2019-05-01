import tweepy
import json
import os.path
import csv
import re

with open(os.path.dirname(__file__) + "/../twitter_keys.json") as keys_file:
    keys = json.load(keys_file)

consumer_key = keys["consumer_key"]
consumer_secret = keys["consumer_secret"]
access_token = keys["access_token"]
access_token_secret = keys["access_token_secret"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

with open(os.path.dirname(__file__)+"/../politicians/politicians.json") as politicians_file:
    politicians = json.load(politicians_file)

with open(os.path.dirname(__file__)+"/../political_words/words.json") as common_words_file:
    political_words = json.load(common_words_file)

def clean(text) :
    text = text.lower()
    text = re.sub(r"[^A-Za-z0-9^!./'=\s]", "", text)
    return text

def count(s) :
    c = 0
    for word in s.split():
        if word in political_words:
            c += 1
    return c

with open(os.path.dirname(__file__) + "/data.csv", "w") as dataFile:
    dataWriter = csv.writer(dataFile)

    for politician in politicians["senators"]:
        print(politician["twitter-handle"]) #for logging
        tweets = api.user_timeline(id=politician["twitter-handle"], count=100)
        for tweet in tweets:
            text = clean(tweet.text)
            if count(text) >= 1:
                arr = [text, politician["party"]]
                dataWriter.writerow(arr)