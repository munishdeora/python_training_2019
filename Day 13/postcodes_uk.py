# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 13:36:27 2019

@author: de

Code Challenge
  Name: 
    Post Codes UK
  Filename: 
    postcodes_uk.py
  Problem Statement:
    We write an expression, which is capable of recognizing the postal codes or postcodes of the UK.

    Postcode units consist of between five and seven characters, 
    which are separated into two parts by a space. 
    
    The two to four characters before the space represent the so-called outward 
    code or out code intended to direct mail from the sorting office to the delivery office. 
    
    The part following the space, which consists of a digit followed by two uppercase characters, 
    comprises the so-called inward code, which is needed to sort mail at the final delivery office. 
    
    The last two uppercase characters do not use the letters CIKMOV, 
    so as not to resemble digits or each other when hand-written.

    The outward code can have the form: One or two uppercase characters, 
    followed by either a digit or the letter R, 
    optionally followed by an uppercase character or a digit. 
    (We do not consider all the detailed rules for postcodes, 
    i.e only certain character sets are valid depending on the position 
    and the context.)    
  Hint: 
    Using Regular Expression 
  Input:
      example_codes = ["SW1A 0AA", # House of Commons
                 "SW1A 1AA", # Buckingham Palace
                 "SW1A 2AA", # Downing Street
                 "BX3 2BB", # Barclays Bank
                 "DH98 1BT", # British Telecom
                 "N1 9GU", # Guardian Newspaper
                 "E98 1TT", # The Times
                 "TIM E22", # a fake postcode
                 "A B1 A22", # not a valid postcode
                 "EC2N 2DB", # Deutsche Bank
                 "SE9 2UG", # University of Greenwhich
                 "N1 0UY", # Islington, London
                 "EC1V 8DS", # Clerkenwell, London
                 "WC1X 9DT", # WC1X 9DT
                 "B42 1LG", # Birmingham
                 "B28 9AD", # Birmingham
                 "W12 7RJ", # London, BBC News Centre
                 "BBC 007" # a fake postcode
                ]

"""

list1=["SW1A 0AA","SW1A 1AA","SW1A 2AA","BX3 2BB","DH98 1BT","N1 9GU","E98 1TT",
       "TIM E22","A B1 A22","EC2N 2DB","SE9 2UG","N1 0UY","EC1V 8DS","WC1X 9DT",
       "B42 1LG","B28 9AD","W12 7RJ","BBC 007"]
valid_list=[]
import re
for item in list1 :
    result= re.match(r'[A-Z]{1,2}(\d|R)([A-Z]|\d)?[ ]\d[ABDEFGHJLNPQRSTUWXYZ]{2}',item)
    if result != None :
        valid_list.append(item)
   
      