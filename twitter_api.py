import tweepy #https://github.com/tweepy/tweepy
import json

key = 'key'
secret = 'secret'
token = "token"
token_secret = "token_secret"

auth = tweepy.OAuthHandler(key, secret)
auth.set_access_token(token, token_secret)
api = tweepy.API(auth)

#Get the user's tweets from recent
#'count' can get the number of tweets you have
public_tweets = api.user_timeline(id="Twitter", count=10)

#Set the first tweet number
i=1

#Print tweets of the user by timeline
for tweet in public_tweets:
    print(str(i)+'. '+tweet.text+'\n')
    i=i+1