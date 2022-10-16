import tweepy #https://github.com/tweepy/tweepy
import json

consumer_key = 'consumer_key'
consumer_secret = 'consumer_secret'
access_token = "access_token"
access_token_secret = "access_token_secret"

au = tweepy.OAuthHandler(consumer_key, consumer_secret)
au.set_access_token(access_token, access_token_secret)
api = tweepy.API(au)

#Get the user's tweets from recent
#'count' can get the number of tweets you have
tweets = api.user_timeline(id="Twitter", count=10)

#Set the first tweet number
i=1

#Print tweets of the user by timeline
for tweet in tweets:
    print(str(i)+'. '+tweet.text+'\n')
    i=i+1