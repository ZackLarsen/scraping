
# coding: utf-8

# # Twitter scraping

# ## https://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/

# In[1]:


from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
get_ipython().magic("config InlineBackend.figure_format = 'retina'")


# In[20]:


import os
import time
import json
from pandas.io.json import json_normalize

import tweepy
from tweepy import OAuthHandler
from twython import Twython


import numpy as np
np.set_printoptions(precision=2, linewidth=120, suppress=True, edgeitems=4)

import pandas as pd
pd.set_option('display.max_columns', 350)
#pd.set_option('precision', 5)


# In[9]:


os.getcwd()
get_ipython().system('ls')
#os.chdir('/Users/zacklarsen/Desktop/CSC 595 DataViz')


# In[11]:


# Define keys for the tweepy44! app

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)


# In[12]:


# Read in home timeline tweets
for status in tweepy.Cursor(api.home_timeline).items(100):
    # Process a single status
    print(status.text)


# In[17]:


tweets = []

def process_or_store(tweet):
    #print(json.dumps(tweet))
    tweets.append(tweet)
    
    

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    process_or_store(status._json)


# In[18]:


tweets


# In[21]:


tweetsDF = json_normalize(tweets)


# In[22]:


tweetsDF


# In[16]:


with open('mytweets.json', 'r') as f:
    line = f.readline() # read only the first tweet/line
    tweet = json.loads(line) # load it as Python dict
    print(json.dumps(tweet, indent=4)) # pretty-print


# In[33]:


tweetsStream = []

# https://ljvmiranda921.github.io/notebook/2017/02/24/twitter-streaming-using-python/
    
from __future__ import absolute_import, print_function

# Import modules
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from sqlalchemy.exc import ProgrammingError

# Your credentials go here

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_status(self, status):
        tweetsStream.append(status.text)
        print(status.text)
        return True
       

    def on_error(self, status_code):
        if status_code == 420:
            return False
        

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['Chicago'])


# In[34]:


tweetsStream


# In[38]:


# https://ljvmiranda921.github.io/notebook/2017/02/24/twitter-streaming-using-python/
    
from __future__ import absolute_import, print_function

# Import modules
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from sqlalchemy.exc import ProgrammingError

# Your credentials go here
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''




# Set up sqlite3 database
import sqlite3
con = sqlite3.connect('tweetsStore.db')






class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_status(self, status):
        print(status.text)
        if status.retweeted:
            return

        id_str = status.id_str
        created = status.created_at
        text = status.text
        fav = status.favorite_count
        name = status.user.screen_name
        description = status.user.description
        loc = status.user.location
        user_created = status.user.created_at
        followers = status.user.followers_count

        table = db['tweetTable']

        try:
            table.insert(dict(
                id_str=id_str,
                created=created,
                text=text,
                fav_count=fav,
                user_name=name,
                user_description=description,
                user_location=loc,
                user_created=user_created,
                user_followers=followers,
            ))
        except ProgrammingError as err:
            print(err)
            
            
    def on_error(self, status_code):
        if status_code == 420:
            return False
        
        
        
        
        
        
        
        
if __name__ == '__main__':
    db = con
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['Chicago', 'Obama'])      


# In[ ]:


con.close()


# In[57]:


# From CSC 455

import urllib2
req = urllib2.Request("http://rasinsrv07.cstcis.cti.depaul.edu/CSC455/Assignment5.txt")
response = urllib2.urlopen(req)
#page = response.read()
lines = response.readlines()


# In[58]:


len(lines)


# In[59]:


lines[0]

