import os
import pathlib
import requests
from .config import get_tba_api_key
from .gmaps import geocode

TBA_API_BASE_URL = 'https://www.thebluealliance.com/api/v3'


class TbaTeamPageIterator:
    """
    TBA serves up their team list in pages of JSON, so this class iterates through their pagelist.
    """

    def __init__(self, start=0):
        self.page_count = start

    def __iter__(self):
        return self

    def __next__(self):
        r = requests.get(TBA_API_BASE_URL + '/teams/' + str(self.page_count), headers={'X-TBA-Auth-Key': get_tba_api_key()})
        r.raise_for_status()
        r = r.json()
        if r:
            self.page_count += 1
            return r
        else:
            raise StopIteration


def pages(start=0):
    return iter(TbaTeamPageIterator(start))


class Team(object):
    def __init__(self, json):
        # Basic team data
        self.team_number = json['team_number']
        self.team_name = json['nickname']

        # Location information
        if json['lng'] is not None and json['lat'] is not None:
            self.longitude, self.latitude = json['lng'], json['lat']
        else:
            self.longitude, self.latitude = geocode(json['city'], json['state_prov'], json['country'])


def print_pages():
    for page in pages():
        t = Team(page[0])
        print(t.team_name)
        print(t.team_number)
        print(t.longitude)
        print(t.latitude)
