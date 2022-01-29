from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys
import tweepy
import numpy as np
import pandas as pd
from googletrans import Translator
class Import_tweet_emotion:

	consumer_key = "SJLR0HtdoFOsTNzXwEYUqdGpG"
	consumer_secret = "itmjg8dFwuTdJZZ9P7oCmvjezbbd0mQ53hYpKqKOdwd42TjmAS"
	access_token = "1476449348099588098-4pLDVC9v4ERfVp3rklMSL0XwYKTfsi"
	access_token_secret = "pf4DtkuhURzJ55FOzgC6sv0TrQ5nhgfyrufB7inUowqWU"

	def tweet_to_data_frame(self, tweets):
		df = pd.DataFrame(data=[tweet.full_text for tweet in tweets], columns=['Tweets'])
		return df

	def get_tweets(self, handle):
		auth = OAuthHandler(self.consumer_key, self.consumer_secret)
		auth.set_access_token(self.access_token, self.access_token_secret)
		auth_api = API(auth)

		account = handle
		item = auth_api.user_timeline(id=account,count=30,tweet_mode="extended")
		df = self.tweet_to_data_frame(item)

		all_tweets = []
		for j in range(30):
			all_tweets.append(df.loc[j]['Tweets'])
		return all_tweets

	def get_hashtag(self, hashtag):
		auth = OAuthHandler(self.consumer_key, self.consumer_secret)
		auth.set_access_token(self.access_token, self.access_token_secret)
		auth_api = API(auth)

		account = hashtag
		all_tweets = []

		for tweet in tweepy.Cursor(auth_api.search, q=account, lang='en',tweet_mode="extended").items(30):
			if 'retweeted_status' in dir(tweet):
				all_tweets.append(tweet.retweeted_status.full_text)		
			else:	
				all_tweets.append(tweet.full_text)
		
		return all_tweets

