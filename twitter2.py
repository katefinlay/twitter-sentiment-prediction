from __future__ import absolute_import, print_function

import tweepy

# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key="6MI3KtDAXpdRGr6pAT5v0R1BD"
consumer_secret="Jhm2u7IXSaMwJK1EwmalOWDKKrJPKXxZhn9cksltKPtZ25Gg2I"

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_token="51351450-FF7bmRblHoAxQyQ7ryrZQAcfSwTyrMV3bLQAJEWTW"
access_token_secret="m8Kcz27xLhA8Vgc0VRbPI9uQ2YkT0hmTF4MpGVX80t32S"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# If the authentication was successful, you should
# see the name of the account print out
print(api.me().name)

results = api.search("#feminism",'en')

# i = 0

# while (results[i:i+2] != "})]")
# 	if results[i:i+18] == "u'screen_name': u'"
# 	i++

print(results)