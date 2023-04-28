import tweepy
import configparser
from textblob import TextBlob


class TopicObject:
    def __init__(self, all_tweets):
        self.topicTweets = all_tweets
        self.total_subjectivity = 0
        self.total_polarity = 0
        self.num_tweets = len(all_tweets)

    def getPolarity(self, topicTweets):
        numTweets = self.num_tweets
        total_polarity_weighted = 0
        for tweet in topicTweets:
            if tweet.polarity == 0.0:
                numTweets -= 1
            else:
                polarity_weight = tweet.tweet.sentiment.polarity * \
                    tweet.tweet.sentiment.subjectivity
                total_polarity_weighted += polarity_weight
        polarity = total_polarity_weighted / numTweets
        return polarity

    def listPolarity(self, topicTweets):
        list = []
        for tweet in topicTweets:
            list.append(tweet.polarity)
        return (list)

    def listSubjectivity(self, topicTweets):
        list = []
        for tweet in topicTweets:
            list.append(tweet.subjectivity)
        return (list)

    def getSubjectivity(self, topicTweets):
        numTweets = self.num_tweets
        total_subjectivity_weighted = 0
        for tweet in topicTweets:
            if tweet.subjectivity == 0.0:
                numTweets -= 1
            else:
                subjectivity_weight = (tweet.tweet.sentiment.subjectivity)
                total_subjectivity_weighted += subjectivity_weight
        subjectivity = total_subjectivity_weighted / numTweets
        return subjectivity

    def getScore(self, polarityScore, subjectivity):
        polarityScore = (polarityScore+1)/2
        score = (subjectivity * polarityScore)
        return score


class TweetObject:
    def __init__(self, tweet):
        self.tweet = TextBlob(tweet)
        self.polarity = self.tweet.polarity
        self.subjectivity = self.tweet.subjectivity


# reads file containing all the keys. Safer way to get keys without hardcoding items
config = configparser.ConfigParser()
config.read('config.ini')

# gets key values and stores them into variables
api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
