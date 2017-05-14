"""
utils
"""

import datetime, time
from dateutil import tz

def convert_twitter_timedate(twitterdate, fromtimezone='UTC', totimezone='UTC'):

    """
    convert twitter time date to local date time.
    twitterdate: twitter time-date type: e.g., 'Tue Mar 29 08:11:25 +0000 2011'
    fromtimezone: convert from which time zone, twitter using UTC, default UTC
    totimezone: convert to which time zone
    >>> convert_twitter_timedate('Tue Mar 29 08:11:25 +0000 2011', fromtimezone='UTC', totimezone='US/Central')
    2011-03-29 03:11:25-05:00
    """
    date = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(twitterdate, '%a %b %d %H:%M:%S +0000 %Y'))
    from_zone = tz.gettz(fromtimezone)
    to_zone = tz.gettz(totimezone)
    utc = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    utc = utc.replace(tzinfo=from_zone)
    # Convert time zone
    return utc.astimezone(to_zone)

'''
    
import os, pickle, fileinput, nltk, errno, time, pytz
from functools import reduce
from datetime import datetime
from winsound import Beep    
    
######################################################
# decorator functions
######################################################
def time_it(f):
    """
    decorator function
    :param f: function needs time recording
    :return: higher order function -> f = timeit(f)
    """
    def timed(*args, **kw):
        begin_time = time.time()
        fun = f(*args, **kw)
        end_time = time.time()
        print(f, 'time used: ', end_time - begin_time)
        return fun
    return timed


def load_or_make2(f):
    """
    decorator function
    set store path when declare the actual fun
    :param f:
    :return:
    """
    def wrap_fun(*args, **kwargs):
        pickle_path = kwargs['path'] + '.pkl'
        if check_file_exist(pickle_path):
            data = load_pickle(pickle_path)
        else:
            data = f(*args, **kwargs)
            dump_pickle(pickle_path, data)
        return data
    return wrap_fun


def load_or_make(path):
    """
    set store path when declare the decorator fun
    :param path:
    :return:
    """
    assert path is not None, 'set path'

    def decorator_fun(f):  # todo, add file path here
        """
        decorator function
        :param f:
        :return:
        """
        def wrap_fun(*args, **kwargs):
            if check_file_exist(path):
                print('loading fun:{} result from: {}'.format(f.__name__, path))
                data = load_pickle(path)
            else:
                print('fun:{} running... '.format(f.__name__))
                data = f(*args, **kwargs)
                dump_pickle(path, data)
            return data
        return wrap_fun
    return decorator_fun


######################################################
# time
######################################################
def time_now(timezone='US/Mountain'):
    """
    Get the current time, in a specific timezone:
    :param timezone:
    :return:
    """
    """
    Get list of timezones
    for tz in pytz.all_timezones:
        print tz
    """
    return datetime.now(pytz.timezone(timezone)).strftime('%Y-%m-%d %H:%M:%S')

######################################################
# files and paths
######################################################


def dump_pickle(path, data):
    """
    save data as binary file
    :param path:
    :param data:
    :return:
    """
    with open(path, 'wb') as f:
        pickle.dump(data, f, protocol=3)  # protocol 3 is compatible with protocol 2, pickle_load can load protocol 2


def load_pickle(path):
    """
    :param path:
    :return:
    """
    with open(path, 'rb') as f:
        data = pickle.load(f)
    return data


def check_file_exist(path):
    """
    check if ``file`` exists
    :param path:
    :return: T/F
    """
    return os.path.isfile(path)


def check_make_dir(path):
    """
    python 3.2+
    try to make a directory if the directory not exist
    :param path:
    :return:
    """
    # exist_ok=True, avoid raising an exception if the directory already exists
    if not os.path.isdir(path):
        print('dir_path is not valid, creating a new dir now: {}'.format(path))
    os.makedirs(path, exist_ok=True)

def files_remove(path):
    """

    :param path:
    :return:
    """
    assert os.path.isdir(path), 'remove all files in a directory'
    files = [os.path.join(path, f) for f in os.listdir(path)]
    if len(files) != 0:
        for f in files: os.remove(f)



def file_remove(path):
    """
    remove file if file exists, return error except no such file
    :param path:
    :return:
    """
    try:
        os.remove(path)
    except OSError as e:  # this would be "except OSError, e:" before Python 2.6
        if e.errno != errno.ENOENT:  # errno.ENOENT = no such file or directory
            raise  # re-raise exception if a different error occurred


def join_file_path(dir_path, file_name):
    """
    Join path components
    :return:
    """
    # assert os.path.isdir(dir_path), 'first argument should be a dir path'
    check_make_dir(dir_path)
    return os.path.join(dir_path, file_name)


def concatenate_directory_files(input_directory, output_file):
    """
    :param input_directory:
    :param output_file:
    :return:
    """
    assert os.path.isdir(input_directory), 'input path should be a directory'

    if not input_directory.endswith('/'):  # todo: os join path
        input_directory = ''.join((input_directory, '/'))

    if not check_file_exist(output_file):
        file_names = os.listdir(input_directory)
        file_paths = [''.join((input_directory, f_n)) for f_n in file_names]
        with open(output_file, 'w', encoding='utf-8') as out_file:
            in_file = fileinput.input(files=file_paths, openhook=fileinput.hook_encoded(
                'utf-8'))  # python 2.7.10, fileinput doest not have `__exit__` --> cannot use `with`
            for line in in_file:
                out_file.write(line)
            in_file.close()


def concatenate_files(*args, path_out):
    """

    :param args:
    :return:
    """
    if not check_file_exist(path_out):
        with open(path_out, 'w', encoding='utf-8', errors='ignore') as outfile:
            for fname in args:
                assert os.path.isfile(fname)
                with open(fname, 'r', encoding='utf-8', errors='ignore') as infile:
                    for line in infile:
                        outfile.write(line)
######################################################
# string
######################################################

def strip_non_ascii(string, starting_ord=32, ending_ord=126):
    """
    Returns the string without non ASCII characters
    :param string:
    :param starting_ord:
    :param ending_ord:
    :return:
    """
    return "".join([c for c in string if starting_ord <= ord(c) <= ending_ord])


@load_or_make
def remove_stop_words(text, path=" "):
    """

    :param tweets:
    :return:
    """
    stop_words = set(nltk.corpus.stopwords.words("english"))
    return [" ".join([word for word in line.split() if word not in stop_words]) for line in text]


def pos_tag(tweet):
    """

    :param words:
    :return:
    """
    pos_t = nltk.pos_tag(strip_non_ascii(tweet).split())  # nltk can only process ascii char
    return pos_t


######################################################
# helper functions
######################################################
def nested_fun(funs, value):
    """
    f1(f2(value))
    :param funs: list of functions (iterable)
    :param value:
    :return: f1(f2(value))
    """
    return reduce(lambda res, f: f(res), funs, value)


######################################################
# push and pop variable
######################################################
path_temp = 'lib/tmp.txt'
def push_var(value):
    """

    :param path:
    :param var:
    :return:
    """
    # file_remove(path_temp)
    dump_pickle(path_temp, value)


def pop_var():
    """

    :return:
    """
    value = load_pickle(path_temp)
    # file_remove(path_temp)
    return value

######################################################
# sound
######################################################
def alarm_when_finish():
    Beep(300, 2000)  # Sound alarm when code finishes
    
    
'''