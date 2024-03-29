# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 12:36:21 2019

@author: de
"""

"""
Code Challenge
  Name: 
    etc passwd
  Filename: 
    passwd.py
  Problem Statement:
    This exercise assumes that you have access to a copy of /etc/passwd,
    The file in which basic user information is stored on Unix computers.
    The format is:

    nobody:*:-2:-2::0:0:Unprivileged User:/var/empty:/usr/bin/false
    root:*:0:0::0:0:System Administrator:/var/root:/bin/sh
    daemon:*:1:1::0:0:System Services:/var/root:/usr/bin/false
    
    In other words, each line is a set of fields, separated by colon (:) characters. 
    The first field is the username, and the third field is the ID of the user. 
    Thus, on my system, the nobody user has ID -2, the root user has ID 0, 
    and the daemon user has ID 1.  
    You can ignore all but the first and third fields in the file.
    
    There is one exception to this format: 
    A line that begins with a # character is a comment, 
    and should be ignored by the parser.
    
    For this exercise, 
    you must create a dictionary based on /etc/passwd, 
    in which the dict's keys are usernames and the values are the numeric IDs of those users. 
    You should then iterate through this dict, displaying one username and 
    user ID on each line in alphabetical order.
    
"""

dict1={}
list1=[]
#file opening for reading the contents of file
with open('passwd','rt') as file:
    file_content = file.readlines()
    #loop for storing the items in list
    for item in file_content:
        list1=item.split(":")
        usr_name=list1[0]
        usr_id=list1[2]
        #dict1 = { usr_name:usr_id}
        dict1[usr_name]=usr_id

#loop for displaying the shorted list
        
for key, value in sorted(dict1.items()):        
  print ( "user_name : "+ key + "  user_id : " + value )


     
        
       
    

