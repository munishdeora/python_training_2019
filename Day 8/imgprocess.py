# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 12:56:08 2019

@author: de
"""


"""
Code Challenge
  Name: 
    Image Processing using PIL
  Filename: 
    imgprocess.py
  Problem Statement:
    Given an image, perform image processing operations. 

    Keep only one output image i.e perform all tasks on the same image (override) 
    and print only the name of your output image with extension name in the end of your program. 

    Take the Image name from User (Handle the extension for image file name in your code)
    
    The image processing features to be provided by your code are:

        a.     Greyscale
        b.     Rotate_90 (Rotate the given image file by 90 clockwise)
        c.     Crop (Center) (size = 160(W), 204(H))
        d.     Thumbnail – Generate the thumbnail of the given image (size = 75, 75)
    
"""
from PIL import Image
str1=input("enter the image file name : ")
str2=".jpg"
usr_ip=str1+str2

#  Greyscale  
img =Image.open(usr_ip).convert('LA') 

#Rotate_90
img = img.rotate(90)

#Crop (Center)
width,height = img.size
new_width=160
new_height=204
left = (width - new_width)/2
top = (height - new_height)/2
right = (width + new_width)/2
bottom = (height + new_height)/2
img = img.crop((left, top, right, bottom))

# creating thumbnail 
MAX_SIZE = (75, 75) 
img.thumbnail(MAX_SIZE) 
img.save('img.png') 
print("output image name : "+str1+".png")

