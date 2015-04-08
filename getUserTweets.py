import csv
import tweepy

def auth():
	consumer_key = '6MI3KtDAXpdRGr6pAT5v0R1BD'
	consumer_secret = 'Jhm2u7IXSaMwJK1EwmalOWDKKrJPKXxZhn9cksltKPtZ25Gg2I'
	access_token = '51351450-FF7bmRblHoAxQyQ7ryrZQAcfSwTyrMV3bLQAJEWTW'
	access_secret = 'm8Kcz27xLhA8Vgc0VRbPI9uQ2YkT0hmTF4MpGVX80t32S'

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)

	api = tweepy.API(auth)
	return api

def getUsersFromCSV(hashtag):
	with open('results-' + hashtag + '.csv', mode='r') as infile:
	    reader = csv.reader(infile)
	    with open('coors_new.csv', mode='w') as outfile:
	        writer = csv.writer(outfile)
	        mydict = dict((rows[0],rows[1]) for rows in reader)
	return mydict

def saveUsers(mydict, api):
	count = 0
	for key in mydict.keys():
		print(key)
		count+=1
		print(count)
		if count == 201:
			break
		for tweet in api.user_timeline(key):
			csvFile = open("user_" + str(key) + ".csv", 'a')
			csvWriter = csv.writer(csvFile)
			csvWriter.writerow([tweet.text.encode('utf-8')])
			csvFile.close()



