from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="NCFqs1DXZmcsSmsA8T85QJGz3"
consumer_secret="8EsVXdr0su5saDwhXDmPcE6O2SQ2rCoLJrRkNnguSPJL6ZOFFK"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="1003883313516253185-aVbhF9fc8BCSHFAnFmXEEcsgedlHE2"
access_token_secret="UI1Efffq0QUnDF1Qb9tyvNnuhpUi7D8BUj7AsZCaUlTzN"

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """
    def on_data(self, data):
        try:
            print(data)
            savefile=open("d:\\twitter.txt","a")
            savefile.write(data)
            savefile.write("\n")
            savefile.close()
            return true

        
        except BaseException,e:
            print ("failed on data"),str(e)
            
            
        
        

    def on_error(self, status):
        print(status)

if __name__=="__main__":
    l=StdOutListener()
    auth=OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    stream=Stream(auth,l)
    stream.filter(track=["bbc"])
