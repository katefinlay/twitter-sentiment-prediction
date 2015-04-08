import csv
import tweepy
import oauth-twitter

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



