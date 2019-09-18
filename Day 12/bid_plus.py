# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 12:41:49 2019

@author: de
"""

"""
Code Challenge:
  Name: 
    Bid Plus
  Filename: 
    bid_plus.py
  Problem Statement:
      USE SELENIUM
      Write a Python code to Scrap data and download data from given url.
      url = "https://bidplus.gem.gov.in/bidlists"
      Make list and append given data:
          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)
          
          # Optional - Do not do this
          7. Name of the PDF file
          
     Make a csv file add all data in it.
      csv Name: bid_plus.csv
"""
from  selenium import webdriver
from time import sleep

url = "https://bidplus.gem.gov.in/bidlists"

browser = webdriver.Chrome("C:/Users/de/Downloads/chromedriver.exe")

browser.get(url)

data=browser.find_element_by_xpath('//div[@id="pagi_content"]')    
bid_no=[]
for row in data.find_elements_by_class_name('block_header'):
    bd_data = row.find_elements_by_tag_name('p')
    if len(bd_data)==2:
        bid_no.append(bd_data[0].text.strip())

items=[]  

quantity_required=[]
dept_name_add=[]
start_date=[]
end_date=[]
   
while(True):
    bid_no=[]
    for row in data.find_elements_by_class_name('block_header'):
        bd_data = row.find_elements_by_tag_name('p')
        if len(bd_data)==2:
            bid_no.append(bd_data[0].text.strip())
        
    i= 0
    for row in data.find_elements_by_class_name('col-block'):
        
        if i%3==0:
            cd_data1 = row.find_elements_by_tag_name('p')
            if len(bd_data)==2:
                items.append(cd_data1[0].text.strip())
                quantity_required.append(cd_data1[1].text.strip())
        
        if i%3==1:
            cd_data = row.find_elements_by_tag_name('p')
            if len(bd_data)==2:
                dept_name_add.append(cd_data[1].text.strip())        
    
        if i%3==2:
            cd_data1 = row.find_elements_by_tag_name('span') 
            if len(bd_data)==2:
                start_date.append(cd_data1[0].text.strip())
                end_date.append(cd_data1[1].text.strip())
        
        i=i+1 
    data=browser.find_element_by_xpath('//*[@id="pagination"]/ul/li/ul/li[5]/a').click()
    sleep(2)
    
browser.quit()
        
from collections import OrderedDict

col_name = ["items","quantity","dept_name_add","start_date","end_date"]
col_data = OrderedDict(zip(col_name,[items,quantity_required,dept_name_add,start_date,end_date]))

import pandas as pd
df = pd.DataFrame(col_data) 
df.to_csv("bid's.csv")

        
        
