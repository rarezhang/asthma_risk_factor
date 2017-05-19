"""
convert geo to detailed address information
input: output of twitter_mongo_geo.py

too slow: use local photon server (10.128.195.35 server)
"""

from Geocoder import Geocode, ReverseGeocode
import time

    
# -----------------------------------
# main 

# read input file

path_input = '../data/twitter_asthma/unique_uid_geo.txt'
# user_id | coordinates 

path_output = '../data/twitter_asthma/tweets_with_address.txt'
# user_id | coordinates |address_info


rg = ReverseGeocode()

with open(path_input, mode='r', encoding='utf-8', errors='ignore') as infile, open(path_output, mode='a', encoding='utf-8', errors='ignore') as outfile:
    for line in infile:
        line = line.split('|')
        user_id = line[0]
        geo = line[1].strip().split(',')        
        
        print(geo)
        
        # nominatim rate limit, 1 request per second
        # time.sleep(1)
        while True:
            try:
                address_info = rg.reverse_geocode(geo)
                break
            except:
                time.sleep(1)
                continue
        
        to_print = '|'.join((user_id, str(geo), str(address_info))) + '\n'
        print(to_print)
        outfile.write(to_print)


