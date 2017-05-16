"""
asthma project

extract all tweets with geo information from MongoDB
"""


import pymongo, re
from utils import *



# connect to mongodb

# this is the local host
client = pymongo.MongoClient('127.0.0.1', 27017)


# connect to database
db = client.asthma 



# connect to the collection
tweets = db.tweets

########################################################################
# count how many tweets have geo information
"""
count = db.tweets.find({'coordinates':{'$ne':None}}).count()
print('tweets have geo information:', count)
"""

########################################################################
"""
# count how many tweets have location information
count = db.tweets.find({'user.location':{'$ne':None}}).count()
print 'tweets have location information:', count
"""

########################################################################
# get data with coordinates
## tweet_id | user_id | created_at | text | coordinates | location | time_zone


cur = db.tweets.find({'coordinates':{'$ne':None}},{'id_str':1,'created_at':1,'text':1,'coordinates':1,'user.time_zone':1, 'user.id_str':1, 'user.location': 1})

path = '../data/twitter_asthma/tweets_with_geo.txt'
print(path)

with open(file=path, mode='a',encoding='utf-8',errors='ignore') as f:
    for c in cur:
        # c: a single tweet. type:dictionary
        tweet_id = c['id_str']
        
        user_id = c['user']['id_str']
        
        created_at = c['created_at']  #keep all timeme information
        created_at = str(convert_twitter_timedate(created_at))
        
        text = c['text'].replace('|',' ') #text: remove '|' in text -> because use'|'as split
        text = text.replace('\r',' ').replace('\n',' ') #combine multiple lines
        
        coordinates = c['coordinates']['coordinates']
        coordinates = ','.join(map(str, coordinates))
        
        try:
            location = c['user']['location'] 
            location = re.sub('[\W_]+', ' ', location) # remove everything except alphanumeric
            location = re.sub( '\s+', ' ', location).strip() # substitute multiple white space with 1
            if location == ' ' or '':
                location = 'None'
        except:
            location = 'None'

        
        try:
            time_zone = c['user']['time_zone']
            time_zone = re.sub('[\W_]+',' ', time_zone) # remove everything except alphanumeric
            if time_zone == ' ' or '':
                time_zone = 'None'
        except:
            time_zone = 'None'

        to_print = '|'.join((tweet_id, user_id, created_at, text, coordinates, location, time_zone, '\n'))
        print(to_print)
        f.write(to_print)
        

