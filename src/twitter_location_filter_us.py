"""
filter out twitter users just from the US

input: D:\Projects\asthma\data\twitter_asthma\tweets_with_address.txt
the result of twitter_geo_to_location.py 
"""

import re

us_loc = '.+United States$|.+United States of America$|.+USA'
us_loc_pat = re.compile(us_loc)

input_path = '../data/twitter_asthma/tweets_with_address.txt'
output_path = '../data/twitter_asthma/tweets_with_address_usa.txt'

with open(input_path, mode='r', encoding='utf-8', errors='ignore') as infile, open(output_path, mode='a', encoding='utf-8', errors='ignore') as outfile:
    for sline in infile:
        line = sline.split('|')
        user_id = line[0]
        geo = eval(line[1])
        location = eval(line[2])[0] # address 
        
        if (location is not None) and us_loc_pat.match(location):
            outfile.write(sline)
