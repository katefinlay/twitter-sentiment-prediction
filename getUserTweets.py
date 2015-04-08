import csv
import tweepy
consumer_key = '6MI3KtDAXpdRGr6pAT5v0R1BD'
consumer_secret = 'Jhm2u7IXSaMwJK1EwmalOWDKKrJPKXxZhn9cksltKPtZ25Gg2I'
access_token = '51351450-FF7bmRblHoAxQyQ7ryrZQAcfSwTyrMV3bLQAJEWTW'
access_secret = 'm8Kcz27xLhA8Vgc0VRbPI9uQ2YkT0hmTF4MpGVX80t32S'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

with open('results-feminism.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('coors_new.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        mydict = dict((rows[0],rows[1]) for rows in reader)



for key in mydict.keys():
	print(key)
	print("a")
	for tweet in api.user_timeline(key):
		csvFile = open("user_" + str(key) + ".csv", 'a')
		csvWriter = csv.writer(csvFile)
		csvWriter.writerow([tweet.text.encode('utf-8')])
		csvFile.close()

# TF(t) = (Number of times term t appears in a document) / (Total number of terms in the document).

# IDF: Inverse Document Frequency, which measures how important a term is. While computing TF, all terms are considered equally important. However it is known that certain terms, such as "is", "of", and "that", may appear a lot of times but have little importance. Thus we need to weigh down the frequent terms while scale up the rare ones, by computing the following: 

# IDF(t) = log_e(Total number of documents / Number of documents with term t in it).
