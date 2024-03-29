# File handling in Python 

file = open("words.txt", "rt")

print (file.name)
print (file.mode )
print (file.closed) 

file.close() 

print (file.closed )


"""
There are four different methods (modes) for opening a file
  "r" - Read
  "a" - Append
  "w" - Write 
  "x" - Create 

In addition you can specify if the file should be handled as binary or text mode
  "t" - Text - Default value. Text mode
  "b" - Binary - Binary mode (e.g. images)

"""


# Exception Handling in File Handling
try:
    file = open("words.txt",  "rt" )
    print (file.name)
except IOError:
    print ( "File not Found or incorrect path")
except Exception:
    print ( "This is a general exception")
finally:
    print ("this is called always")
    file.close() 



# Context Manager to open the File 
# ( Automatically closes the file after using in the block ) 

with open('data/words.txt', mode='r', encoding = 'utf-8') as f :
    # perform your operations within this block 
    pass


with open('data/words.txt', mode='rt') as file :
   file_contents = file.read()
   print(type(file_contents))
   print (file_contents)
   
   
with open('data/words.txt', mode='rt') as file :
   file_contents = file.readline()
   print(type(file_contents))
   print (file_contents)
   
   file_contents = file.readline()
   print(type(file_contents))
   print (file_contents)


with open('data/words.txt', mode='rt') as file :
   file_contents = file.readlines()
   print(type(file_contents))
   print(len(file_contents))
   print (file_contents)


with open('data/words.txt', mode='rt') as file :
   for line in file:
       print (line)


with open('words.txt', mode='rt') as file :
   file_contents = file.read(6)
   print(type(file_contents))
   print (file_contents)
   print (list(file_contents))
   

file = open("words.txt", "rt")

position = file.tell()
print (position)

line = file.readline()
print (line )

position = file.tell()
print (position)

# The method seek() sets the file's current position at the offset.

   
# file.seek(offset[, whence])
# offset − This is the position of the read/write pointer within the file.
# whence − defaults to 0 which means absolute file positioning,
#          1 which means seek relative to the current position,
#          2 means seek relative to the file's end


line = file.readline()
print (line) 
   
position = file.tell()
print (position)
    
file.seek(0,0) 
position = file.tell()
print (position)

file_contents = file.read(6)
print (file_contents)

position = file.tell()
print (position)

lines = file.readlines()
print (lines)


# How to create and write into Files

file = open('new.txt', mode='wt')

file.write("Now this has one line\n")
file.writelines(["Second Line\n", "Third Line\n"])

file.close()



# How to read and write non text files

with open ("a.jpg", "rb") as rf :
  with open ("b.jpg", "wb") as wf :
    for line in rf :
      wf.write ( line)


# Important Operating System related file handling
      
import os

os.getcwd()

os.chdir("C:\\Users\\de\\Desktop\\Forsk\\Day 2")

os.getcwd()

os.chdir("/Users/sylvester/Google Drive/Skills_Dev/Courses/2019/Trainings_2019/Python")

os.path.exists("zoo.csv")

os.path.exists("data/zoo.csv")

os.remove("new.txt")

os.makedirs("myfolder")

os.rmdir("myfolder")

os.listdir(".")





"""
Code Challenge
  Name: 
    copy command
  Filename: 
    copy.py
  Problem Statement:
    Make a program that create a copy of a file    
"""


"""
Code Challenge
  Name: 
    Create a list of absentee
  Filename: 
    absentee.py
  Problem Statement:
    Make a program that create a file absentee.txt
    The program should take max 25 students name one by one
    When the user enter a blank line, it should terminate the input
    Store all the name of students in the file    
    Once all the students names have been entered, it should display the list
    
"""

"""
Code Challenge
  Name: 
    Zoo Management
  Filename: 
    zoo.py
  Problem Statement:
    Create different functions to :
    read the zoo.csv file using readlines and print them
    Print in list of animals in groups (elephant / tiger / lion / zebra / kangaroo)
    print the total number of water need by elephant / tiger / lion / zebra / kangaroo
    print the total number of water needed by all the animals    
"""

"""
Code Challenge
  Name: 
    Romeo and Juliet
  Filename: 
    romeo.py
  Problem Statement:
    Let’s start with a very simple file of words taken from the text of 
    Romeo and Juliet. (romeo.txt)
    We will write a Python program to read through the lines of the file
    break each line into a list of words
    and then loop through each of the words in the line,
    and count each word using a dictionary.    
"""

"""
Code Challenge
  Name: 
    SHA-1 Algorithm
  Filename: 
    hash.py
  Problem Statement:
    Find hash of a file using hashlib library and using SHA-1 algorithm
  Hint:
    https://www.programiz.com/python-programming/examples/hash-file
"""

"""
Code Challenge
  Name: 
    Resolution of an Image
  Filename: 
    resolution.py
  Problem Statement:
    Find the resolution of any jpeg Image file ( width x height )
  Hint:
    https://www.programiz.com/python-programming/examples/resolution-image
"""


"""
Code Challenge
  Name: 
    Last Line
  Filename: 
    lastline.py
  Problem Statement:
    Ask the user for the name of a text file. 
    Display the final line of that file.
    Think of ways in which you can solve this problem, 
    and how it might relate to your daily work with Python.
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


"""
Code Challenge
  Name: 
    Word count
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


"""
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

# PIL ( PILLOW LIBRARY )


"""
Installing external modules/packages in IDLE
run this pip command from the scripts directory inside the directory 
where you have installed python 

go to python scripts directory and run the below command 

pip install Pillow

Or Open the Anaconda Prompt 

conda install <name of library>

"""



from PIL import Image
import os

#os.chdir("/Users/sylvester/Desktop/Python/")

# Open the image and create it's instance
img = Image.open("data/sample.jpg")

# Gives the dimensions or the size of the image
print (img.size)

# Gives the width of the image
print (img.width)

# Gives the width of the image
print (img.height)


# Gives the format of image like JPEG, PNG ...
    print (img.format)

# Gives the mode of image like RGB, binary, GreyScale ...
print (img.mode)

# Displays the Image
img.show()


# Rotate the image with the given angle
# Create separate instance for rotated image
# ROTATE_90, ROTATE_180, ROTATE_270
img_rotate = img.transpose(Image.ROTATE_90)
 
# Displays the rotated image
img_rotate.show()  

img_rotate.save("data/sample1.jpg")


# Resizing the image 
small_im = img.resize((300, 150), resample=Image.BICUBIC)
small_im.save('data/small_sample1.jpg')


# Creating Thumbnail
img = Image.open("data/sample.jpg")
img.thumbnail((150, 100))
print(img.width, img.height)
img.save('data/thumb_sample1.jpg')


# Cropping
img = Image.open("data/sample.jpg")
                    # startx, starty,width,height
crop_im = img.crop(box=(340, 20, 560, 164))
crop_im.save('data/crop_sample1.jpg')


# Adding a Border

img = Image.open("data/sample.jpg")
border_im = Image.new('RGB', (img.width+20, img.height+20), 'yellow')
border_im.paste(img, (10, 10))
border_im.save("data/border_sample.jpg")


# Flip the image
# Create separate instance for flipped image
# FLIP_LEFT_RIGHT, FLIP_TOP_BOTTOM
img_flip = img.transpose(Image.FLIP_TOP_BOTTOM)

# Displays the rotated image
img_flip.show()  
img_flip.save("data/sample2.jpg")



# Make Black and White image
img_bw = Image.open("data/sample.jpg")
img_bw.convert(mode='L').save('data/sample3.jpg')
img_bw = Image.open("data/sample3.jpg")
img_bw.show()


# Blur the Images 
from PIL import Image, ImageFilter
img_blur = Image.open("data/sample.jpg")

# 15 is the radius, default is 2 so it doesn’t show too much 
img_blur.filter(ImageFilter.GaussianBlur(15)).save('data/sample4.jpg')
img_blur = Image.open("data/sample4.jpg")
img_blur.show()


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

"""
Code Challenge
  Name: 
    Different sizes
  Filename: 
    png.py
  Problem Statement:
    Convert all files PNG in a directory into different sizes
  Hint: 
    os.listdir('.') function will list all the files in the current directory   
"""


# Playing with csv files


"""
For example, you might export the results of a data mining program to a CSV 
file and then import that into a spreadsheet to analyze the data, generate 
graphs for a presentation, or prepare a report for publication.


A CSV file (Comma Separated Values file) is a type of plain text file 
that uses specific structuring to arrange tabular data.

Because it's a plain text file, it can contain only actual text data
—in other words, printable ASCII or Unicode characters.

Normally, CSV files use a comma to separate each specific data value.

In general, the separator character is called a delimiter, 
and the comma is not the only one used.
Other popular delimiters include the tab (\t), colon (:) and semi-colon (;).
 
"""

    
import csv

with open("data/Salaries.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    # row has the list of all columns
    for row in csv_reader:
        print (row)
     
 
# Printing  a specific column    
import csv

with open("data/Salaries.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    # row has the list of all columns
    for row in csv_reader:
        print ( row[5] )
      

    
# Skipping a header line or first line
        
import csv

with open("data/Salaries.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    # Skip the first row
    next(csv_reader)
    # row has the list of all columns
    for row in csv_reader:
        print (row)

        
        
# Reading as a Dictionary
        
import csv

with open("data/Salaries.csv") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    for row in csv_reader:
        #print ( row )
        #print ( row['discipline'] )
        print ( row['salary'] )
        #print ( row['service'] )
        #print ( row['rank'] )
        #print ( row['sex'] )
        #print ( row['phd'] )



# Creating a csv file
        
import csv

with open('data/employee.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',')

    employee_writer.writerow(['John Smith', 'Accounting', 'November'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])


"""
Code Challenge
  Name: 
    Reading and Writing CSV
  Filename: 
    csv.py
  Problem Statement:
    Create a program that reads from one CSV file (/etc/passwd), 
    and writes to another one. 
    
    You are to read from passwd file,
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

"""
https://pymbook.readthedocs.io/en/latest/
https://www.datacamp.com/community/tutorials/reading-writing-files-python
https://www.datacamp.com/community/tutorials/python-excel-tutorial
https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python
"""



