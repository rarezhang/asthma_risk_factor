"""
get lat_lon based on unique user ids 

goal: for later use: get address based on lat_lon

input: the out put of twitter_mongo_geo.py <'../data/twitter_asthma/tweets_with_geo.txt'>
"""

# create a set to check if already add the user_id 
added_user_ids = set()  # xx in set O(1)

#########################################
def coordinates_to_geo(coordinates):
    lon_lat = coordinates.split(',')
    geo = ','.join((lon_lat[1], lon_lat[0])) # lat_lon
    return geo 
#########################################

path_infile = '../data/twitter_asthma/tweets_with_geo.txt'
# tweet_id | user_id | created_at | text | coordinates | location | time_zone

path_outfile = '../data/twitter_asthma/unique_uid_geo.txt'

with open(path_infile, mode='r', encoding='utf-8', errors='ignore') as infile, open(path_outfile, mode='a',encoding='utf-8',errors='ignore') as outfile:
    for line in infile:
        line = line.split('|')
        user_id = line[1]
        coordinates = line[4]
        geo = coordinates_to_geo(coordinates) # lon_lat to lat_lon
        
        if user_id not in added_user_ids:
            added_user_ids.add(user_id)
            to_print = '|'.join((user_id, geo)) + '\n'
            outfile.write(to_print)
