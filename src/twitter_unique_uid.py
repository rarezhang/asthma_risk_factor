"""
get the unique user ids 
input: output of twitter_mongo_geo.py
output: dump python list: unique twitter user ids 
"""

from utils import dump_pickle, check_file_exist


path_input = '../data/twitter_asthma/tweets_with_geo.txt'
# tweet_id | user_id | created_at | text | coordinates | location | time_zone

def extract_user_id(path_input):
    with open(path_input, mode='r', encoding='utf-8', errors='ignore') as infile:
        for line in infile:
            line = line.split("|")
            user_id = line[1]
            yield user_id

output = '../data/twitter_asthma/unique_user_ids.pkl'
if not check_file_exist(output):          
    user_ids = extract_user_id(path_input)

    # dump unique user ids 
    unique_user_ids = set(user_ids)
    print(unique_user_ids)
    dump_pickle(output, unique_user_ids)
        