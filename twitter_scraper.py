import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s
import time


#consumer key, consumer secret, access token, access secret.
ckey="sLrasFYsx1XgG6cMlKVPov1Km"
csecret="LcUU4QhVHH5hEf0bb1THJq72yDIMSk1w2vSonshLQxTrWL0EsK"
atoken="2391812528-5QsFVFaqEnVWDaKHuBWwfV4pC8NXzofU8f4qBmY"
asecret="8zVXLAnwTldlCpRyCVyjpubgTK4zKx4e4adsLdO1IYHTC"

#from twitterapistuff import *

class listener(StreamListener):

    def on_data(self, data):

        all_data = json.loads(data)

        tweet = all_data["text"]
        sentiment_value, confidence = s.sentiment(tweet)
        #print(tweet, sentiment_value, confidence)

        if confidence*100 >= 80:
            output = open("twitter-out.txt","a")
            #output.write(sentiment_value)
            output.write(tweet)
            output.write('\n')
            output.close()

        return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

lookup = input("Look up tweets: ")

import time
timeout = time.time() + 60 * 0.25

print ("Getting tweets...one minute please...")

while time.time() < timeout:
    twitterStream = Stream(auth, listener())
    twitterStream.filter(track=[lookup])
    print (time.time())


print ("Got Tweets!")
