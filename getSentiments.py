''' Gathers the sentiments from the sentiments dictionary
    And finds the sentiment of a Twitter string
    @author Alan Ponte
'''
from __future__ import print_function
from calculateSentiments import SentinmentCalculator
import sys
from pprint import pprint
import tweepy
import csv

query = '#ukraine'

def getTweets():
    """Gets tweets using the REST API and returns a dictionary with the keys
    the usernames and the values the tweets"""
    # assuming twitter_authentication.py contains each of the 4 oauth elements (1 per line)
    #setting up the keys
    consumer_key = '6MI3KtDAXpdRGr6pAT5v0R1BD'
    consumer_secret = 'Jhm2u7IXSaMwJK1EwmalOWDKKrJPKXxZhn9cksltKPtZ25Gg2I'
    access_token = '51351450-FF7bmRblHoAxQyQ7ryrZQAcfSwTyrMV3bLQAJEWTW'
    access_secret = 'm8Kcz27xLhA8Vgc0VRbPI9uQ2YkT0hmTF4MpGVX80t32S'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth)

    # Open/Create a file to append data
    csvFile = open('results-ukraine.csv', 'a')
    #Use csv Writer
    csvWriter = csv.writer(csvFile)

    
    max_tweets = 1000
    tweetDict = {}

    for tweet in tweepy.Cursor(api.search, q=query).items(max_tweets):
        #Write a row to the csv file/ I use encode utf-8
        csvWriter.writerow([tweet.user.screen_name, tweet.text.encode('utf-8')])
        tweetDict[tweet.user.screen_name] = [tweet.text.encode('utf-8')]
    csvFile.close()
    return tweetDict

def open_sentiments_file(file):
    """ Opens the sentiments FILE. """
    sentiments_dict = {}
    with open(file) as data_file:
        pass
        
def load_sentiments(file_name = "sentiments.csv"):
    """Read the sentiment file and return a dictionary containing the sentiment
    score of each word, a value from -1 to +1.
    """
    sentiments = {}
    for line in open("sentiments.csv"):
        word, score = line.split(',')
        sentiments[word] = float(score.strip())
    return sentiments

def get_sentiments():
    """ Finds and returns the Sentiments of Twitter strings."""
    tweets=[]
    #makes a list of tweets
    myDict = getTweets()
    for key in myDict.keys(): 
        currTweet = myDict[key]
        tweets.append(currTweet)
    sentiments = load_sentiments()
    se = SentinmentCalculator(tweets, sentiments) 
    return se.analyze_tweet_sentiments()

def create_sentiment_report():    
    """ Creates a sentiment report."""
    sentiments = get_sentiments()
    print("Based on the query, {q} has a sentiment value of {sents}".format(q = query, sents = sentiments))

def main():
    sentiments = load_sentiments()
    pprint(sentiments['higher'])
    create_sentiment_report()

if __name__ == "__main__":
    main()
    
        
