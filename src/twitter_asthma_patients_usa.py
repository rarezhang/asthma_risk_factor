"""
asthma patients in the USA 
(mentioned `asthma` or `inhaler` in one of the tweets)
created twitter account at 2013
who has geo information 
"""
import re
from utils import check_file_exist, dump_pickle, load_pickle


##############################################################
# unique user ids in the USA, created account at 2013
path_uid_usa_2013 = '../data/twitter_asthma/unique_uid_usa_created_2013.txt'
# user_id | created_at 

path_unique_user_ids_usa_2013 = '../data/twitter_asthma/unique_user_ids_usa_2013.pkl'

if not check_file_exist(path_unique_user_ids_usa_2013):
    unique_user_ids_usa_2013 = set()
    with open(path_uid_usa_2013, 'r') as f:
        for line in f:
            line = line.split('|')
            user_id = line[0]
            unique_user_ids_usa_2013.add(user_id)
    dump_pickle(path_unique_user_ids_usa_2013, unique_user_ids_usa_2013)
else:
    unique_user_ids_usa_2013 = load_pickle(path_unique_user_ids_usa_2013)

##############################################################

asthma = '.*asthma.*|.*inhaler.*'
asthma_pat = re.compile(asthma, flags=re.IGNORECASE)

path_tweets_with_geo = '../data/twitter_asthma/tweets_with_geo.txt'
 # tweet_id | user_id | created_at | text | coordinates | location | time_zone
path_asthma_patients = '../data/twitter_asthma/asthma_uid_usa_2013.txt'

with open(path_tweets_with_geo, 'r', encoding='utf-8', errors='ignore') as infile, open(path_asthma_patients, 'a', encoding='utf-8', errors='ignore') as outfile:
    for line in infile:
        line = line.split("|")
        user_id = line[1]
        if user_id in unique_user_ids_usa_2013:
            text = line[3]
            if re.match(asthma_pat, text):
                to_print = "|".join((user_id,text)) + '\n'
                print(to_print)
                outfile.write(to_print)
