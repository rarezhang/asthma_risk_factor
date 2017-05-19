"""
get the unique user ids 
input: output of twitter_mongo_geo.py
output: dump python list: unique twitter user ids 
"""

from utils import dump_pickle, check_file_exist




###################################################
def extract_user_id(path_input, pos=1):
    with open(path_input, mode='r', encoding='utf-8', errors='ignore') as infile:
        for line in infile:
            line = line.split("|")
            user_id = line[pos]
            yield user_id

###################################################
'''
path_input = '../data/twitter_asthma/tweets_with_geo.txt'
# tweet_id | user_id | created_at | text | coordinates | location | time_zone

output = '../data/twitter_asthma/unique_user_ids.pkl'
if not check_file_exist(output):          
    user_ids = extract_user_id(path_input)

    # dump unique user ids 
    unique_user_ids = set(user_ids)
    # print(unique_user_ids)
    dump_pickle(output, unique_user_ids)
'''


path_input = '../data/twitter_asthma/tweets_with_address_usa.txt'
# user_id | geo | location 

output = '../data/twitter_asthma/unique_user_ids_usa.pkl'
if not check_file_exist(output):          
    user_ids = extract_user_id(path_input, pos=0)

    # dump unique user ids 
    unique_user_ids = set(user_ids)
    # print(unique_user_ids)
    dump_pickle(output, unique_user_ids)        