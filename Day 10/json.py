# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 12:15:32 2019

@author: de
"""


"""
Code Challenge
  Name: 
    JSON Parser
  Filename: 
    json.py
  Problem Statement:
    Get me the other details about the city
        Latitude and Longitude
        Weather Condition
        Wind Speed
        Sunset Rise and Set timing
"""
import requests
url1 = "http://api.openweathermap.org/data/2.5/weather?q="
url2 = input("enter the city name : ")
url3 = "&appid=8573b478c87b6c6258bb3a4cefa99666"

url = url1 + url2 + url3

response = requests.get(url)

response.content

response.text

jsondata = response.json()

print("Latitude : {} and Longitude {}".format((jsondata['coord']['lon']),(jsondata['coord']['lat'])))

print("Weather Condition :",jsondata['weather'][0]['description'])

print("Wind Speed : ",jsondata['wind']['speed'])

import datetime
a1=jsondata['sys']['sunrise']
a2=jsondata['sys']['sunset']
sun_rise=datetime.datetime.fromtimestamp(a1).strftime('%c')
sun_set=datetime.datetime.fromtimestamp(a2).strftime('%c')

print("Sunset Rise : {} and Set timing : {}".format((sun_rise),(sun_set)))
