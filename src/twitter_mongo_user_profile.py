"""
get user profile based on user id 
input 1: python set: the output of twitter_unique_uid.py
input 2: twitter_mongo_geo.py
"""


# import pymongo, json
# from utils import load_pickle

# unique user ids 
unique_user_ids = load_pickle('../data/twitter_asthma/unique_user_ids.pkl')
# python set, xx in set is O(1)

# create a set to check if already add the user_id 
added_user_ids = set()

#####################################################
outfile = '../data/twitter_asthma/user_profiles.json'

with open(outfile, mode='a',encoding='utf-8',errors='ignore') as outfile:
    for c in cur:
        user_id = c['user']['id_str']
        profile = c['user']
        
        if user_id in unique_user_ids and user_id not in added_user_ids: # O(1)
            added_user_ids.add(user_id)
            print(user_id)
            json.dump(profile, outfile)
            outfile.write('\n')
        


