"""
get created_at information
input: tweets_with_address_usa.txt
"""
import pymongo
from utils import convert_twitter_timedate, load_pickle


# unique user ids in USA
unique_user_ids_usa = load_pickle('../data/twitter_asthma/unique_user_ids_usa.pkl') # python set

# connect to mongodb
client = pymongo.MongoClient('127.0.0.1', 27017)
# connect to database
db = client.asthma 
# connect to the collection
collection = db.profiles


cur = collection.find({},{'id_str':1,'created_at':1})

path_output = '../data/twitter_asthma/unique_uid_usa_created.txt'

with open(path_output, 'a', encoding='utf-8', errors='ignore') as outfile:
    for c in cur:
        user_id = c['id_str']
        if user_id in unique_user_ids_usa:
            created_at = c['created_at']
            created_at = str(convert_twitter_timedate(created_at))
            to_print = '|'.join((user_id, created_at)) + '\n'
            outfile.write(to_print)
        