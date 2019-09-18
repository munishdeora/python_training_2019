# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 12:04:57 2019

@author: de
Code Challenge
  Name: 
    Anagrams
  Filename: 
    anagram.py
  Problem Statement:
      Two words are anagrams if you can rearrange the letters of one to spell the second.  
      For example, the following words are anagrams:

          ['abets', 'baste', 'bates', 'beast', 'beats', 'betas', 'tabes']

      Write a program that will mine the file anagram.txt for anagrams.  
 

  Hint: 
      How can you tell quickly if two words are anagrams?  
      Dictionaries allow you to find a key quickly.  
      
"""
list1=['abets', 'baste', 'bates', 'beast', 'beats', 'betas', 'tabes']
with open("anagram.txt",'wt') as file1 :
    file1.write(str(list1))
        
list2=list(list1[0])
s=""
final_list=list(map(lambda x : s.join(sorted(x)) ,list1))

if (len(set(final_list))==1):
    print("anagram")
else:
    print("not anagram")    


        
        
        
