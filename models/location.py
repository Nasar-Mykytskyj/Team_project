import socket
import os
import IP2Location
import json
import urllib.request
class Location():
    def __init__(self):
        current_location=None
    def get_current_location(self):
        import json
        import urllib.request
        resource = urllib.request.urlopen('https://api.ipregistry.co/?key=c9qw7jv0pu8kv9')
        payload = resource.read().decode('utf-8')
        country = json.loads(payload)['location']['country']['name']
        region = json.loads(payload)['location']['region']['name']
        city = json.loads(payload)['location']['city']
        latitude = json.loads(payload)['location']['latitude']
        longitude = json.loads(payload)['location']['longitude']
        return latitude,longitude,"country:{0} region:{1} city:{2}".format(country,region,city)


location=Location()