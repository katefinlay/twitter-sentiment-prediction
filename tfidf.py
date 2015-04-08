import csv
import os
from os import listdir
import operator

rootdir= os.path.expanduser("~/Development/twitter-app/feminism")
suffix=".csv"

filenames = listdir(rootdir)
LC = [ filename for filename in filenames if filename.endswith( suffix ) ]

dict = {}
for filename in LC:	
	with open(("feminism/"+filename), mode='r') as data:
		currList = list(csv.reader(data))
		for tweet in currList:
			#tweet is now ["example tweet"], turn it into a string and remove the [""]
			tweet = str(tweet)
			tweet = tweet[2:-2] 
			#get individual words
			splitTweet = tweet.split()
			for word in splitTweet:
				word = word.lower()
				value = 1
				if (word[0] == '#') and (word != "#feminism"):
					if word not in dict:
						dict[word] = []
					elif word in dict: #if w in d
						dict[word] += [value]

numTerms = len(dict)

for keys,values in dict.items():
	values = [sum(values)/len(dict)]
	print(keys)
	print(values)

print
print max(dict.iteritems(), key=operator.itemgetter(1))[0]
 (Number of times term t appears in a document) / (Total number of terms in the document).
#update the idf csv
with open('test.csv', 'rb') as f:
    reader = csv.reader(f) # pass the file to our csv reader
    for row in reader:     # iterate over the rows in the file
        new_row = row      # at first, just copy the row
        for key, value in changes.items(): # iterate over 'changes' dictionary
            new_row = [ x.replace(key, value) for x in new_row ] # make the substitutions
        new_rows.append(new_row) # add the modified rows

with open('test.csv', 'wb') as f:
    # Overwrite the old file with the modified rows
    writer = csv.writer(f)
    writer.writerows(new_rows)









