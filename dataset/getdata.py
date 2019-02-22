import tweepy
import json
import os.path

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

with open(os.path.dirname(__file__)+"/../common_words/words.json") as common_words_file:
    common_words = json.load(common_words_file)

data = {
    "Republicans": [],
    "Democrats": []
}

for politician in politicians["senators"]:
    print(politician["twitter-handle"]) #for logging
    tweets = api.user_timeline(id=politician["twitter-handle"], count=100)
    for tweet in tweets:
        arr = []
        for common_word in common_words:
            if common_word in tweet.text.lower().split():
                arr.append(1)
            else:
                arr.append(0)
        if sum(arr) >= 5:
            if politician["party"] == "Republican":
                data["Republicans"].append(arr)
            else:
                data["Democrats"].append(arr)
    
data_json = json.dumps(data)

f = open(os.path.dirname(__file__) + "/data.json", "w")
f.write(data_json)