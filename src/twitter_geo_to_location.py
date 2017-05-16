"""
convert geo to detailed address information
input: output of twitter_mongo_geo.py

too slow: use local photon server (10.128.195.35 server)
"""

from geopy.geocoders import Nominatim
import time

# global parameter
geolocator = Nominatim(timeout=5) # timeout second 


# reverse lat long order 
# geo list -> lat_lon str
# coordinate list -> lon_lat str
def lat_lon_order(lon_lat):
    """
    lon_lat to lat_lon
    """
    geo = lon_lat.split(',')
    lat_lon = ','.join((geo[1], geo[0]))
    return lat_lon

# geo to detailed address information 
def geo_to_address(lat_lon):
    """
    geo to address information
    """        
    location = geolocator.reverse(lat_lon)
    loc_dic = location.raw
    
    try: # nomally always have these information
        lat = loc_dic['lat']
        lon = loc_dic['lon']
        display_address = loc_dic['display_name']
        
        boundingbox = loc_dic['boundingbox']
        boundingbox = ','.join(map(str, boundingbox))
    except:
        time.sleep(5)
    
    try:
        city = loc_dic['address']['city']
    except:
        city = 'None'
    try:
        county = loc_dic['address']['county']
    except:
        county = 'None'   
    try:
        state = loc_dic['address']['state']
    except:
        state = 'None'
    try:
        country = loc_dic['address']['country']
    except:
        country = 'None'
    try:
        country_code = loc_dic['address']['country_code']
    except:
        country_code = 'None'
    try:
        postcode = loc_dic['address']['postcode']
    except:
        postcode = 'None'
    

    return '|'.join((lat, lon, display_address, city, county, state, country, country_code, postcode, boundingbox))
    
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


