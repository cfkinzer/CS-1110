# Christian Kinzer (cfk5ax) and Adam Hershaft (agh3cn)
from urllib.request import urlopen
import math
import webbrowser


def distance_between(lat_1, lon_1, lat_2, lon_2):
    """Uses the "great circle distance" formula and the circumference of the earth
    to convert two GPS coordinates to the miles separating them"""
    lat_1, lon_1 = math.radians(lat_1), math.radians(lon_1)
    lat_2, lon_2 = math.radians(lat_2), math.radians(lon_2)
    theta = lon_1 - lon_2
    dist = math.sin(lat_1)*math.sin(lat_2) + math.cos(lat_1)*math.cos(lat_2)*math.cos(theta)
    dist = math.acos(dist)
    dist = math.degrees(dist)
    dist = dist * 69.06         # 69.09 = circumference of earth in miles / 360 degrees
    return dist


user_lat = float(input('Please input your latitude. '))
user_lon = float(input('Please input your longitude. '))
text = urlopen('http://cs1110.cs.virginia.edu/files/wendys.csv')
distances = []
minimum_distance = 5000
for line in text:
    line = line.decode('utf-8')
    line = str(line.strip())
    line = line.split(',')
    lat = float(line[1])
    lon = float(line[0])
    distance = distance_between(user_lat, user_lon, lat, lon)
    if distance < minimum_distance:
        minimum_distance = distance
        address = line[4]
        address = address.strip()
        city = line[5]
        city = city.strip()
        state = line[6]
        state = state.strip()
print("The nearest Wendy's is located at " + address + ', ' + city + ', ' + state)
url_end = address + ' ' + city + ' ' + state
url_end = url_end.replace(' ', '+')
url = 'http://maps.google.com/maps?q=' + url_end
url = url.replace("'", '')
webbrowser.open(url)
