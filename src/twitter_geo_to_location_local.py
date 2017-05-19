"""
convert geo to detailed address information
input: output of twitter_mongo_geo.py

use local ```photon``` server 
too slow 
"""

import urllib.request

# reverse lat long order 
# geo list -> lat_lon str
# coordinate list -> lon_lat str
def lat_lon_order(lon_lat):
    """
    lon_lat to lat_lon
    """
    coordinate = lon_lat.split(',')
    return coordinate

    
# geo to detailed address information 
def geo_to_address(coordinate):
    lon = coordinate[0]
    lat = coordinate[1]
    url = f'http://localhost:2322/reverse?lon={lon}&lat={lat}'
    address = urllib.request.urlopen(url).read()
    return address 
    
    
    
# -----------------------------------
# main 

# read input file

path_input = '../data/twitter_asthma/tweets_with_geo.txt'
# tweet_id | user_id | created_at | text | coordinates | location | time_zone

path_output = '../data/twitter_asthma/tweets_with_address.txt'
# tweet_id | lat | lon | display_address | city | county | state | country | country_code | postcode | boundingbox

with open(path_input, mode='r', encoding='utf-8', errors='ignore') as infile, open(path_output, mode='a', encoding='utf-8', errors='ignore') as outfile:
    for line in infile:
        line = line.split('|')
        tweet_id = line[0]
        user_id = line[1]
        lon_lat = line[4]  # coordinates        
        
        lat_lon = lat_lon_order(lon_lat) # geo
        
        # time.sleep(1)  # nominatim rate limit, 1 request per second
        add_info = geo_to_address(lat_lon)
        
        to_print = '|'.join((tweet_id, user_id, add_info)) + '\n'
        print(to_print)
        outfile.write(to_print)


