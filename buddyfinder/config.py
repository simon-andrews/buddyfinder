import errno
import os
import pathlib

tba_api_key_path = os.path.join(str(pathlib.Path.home()), '.buddyfinder_tba_apikey')
gmaps_api_key_path = os.path.join(str(pathlib.Path.home()), '.buddyfinder_gmaps_apikey')
tba_api_key = None
gmaps_api_key = None


def refresh_api_keys():
    # TODO: make this not repeat code
    try:
        with open(tba_api_key_path, 'r') as config_file:
            global tba_api_key
            tba_api_key = config_file.read().strip()
        with open(gmaps_api_key_path, 'r') as config_file:
            global gmaps_api_key
            gmaps_api_key = config_file.read().strip()
    except IOError as error:
        if error.errno == errno.ENOENT:  # If the IO error is that the file wasn't found...
            if not os.path.exists(tba_api_key_path):
                with open(tba_api_key_path, 'w') as config_file:
                    api_key = input("Please enter your TBA API key: ")
                    config_file.write(api_key)
            if not os.path.exists(gmaps_api_key_path):
                with open(gmaps_api_key_path, 'w') as config_file:
                    api_key = input("Please enter your GMaps API key: ")
                    config_file.write(api_key)
            refresh_api_keys()
        else:
            raise error


def get_tba_api_key():
    if tba_api_key is None:
        refresh_api_keys()
    return tba_api_key


def get_gmaps_api_key():
    if gmaps_api_key is None:
        refresh_api_keys()
    return gmaps_api_key