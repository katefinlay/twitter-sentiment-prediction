import tweepy
import csv
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
csvFile = open('results-feminism.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

query = '#feminism'
max_tweets = 1000
tweetDict = {}

for tweet in tweepy.Cursor(api.search, q=query).items(max_tweets):
    #Write a row to the csv file/ I use encode utf-8
    csvWriter.writerow([tweet.user.screen_name, tweet.text.encode('utf-8')])
    tweetDict[tweet.user.screen_name] = [tweet.text.encode('utf-8')]
csvFile.close()
print tweetDict
