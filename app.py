# -*- coding: utf-8 -*-
import tweepy
import datetime
import credentials

keyword = "大黒屋 -RT"
dfile = "test.txt"

jsttime = datetime.timedelta(hours=9)
print(jsttime)



auth = tweepy.OAuthHandler(credentials.Consumer_key, credentials.Consumer_secret)
auth.set_access_token(credentials.Access_token, credentials.Access_secret)

api = tweepy.API(auth, wait_on_rate_limit = True)

q = keyword

tweets_data = []


for tweet in tweepy.Cursor(api.search, q=q,tweet_mode='extended',lang='ja').items(100):

	tweets_data.append(tweet.full_text + '\n')

fname = r"'" + dfile + "'"
fname = fname.replace("'", "")

with open(fname, "w", encoding="utf-8") as f:
	f.writelines(tweets_data)