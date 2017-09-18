import requests
from .config import get_gmaps_api_key


def geocode(city, state_prov, country):
    target = 'https://maps.googleapis.com/maps/api/geocode/json?address={} {} {}&key={}'.format(city, state_prov, country, get_gmaps_api_key())
    print(target)
    r = requests.get(target)
    r.raise_for_status()
    print(r.json()['results'])
    data = r.json()['results'][0]['geometry']['location']
    print(data)
    lng = data['lng']
    lat = data['lat']
    return lng, lat
