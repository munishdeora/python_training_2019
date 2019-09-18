# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 13:47:29 2019

@author: de
"""

"""
Code Challenge
  Name: 
    Word counts
  Filename: 
    wordcount.py
  Problem Statement:
    Unix systems contain many utility functions. 
    One of the most useful to me is wc, the "word count" program. 
    If you run wc against a text file, it'll count the characters, words, 
    and lines that the file contains.
     
    The challenge for this exercise is to write a version of wc in Python. 
    However, your version of wc will return four different types of information 
    about the files:
 
        Number of characters (including whitespace)
        Number of words (separated by whitespace)
        Number of lines
        Number of unique words
    
    The program should ask the user for the name of an input file, 
    and then produce output for that file. 
    
"""
    
usr_ip=input("enter the file name : ")    
file=open(usr_ip,"r")
text=file.read()
print("number of character: ",len(text))
print("no of lines : ",text.count('\n')+1)
print ("no of unique word : {}".format(len(set(text.split(None)))))
print("no of word : ",len(text.split(None)))


    
    
    
    
    
    
    
    