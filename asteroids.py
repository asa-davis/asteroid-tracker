#!/usr/bin/python
import requests
import json
import datetime
import cgi
import cgitb

cgitb.enable()

print 'Content-type: text/html\n\n'

# Get the feed
today = datetime.datetime.now()
todayStr = today.strftime('%Y-%m-%d')
r = requests.get("https://api.nasa.gov/neo/rest/v1/feed?start_date=" + todayStr + "&end_date=" + todayStr + "&api_key=kAO2cD5WiytNuYEqqaP1si0fUFQ9teIagRaie5Dp")

# Convert it to a Python dictionary
data = json.loads(r.text)

# Parse data
date = data['near_earth_objects'].keys()
date = date[0]
asteroids = data['near_earth_objects'][date]
count = len(asteroids)

# Output
print('<div style="text-align: center">')
print('<h1 style="text-decoration: underline">%d asteroids will pass earth today on %s!</h1>' %(count, date))
for asteroid in asteroids:
        print('<h2>Name of Object: ' + asteroid['name'] + '</h2>')
        print('<div>min diameter: %.3f miles</div>' %(asteroid['estimated_diameter']['miles']['estimated_diameter_min']))
        print('<div>max diameter: %.3f miles</div>' %(asteroid['estimated_diameter']['miles']['estimated_diameter_max']))
        print('<div>relative velocity: %.1fk miles per hour</div>' %(float(asteroid['close_approach_data'][0]['relative_velocity']['miles_per_hour'])/1000))
        print('<div>miss distance: %.1fk miles</div>' %(float(asteroid['close_approach_data'][0]['miss_distance']['miles'])/1000))
        print('<a href="%s">orbit diagram</a>' %(asteroid['nasa_jpl_url']+';old=0;orb=1;cov=0;log=0;cad=0#orb'))
        print('<div></div>')
print('</div>')