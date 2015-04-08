import tweepy

def auth():
	consumer_key = '6MI3KtDAXpdRGr6pAT5v0R1BD'
	consumer_secret = 'Jhm2u7IXSaMwJK1EwmalOWDKKrJPKXxZhn9cksltKPtZ25Gg2I'
	access_token = '51351450-FF7bmRblHoAxQyQ7ryrZQAcfSwTyrMV3bLQAJEWTW'
	access_secret = 'm8Kcz27xLhA8Vgc0VRbPI9uQ2YkT0hmTF4MpGVX80t32S'

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)

	api = tweepy.API(auth)