# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 11:54:07 2019

@author: de

Code Challenge
  Name: 
    Webscrapping ICC Cricket Page
  Filename: 
    icccricket.py
  Problem Statement:
    Write a Python code to Scrap data from ICC Ranking's 
    page and get the ranking table for ODI's (Men). 
    Create a DataFrame using pandas to store the information.
  Hint: 
    https://www.icc-cricket.com/rankings/mens/team-rankings/odi 
    
    
    #https://www.icc-cricket.com/rankings/mens/team-rankings/t20i
    #https://www.icc-cricket.com/rankings/mens/team-rankings/test
"""
from bs4 import BeautifulSoup   
import requests

source = requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi").text

soup = BeautifulSoup(source,"lxml")
print (soup.prettify())


right_table=soup.find('table', class_='table')

#Generate lists
A=[]
B=[]
C=[]
D=[]

for row in right_table.findAll('tr'):
    table_heads = row.findAll('th')
    cells = row.findAll('td')
    if len(cells) == 5:
        A.append(cells[1].text.strip())
        B.append(cells[2].text.strip())
        C.append(cells[3].text.strip())
        D.append(cells[4].text.strip())

from collections import OrderedDict

col_name = ["TEAM","Weighted Matches","Points","Ratings",]
col_data = OrderedDict(zip(col_name,[A,B,C,D]))

import pandas as pd
df = pd.DataFrame(col_data) 
df.to_csv("ODI's.csv")

