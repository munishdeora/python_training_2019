# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 12:43:55 2019

@author: de
"""

"""
Code Challenge
  Name: 
    Currency Converter Convert  from USD to INR
  Filename: 
    currecncyconv.py
  Problem Statement:
    You need to fetch the current conversion prices from the JSON  
    using REST API
  Hint:
    http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=y
    Check with http://api.fixer.io/latest?base=USD&symbol=EUR
    
"""

import requests

url1 = "http://free.currencyconverterapi.com/api/v5/convert?q="
url2 = input("enter the from aur to currency requirement : ")
url3 = "&apiKey=2881c9abf6cade9ce504"


url = url1 + url2 + url3

response = requests.get(url)

response.text
# Since we know that the content type is json we can call the json() function to get the data converted to python data type (dict)
json_data = response.json() 

print("from {} price value : {} ".format((json_data['results'][url2]['id']),(json_data['results'][url2]['val'])))


USD_EUR
USD_INR
