# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 11:07:03 2019

@author: de
"""


import requests

url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q=Jaipur"
url3 = "&appid=8573b478c87b6c6258bb3a4cefa99666"

url = url1 + url2 + url3

response = requests.get(url)

response.content
print (type(response.content))

response.text #coverting data form bytes to text

print ("Status code: " + str(response.status_code))
print ("Headers : " + str(response.headers))
print ("Data : " + response.text)


# Since we know that the content type is json we can call the json() function to get the data converted to python data type (dict)
jsondata = response.json()
