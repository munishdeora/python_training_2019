# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 14:48:52 2019

@author: de
"""

"""
Code Challenge
  Name: 
    Reading and Writing CSV
  Filename: 
    csv.py
  Problem Statement:
    Create a program that reads from one CSV file (/etc/passwd), 
    and writes to another one. 
    
    You are to read from data/passwd,
    and produce a file whose contents are the username (index 0) 
    and the user ID (index 2).
    Note that a record may contain a comment, 
    in which it will not have anything at index 2; 
    you should take that into consideration when writing the file.  
    The output file should use TAB characters to separate the elements.
 
    Thus, the input will look like:
    root:*:0:0::0:0:System Administrator:/var/root:/bin/sh
    daemon:*:1:1::0:0:System Services:/var/root:/usr/bin/false
    _ftp:*:98:-2::0:0:FTP Daemon:/var/empty:/usr/bin/false
    
    and the output will look like:
 
        root    0
        daemon  1
        _ftp    98
    
"""

list2=[]
list1=[]
usr_name=[]
usr_id=[]
dict1={}
#file opening for reading the contents of file
with open('passwd.csv','rt') as file:
    file_content = file.readlines()
    #loop for storing the items in list
    for item in file_content:
        list1=item.split(":")
        
        dict1[(list1[0])] = list1[2]



  
    