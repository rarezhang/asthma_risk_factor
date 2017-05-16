"""
get user profile based on user id 
input: python set: the output of twitter_unique_uid.py

"""


import pymongo, json
from utils import load_pickle

# unique user ids 
unique_user_ids = load_pickle('../data/twitter_asthma/unique_user_ids.pkl')
# python set, xx in set is O(1)

#########################################
# connect to mongodb

# this is the local host
client = pymongo.MongoClient('127.0.0.1', 27017)

# connect to database
db = client.asthma 

# connect to the collection
tweets = db.tweets

cur = db.tweets.find({}, {'user': 1})

outfile = '../data/twitter_asthma/user_profiles.json'
with open(outfile, mode='a',encoding='utf-8',errors='ignore') as outfile:
    for c in cur:
        user_id = c['user']['id_str']
        profile = c['user']
        
        if user_id in unique_user_ids: # O(1)
            print(profile)
            json.dump(profile, outfile)
            outfile.write('\n')
        


