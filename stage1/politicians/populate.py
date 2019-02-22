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

politicians = {
    "senators": [],
    "representatives": []
}

democrats = tweepy.Cursor(api.list_members, 'ENM185', 'senate-democrats').items()

for user in democrats:
    senator = {
        "twitter-handle": user.screen_name,
        "party": "Democrat"
    }
    politicians["senators"].append(senator)

republicans = tweepy.Cursor(api.list_members, 'ENM185', 'senate-republicans').items()

for user in republicans:
    senator = {
        "twitter-handle": user.screen_name,
        "party": "Republican"
    }
    politicians["senators"].append(senator)

politicians_json = json.dumps(politicians, indent=4)

f = open(os.path.dirname(__file__) + "/politicians.json", "w")
f.write(politicians_json)
