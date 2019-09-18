
"""
Collections or Iterables in Python  
  List  - ordered values
  Tuples - *immutable* ordered values
  Dictionary - key, value pairs
  Sets - collection of distinct values
"""


"""
Lists
  Introduce the concept of grouping of items in Python  
  Arrays in other programming language 
  How to store a long list of information, which does change over time?
  Collection of different data types similar to array and mutable 
"""


#Creating empty list   
empty_list = [] 
print (empty_list)
print (type(empty_list))


#Creating empty list   
empty_list = list ( ) 
print (empty_list)
print (type(empty_list))



#List Creation
my_list = [ 1, 2.3, 3 ]
print(my_list)

#Adding single items in the list in the last 
my_list.append( 5 ) 
print(my_list)
 
#Adding single item in the list at a specific position in the list
my_list.insert ( 0, 6 )
print(my_list)

# Removing values using the value itself 

#Remove a specific item by its value from the list 
my_list.remove ( 4 )   #( ValueError here since 4 is not in the list )




#Removes always the last item from the list 
# Removing values using the index 
print(my_list)
my_list.pop ( )
print(my_list)
 
myindex = my_list.index(3)
print(myindex)

my_list.pop (myindex)
print(my_list)

my_list.pop ( 0 )
print(my_list)


# Accessing the values of the list using index
print(my_list[0])

 
#Deletion of items from the list at a given index using Global Functions
del my_list[0]         #deletes the item from given index
print(my_list)

 

#Replacing in a List
print(my_list)
my_list[0]  = 5
print(my_list)

#my_list [ START : END ] = NEW LIST or ITERABLE
  

#List Slicing 
my_list = [0,5,2,4,3,1 ]
print (my_list[1:])
print (my_list[1:5:2])



#How to make big list which spans to multiple lines 
list1 = ['a', 'b','c' ]
list1 = ['a', 'b',\
         'c' ]
print (list1)



#Sorting of the list items  
print(my_list)
my_list.sort()
print (my_list)


my_list[::-1]
my_list.reverse()

#Sorting using Global function  
my_list = [0,5,2,4,3,1 ]
print (my_list) 
sorted ( my_list )
print (my_list)


#Appending multiple items in a list to another list 
x = [0,1,2]
y = [3,4,5]
x.append (y)      # to add y itself, not its values  
print (x)
# [0, 1, 2, [3, 4, 5]]



#Referencing using the 2D Array concept  
print (x[3])
print(type(x[3]))
print(x[3][0])
x[3][0] = 2   #Visualise it like a 2D array
print (x)

#[0, 1, 2, [2, 4, 5]]


# Extending a list with another list ( adding multiple items to a list )
x = [0,1,2]
y = [3,4,5]

x.extend (y)  #to add values of y, not y itself
print (x)


#this could be achievable by + operator also
x = [0,1,2]
y = [3,4,5]
   
x + y
x = x + y
print (x)

x + 5 #should give an error , since you cannot add a int to list data type 

#try x * 2 will have two copies 

x + [5]


    
# Membership Operators 
# in   ,  not in 

# Used to check if some single item is in a larger collection  
# Return True if the item is in list
# Return False if the item is not in list  

# Example
some_list = [1,2,3,5,6,2,4,3,5,6,7,8,1,2,3]

3 in some_list  # will return True

3 not in some_list # will return False

7 not in some_list  # will return True

# Hand on
while (3 in some_list):
    some_list.remove(3)
print (some_list)
    
    
  

# Identity Operators 
# is ,    is not


# is and is not Operator ( Object Identity )
# is   used to check if objects are same 
# == used to check if values are same

a = [1,2]
b = [1,2]

print ( id(a) )
print ( id (b) )
 
a is b # will return False
a == b # will return True
c = a
print ( id (c) )


a is c # will return True
a == c # will return True


# Introduce the isInstance function usage  

isinstance(45.5, float)

isinstance(45, int)

isinstance(True, bool)

isinstance(None, type(None))


"""
Looping technique using for each

for LOOP_VARIABLE in SEQUENCE_LIST :
    STATEMENTS
"""
my_list = [0,1,2,3,4,5,6]
for number in my_list:
  print (number)


#Introduce the range function to generate a list of numbers

# default the range starts from 0

our_list = list(range(13))
print (type(our_list))
print (our_list)

for number in list(range (13)):
  print (number)


for number in list(range (1,13)):
  print (number)



"""
Hands On 1
"""
# Create a list of number from 1 to 20 using range function. 
# Using the slicing concept print all the even and odd numbers from the list 


# simple foreach statements 
# THIS WILL PRINT ALL THE NUMBERS FROM 12,16,17,24,29,30 and done
for i in [12, 16, 17, 24, 29, 30]:
  print (i)
print("done")


#foreach statement with break statements 
#THIS WILL PRINT 12,16 and done

for i in [12, 16, 17, 24, 29, 30]:
  if i % 2 == 1:  # if the number is odd
    break        # immediately exit the loop
  print(i)
print("done")


#foreach statement with continue  statements 
#THIS WILL PRINT 12,16,24,30 and done
for i in [12, 16, 17, 24, 29, 30]:
  if i % 2 == 1:  # if the number is odd
    continue        # don't process and skip to next iteration
  print(i)
print("done")


#foreach statement with pass statements 
#THIS WILL PRINT 12,16,17,24,29,30 and done

for i in [12, 16, 17, 24, 29, 30]:
  if i % 2 == 1:  # if the number is odd
    pass            # its like comment but is processed   
  print(i)
print("done")




"""
Else clause on Loops
This is also known as a NO BREAK.
It gets executed if the loop is not broken by the break statement
and it gets executed fully.
"""


# else clause with foreach loop
my_list = [1,2,3,4,5,6]

for i in my_list :
  print (i)
  # try to comment and un comment this block and try 
  if i == 3 :
    break;
  # try to comment and un comment this block and try 
else:
  print ('Hit the For/Else Statement !')



# else clause with while loop
i = 1
while (i <= 5) :
  print (i)
  i += 1
  
  # try to comment and un comment this block and try 
  if (i == 3) :
    break
  # try to comment and un comment this block and try 
else:
  print ('hit the while / Else Statement')



#Real Example to implement Else clause on loop

a = 9
b=10

def add(a,b=20):
    c = a+b
    return c

add(10)

def find_index ( to_search, target ) :
  for i, value in enumerate (to_search) :
    if value == target :
      break
  else :
    return -1
  return i

my_list = ['Corey', 'Rick', 'john' ]
index_location = find_index(my_list, 'Rick')

print ("Location of target is index : {}".format(index_location))

    
    

"""
Code Challenge
  Name: 
    Vowels Finder
  Filename: 
    vowels.py
  Problem Statement:
    Remove all the vowels from the list of states  
  Hint: 
    Use nested for loops and while
  Input:
    state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
  Output:
    ['lbm', 'clfrn', 'klhm', 'flrd']
    
"""

"""
Code Challenge
  Name: 
    Pattern Builder
  Filename: 
    pattern.py
  Problem Statement:
    Write a Python program to construct the following pattern. 
    Take input from User.  
  Input: 
    5
  Output:
    Below is the output of execution of this program.
      * 
      * * 
      * * * 
      * * * * 
      * * * * * 
      * * * * 
      * * * 
      * * 
      * 
"""



"""
Code Challenge
  Name: 
    Pallindromic Integer
  Filename: 
    pallindromic.py
  Problem Statement:
    You are given a space separated list of integers. 
    If all the integers are positive and if any integer is a palindromic integer, 
    then you need to print True else print False.
    (Take Input from User)  
  Hint: 
      A palindromic number or numeral palindrome is a number that remains the same
      when its digits are reversed. 
      Like 16461, for example, it is "symmetrical"
      Shorter logic can be developed using any and all and List comprehension
  Input: 
    12 9 61 5 14
  Output:
    True
"""




"""
Introduction to Function 


Functions are group of statements which perform specific tasks 
Functions reduce repetition of code 
Functions can be used to extend functionality in future 
Keep your code Dry ( Don’t Repeat Yourself ) 

"""


# Explain the calling of the function with the example of outsourcing your work to someone else ,
# Take Ashwani use case for taking attendance 

# Calling a global function
c = len("Test")
print(c)

print ( len ("Test") ) 


#Defining an empty function 
def hello_func():
  pass


#Calling the function 
hello_func()
 
# Printing the calling of the function will print None since our function is not returning anything 
print ( hello_func() ) 

# if we miss the () then it will not execute or 
# run the function but will print the address of the function 
hello_func

id(hello_func)



#Defining the function 
def hello_func():
  print ('Hello Forsk')


print ( hello_func() ) 



#Defining the function with return statements 
def hello_func():
  return 'Hello Forsk'



print ( hello_func() ) 



#Defining the function with argument 
def hello_func(greeting):
  return 'Welcome {}'.format ( greeting ) 



print ( hello_func("Sylvester") ) 


#Best Practice 
print ( hello_func(greeting = "Sylvester") ) 



#Defining the function with argument and default 
def hello_func(greeting, name ='You' ):
  return '{} {} Function'.format ( greeting, name ) 


print ( hello_func("Sylvester") ) 

print ( hello_func("Sylvester","Fernandes") ) 

print ( hello_func(greeting="Sylvester",name="Fernandes") ) 

print ( hello_func(name="Fernandes", greeting="Sylvester") ) 



#Introduce the concept of doc string for documentation of the function 
def hello_func(greeting, name ='You' ):
    """ My Greeting function """
    return '{} {} Function'.format ( greeting, name ) 

print ( hello_func("Sylvester") ) 

help(hello_func)
  
    


#Create a new package/module of your own function and 
# import it and use it ( mylibrary.py )

import mylibrary

print (mylibrary.__file__)

dir(mylibrary)

help ( mylibrary.hello_func)

print (mylibrary.hello_func("Sylvester", "Fernandes"))





# Hands On 1  
# Make a function to find whether a year is a leap year or no, return True or False 

# Hands On 2
# Make a function days_in_month to return the number of days in a specific month of a year



"""
Code Challenge
  Name: 
    Pangram
  Filename: 
    pangram.py
  Problem Statement:
    Write a Python function to check whether a string is PANGRAM or not
    Take input from User and give the output as PANGRAM or NOT PANGRAM.
  Hint:
    Pangrams are words or sentences containing every letter of the alphabet at least once.
    For example: "The quick brown fox jumps over the lazy dog"  is a PANGRAM.
  Input: 
    The five boxing wizards jumps.
  Output:
    NOT PANGRAM
"""



"""
Code Challenge
  Name: 
    Bricks
  Filename: 
    bricks.py
  Problem Statement:
    We want to make a row of bricks that is target inches long. 
    We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
    Make a function that prints True if it is possible to make the exact target 
    by choosing from the given bricks or False otherwise. 
    Take list as input from user where its 1st element represents number of small bricks, 
    middle element represents number of big bricks and 3rd element represents the target.
  Input: 
    2, 2, 11
  Output:
    True
"""


"""
Code Challenge
  Name: 
    Reverse Function
  Filename: 
    reverse.py
  Problem Statement:
    Define a function reverse() that computes the reversal of a string.
    Without using Python's inbuilt function
    Take input from User  
  Input: 
    I am testing
  Output:
    gnitset ma I  
"""

"""
Code Challenge
  Name: 
    Translate Function
  Filename: 
    translate.py
  Problem Statement:
    Write a function translate() that will translate a text into "rövarspråket" 
    Swedish for "robber's language". 
    That is, double every consonant and place an occurrence of "o" in between. 
    Take Input from User  
  Input: 
    This is fun
  Output:
    ToThohisos isos fofunon  
"""

"""
Code Challenge
  Name: 
    Operations Function
  Filename: 
    operation.py
  Problem Statement:
    Write following functions for list operations. Take list as input from the User
    Add(), Multiply(), Largest(), Smallest(), Sorting(), Remove_Duplicates(), Print()
    Only call Print() function to display the results in the below displayed 
    format (i.e all the functions must be called inside the print() function 
    and only the Print() is to be called in the main script)

  Input: 
    5,2,6,2,3
  Output:
    Sum = 18
    Multiply = 360
    Largest = 6
    Smallest = 2
    Sorted = [2, 2, 3, 5, 6]
    Without Duplicates = [2, 3, 5, 6]  
"""


"""
Code Challenge
  Name: 
    Sorting
  Filename: 
    sorting.py
  Problem Statement:
    You are required to write a program to sort the (name, age, height) 
    tuples by ascending order where name is string, age and height are numbers. 
    The tuples are input by console. The sort criteria is:
    1: Sort based on name;
    2: Then sort based on age;
    3: Then sort by score. 
    The priority is that name > age > score
  Input: 
    Tom,19,80/
    John,20,90
    Jony,17,91
    Jony,17,93
    Json,21,85
  Output:
    [('John', 20, 90), ('Jony', 17, 91), ('Jony', 17, 93), ('Json', 21, 85), ('Tom', 19, 80)]
"""


"""
Code Challenge
  Name: 
    Centered Average
  Filename: 
    centered.py
  Problem Statement:
    Return the "centered" average of an array of integers, which we'll say is 
    the mean average of the values, except ignoring the largest and 
    smallest values in the array. 
    If there are multiple copies of the smallest value, ignore just one copy, 
    and likewise for the largest value. 
    Use int division to produce the final average. You may assume that the 
    array is length 3 or more.
    Take input from user  
  Input: 
    1, 2, 3, 4, 100
  Output:
    3
"""


"""
Code Challenge
  Name: 
    Unlucky 13
  Filename: 
    unlucky.py
  Problem Statement:
    Return the sum of the numbers in the array, returning 0 for an empty array. 
    Except the number 13 is very unlucky, so it does not count and numbers that 
    come immediately after a 13 also do not count
    Take input from user  
  Input: 
    13, 1, 2, 13, 2, 1, 13
  Output:
    3
"""
 


"""
Collections or Iterables in Python  
  Tuples ( Ordered on Key collection ) 
  
How to store a long list of information, which doesn't change over time? 
Tuples cannot be modified and is IMMUTABLE
Collection of Constant values of different data types 
Represented by ( and ) brackets with a comma or only comma operator
"""

a = 7

#Introduce the concept of Simultaneous Assignment 
a , b = 1 , 2.7

print (a)
print (b)
type (a)
type(b) 


c = (3, 4) #PACKING 
print (c)
type(c) 

  

d , e = c #UNPACKING 
print (d)
print (e)
type (d)
type (e)
type(c)


my_tuple = (1,2,3)

print (type(my_tuple)) 

my_sec_tuple = 1, 2, 3
a,b,c = 1,2,3
print (type(my_sec_tuple)) 

my_sec_tuple = 1 
print (type(my_sec_tuple)) 

my_sec_tuple = (1) 
print (type(my_sec_tuple))

my_sec_tuple = 1, 
print (type(my_sec_tuple)) 

my_sec_tuple = (1,) 
print (type(my_sec_tuple)) 


# Represented by ( and ) brackets with a comma or only comma operator
# Actually Left ( and right ) are not required only to represent tuples


# Tuples concept to swap the variables
# Explain the concept of swapping two variables using third variable 

a = 1
b = 2

a , b = b , a

print (a)
print(b)


# Introduce the unpacking using the function returning a tuple using 
# divmod(23,2) 
# Function returning a tuple, so on left hand side you can multiple variables 

23 / 2

23 // 2  #( Quotient)
23 % 2   #( Remainder)

print (divmod ( 23 , 2 ) ) #will print ( 11 , 1 ) 

x, y = divmod ( 23 , 2 )

print(x)
print(y)

# x will be 11 and y will be 1
# Tuple unpacking requires that the list of variables on the left has the same # number of elements as the length of the tuple.



#Creating empty tuple 
empty_tuple = ()
print(type(empty_tuple))

empty_tuple = tuple()
print(type(empty_tuple))

# Slicing of tuples similar to slicing of string  

names_of_days = ( 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday' )
print (names_of_days)
print (type(names_of_days))



names_of_days [0]

names_of_days [ 1: ]


# Tuples are IMMUTABLE similar to string 

names_of_days[0] = 'some other value'  





# Enumerate 

"""
A lot of times when dealing with iterators, we also get a need to keep a count of iterations.
Python eases the programmers’ task by providing a built-in function enumerate() for this task.

Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object.
This enumerate object can then be used directly in for loops or be converted into a list of tuples using list() method.

Syntax:
enumerate(iterable, start=0)

"""


# Python program to illustrate 
# enumerate function 
l1 = ["eat","sleep","repeat"] 
s1 = "geek"

for item in l1:
    print (item)
 
for item in s1:
    print (item)


counter = 0
for item in l1:
    print (counter, item)
    counter += 1
    
    
  
# creating enumerate objects 
obj1 = enumerate(l1) 
obj2 = enumerate(s1) 
  
print (type(obj1) )
print (list(enumerate(l1)) )


print (list(enumerate(s1)))

# changing start index to 2 from 0 
print (list(enumerate(s1,2)))


# Python program to illustrate # enumerate function in loops 
l1 = ["eat","sleep","repeat"]    

index = 0
for ele in l1 :
  print("{} {} ". format (index, ele ))
  index += 1
  
  
# printing the tuples in object directly 
for ele in enumerate(l1):      
    print (ele)  
    print (type(ele))

# changing index and printing separately 
for index,ele in enumerate(l1):     
    print (index,ele) 


for index,ele in enumerate(l1,100):     
    print (index,ele) 



# Using the concept of enumeration to iterate the tuple 
names_of_days = ( 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday' )


for index, item in enumerate(names_of_days):
  print("{} : {} ". format (index, item ))
 

for step in enumerate(names_of_days):
  print("{} : {} ". format (step[0], step[1] ))
 

for step in enumerate(names_of_days):
    print("{} : {} ". format (*step))
    
#single * denotes tuple and ** denotes dictionary 
 


# Create a custom function to return a tuple   

def my_func():
    return (1,2,3)
 
my_func()

tup = my_func()
 
a,b,c = my_func()

print (a)
print (b)
print (c)



"""
Code Challenge
  Name: 
    generator
  Filename: 
    generator.py
  Problem Statement:
    This program accepts a sequence of comma separated numbers from user 
    and generates a list and tuple with those numbers.  
  Input: 
    2, 4, 7, 8, 9, 12
  Output:
    List : ['2', ' 4', ' 7', ' 8', ' 9', '12'] 
    Tuple : ('2', ' 4', ' 7', ' 8', ' 9', '122')
"""


"""
Code Challenge
  Name: 
    weeks
  Filename: 
    weeks.py
  Problem Statement:
    Write a program that adds missing days to existing tuple of days
  Input: 
    ('Monday', 'Wednesday', 'Thursday', 'Saturday')
  Output:
    ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
"""



# Add more code challenges based on tuple concept


"""
Dictionaries
How to store phone number in a phone book ? 
You would have a list of names and attached to each name a phone number 

Dictionaries is a key value un-ordered pair ( name : mobile number )
Unordered set of key: value pairs where keys are unique
Dictionaries consist of zero or more comma-separated key-value pairs that are enclosed in braces { }
The key and its value are separated by a colon :

We declare dictionaries using {} braces
Like lists dictionaries are also mutable
"""

"""

phonebook = [
    ("John Doe", "555-555-5555"),
    ("Albert Einstein", "212-555-5555"),
]


def find_phonenumber(phonebook, name):
    for n, p in phonebook:
        if n == name:
            return p
    return None

print "John Doe's phone number is", find_phonenumber(phonebook, "John Doe")


phonebook = {
    "John Doe": "555-555-5555",
    "Albert Einstein" : "212-555-5555",
}
print "John Doe's phone number is", phonebook["John Doe"]

"""


# Create empty  dictionary 
dict1 = {} 
print(type(dict1))

dict1 = dict() 
print(type(dict1))

dict1 = dict({})  
print(type(dict1))

print (dict1)
  
dict1 = { 'name':'mobile_number'}
print(dict1)
print(type(dict1))

phone_book = { 'Vidhan':8504982228, 'Aayushi':8905336615, 'Vibhooti':9414701291 }
print(phone_book)
print(type(phone_book))


# Creation of dictionaries
dict1 = {'fname':'John', 'lname':'Mille', 'profession':'plumber',  'age':'32'}
print(dict1)


# Add/Update
dict1['lname'] = 'Miller'
dict1['profession'] = 'electrician'
dict1['age'] = '36'
dict1['city'] = 'NY' #add
print(dict1)

dict1['city'] = 'MA' #update
print(dict1)

dict1.update ( {'age':32, 'city':'NY' } )
print(dict1)

# Printing Values
print (dict1["lname"])
print (dict1.get('lname'))
print (dict1.get('name'))
print (dict1.get('name', 'Not Found'))


# Usage of Dictionary for String Formatting

# This is the old way  
my_string = "Hi ! My name is {name} and I live in {city}.".format(name='John Miller', city='MA')


# Assume that your have 
dict1 = { 'name': 'John Miller', 'city':'MA'}
 
my_string = "Hi ! My name is {name} and I live in {city}.".format(**dict1)


# Remove from dictionary
del dict1['city']
print(dict1)

dict1.pop('city')

dict1.pop('age')
print(dict1)


dict1 = {'fname':'John', 'lname':'Miller', 'profession':'plumber',  'age':'32'}


# To list all the keys
a  = list(dict1.keys())
print(a)
print(type(a)) 

# To list all the values  
print(list(dict1.values()))


# To list all the values  
print(list(dict1.items()))


l = [8,2,6,3]

for item in range(len(l)):
    print(l[item])

# To list all keys  
for key in dict1.keys() :
  print ( key)


# To list all values   
for value in dict1.values():
  print ( value )

 
# To list all values and keys  
for key in dict1:
  print ( key , dict1[key] )

for key in dict1:
  print ( key , dict1.get(key) )


# Looping the dictionary 
for key, value in dict1.items() :
  print ( key, value )

s = set("dafdfdsfdsfdsfsdfdsf")
h = set("fsdfsdsadadjsafad")

s.intersection(h)
h.difference(s)
s.issubset(h)

try:
    f = int(input("Enter: "))
   
except ValueError:
    print("Non- Integer")


"""
Code Challenge
  Name: 
    Supermarket
  Filename: 
    supermarket.py
  Problem Statement:
    You are the manager of a supermarket. 
    You have a list of items together with their prices that consumers bought on a particular day. 
    Your task is to print each item_name and net_price in order of its first occurrence. 
    Take Input from User  
  Hint: 
    item_name = Name of the item. 
    net_price = Quantity of the item sold multiplied by the price of each item.
    try to use new class for dictionary : OrderedDict
  Input:
    BANANA FRIES 12
    POTATO CHIPS 30
    APPLE JUICE 10
    CANDY 5
    APPLE JUICE 10
    CANDY 5
    CANDY 5
    CANDY 5
    POTATO CHIPS 30
  Output:
    BANANA FRIES 12
    POTATO CHIPS 60
    APPLE JUICE 20
    CANDY 20

"""


"""
Code Challenge
  Name: 
    Teen Calculator
  Filename: 
    teen_cal.py
  Problem Statement:
    Take dictionary as input from user with keys, a b c, with some integer 
    values and print their sum. However, if any of the values is a teen -- 
    in the range 13 to 19 inclusive -- then that value counts as 0, except 
    15 and 16 do not count as a teens. Write a separate helper "def 
    fix_teen(n):"that takes in an int value and returns that value fixed for
    the teen rule. In this way, you avoid repeating the teen code 3 times  
  Input: 
    {"a" : 2, "b" : 15, "c" : 13}
  Output:
    Sum = 17
"""


"""
Code Challenge
  Name: 
    Character Frequency
  Filename: 
    frequency.py
  Problem Statement:
    This program accepts a string from User and counts the number of characters (character frequency) in the input string.  
  Input: 
    www.google.com
  Output:
    {'c': 1, 'e': 1, 'g': 2, 'm': 1, 'l': 1, 'o': 3, '.': 2, 'w': 3}
"""



"""
Code Challenge
  Name: 
    Digit Letter Counter
  Filename: 
    digit_letter_counter.py
  Problem Statement:
    Write a Python program that accepts a string from User and calculate the number of digits and letters.
  Hint:
    Store the letters and Digits as keys in the dictionary  
  Input: 
    Python 3.2
  Output:
    Digits 2
    Letters 6 
"""


"""
Two words are anagrams if you can rearrange the letters of one to spell the second.  
For example, the following words are anagrams:

 ['abets', 'baste', 'bates', 'beast', 'beats', 'betas', 'tabes']

Hint: How can you tell quickly if two words are anagrams?  
Dictionaries allow you to find a key quickly.  

"""

# Collections or Iterables in Python  
# Sets


# Set Methods and Operations to Solve Common Problems 

"""
Sets is like a list without duplicate values
 
unordered collection of unique items
no duplicate data
No indexing and No Slicing applicable

Good way to remove duplicate values from a list 
"""

# Creating empty set
empty_set = set()
print(empty_set)
print(type(empty_set))

empty_set = {} #will create an empty dictionary 
print(type(empty_set))


a = { 1,2,2,3,3,4,5 }
print(type (a) ) 
print (a)   
# will print set ( {1 2 3 4 5 } )
# It removes the duplicate values from the list 

 
a  = set("abcdef")
print (a)

a = {'a','b','c','d','e','f'}   # not a dictionary
print (a)




# Set Operations 
# ( add, clear, copy, difference, discard, remove, union, intersection)
# ( isdisjoint, issubset, issuperset, pop )
s1 = {1,2,3,4,5}
print (s1)

s1.add(6)   # add() function can be used to add element to a set
print (s1)

s1.update ([6,7,8])
print (s1) 
 
s2 = {7,8,9}
s1.update([6,7,8],s2)
print (s1)
 
s1.remove(5) # if it doesnt exits it will give Keyerror
print(s1)

s1.discard(5) # this won’t throw key error  
print(s1)

s1.remove(5) # if it doesnt exits it will give Keyerror
print(s1)


"""
It is similar to Mathematical sets.
  Union 
  Difference
  Intersection 
"""

s1 = {1,2,3}
s2 = {2,3,4}
s3 = {3,4,5}
# They have some unique values
# They have overlapping values 


# Question: get a set of values which are in all in these sets 
# Using Intersection method of Set we can find this
 
s4 = s1.intersection(s2) 
print (s4) # which are common in s2 and s1 {2,3}
s5 = s4.intersection(s3)
print (s5)

# Short Cut
s4 = s1.intersection(s2,s3) 
print (s4) # which are common in s3, s2 and s1 {3}



# Question: get a set of values which are different in all these sets 
# Using Difference  method of Set we can find this


s4 = s1.difference(s2) 
print (s4) # which is present in s1 but not present in s2 {1}


s4 = s2.difference(s1) 
print (s4) # which is present in s2 but not present in s1 {4}
 

s4 = s3.difference(s1,s2) 
print (s4) # which is present in s3 but not present in s1or s2 {5}
 

# Symmetric Difference removes which are common in both

s4 = s1.symmetric_difference(s2) 
print (s4) #   differences from both sets    {1,4} 

s4 = s2.symmetric_difference(s1) 
print (s4) #   differences from both sets    {1,4} 


"""
REAL WORLD USAGE OF SETS 
"""

# Question: remove duplicate values from a list 
l1 = [1,2,3,1,2,3]

# You need to traverse the list one by one and create another empty list and 
# check whether it is present in that or no and add it 
# or a simple solution using sets which is more efficient 

l2 = list ( set ( l1 ) ) 
print (l2)



# Real Life Example 
employees = ['Sita', 'Rohit', 'Sylvester', 'Ram', 'Kunal', 'Yogendra', 'Laxman', 'Dev' ]
gym_members = ['Ram', 'Laxman', 'Sita']
developers = ['Kunal', 'Sita', 'Sylvester', 'Dev', 'Ram']


  
#Question:  Which employers have gym membership and are also employees 
#Intersect gym members with developers 

result = list ( set(gym_members).intersection(set(developers)) )
print (result)   # Ram and Sita 



#Question: All the employees who are not either gym members or developers 
#Difference between employees and gym members and developers 

result = set(employees).difference (set(gym_members), set(developers))
print (result)
# sets can replace a lot of membership tests 


# Frozensets

# Though sets can't contain mutable objects, sets are mutable: 
# Frozensets are like sets except that they cannot be changed, 
# i.e. they are immutable: 

cities = frozenset(["Frankfurt", "Basel","Freiburg"])
cities.add("Strasbourg")

    
# Example
vowels = ('a', 'e', 'i', 'o', 'u')
fSet = frozenset(vowels)
print("The frozen set is: ", fSet)



# Another Example
# dictionary key must be immutable.
# frozenset is hashable so you can use it as a key in a dictionary

person = {"name": "John", "age": 23, "sex": "male"}
fSet = frozenset(person)
print("The frozen set is: ", fSet)


# Frozensets are useful in situations where you want to use a set, 
# but you need an immutable object
# For example, you can’t define a set whose elements are also sets, 
# because set elements must be immutable:

x1 = set(['foo'])
x2 = set(['bar'])
x3 = set(['baz'])
x = {x1, x2, x3}


#If you really feel compelled to define a set of sets (hey, it could happen), 
#you can do it if the elements are frozensets, because they are immutable:
x1 = frozenset(['foo'])
x2 = frozenset(['bar'])
x3 = frozenset(['baz'])
x = {x1, x2, x3}





"""
Code Challenge
  Name: 
    Intersection
  Filename: 
    Intersection.py
  Problem Statement:
    With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155]
    Write a program to make a list whose elements are intersection of the above given lists.  
"""



"""
Code Challenge
  Name: 
    Duplicate
  Filename: 
    duplicate.py
  Problem Statement:
    With a given list [12,24,35,24,88,120,155,88,120,155]
    Write a program to print this list after removing all duplicate values 
    with original order reserved  
"""


"""
Code Challenge
  Name: 
    Mailing List
  Filename: 
    mailing.py
  Problem Statement:
  I recently decided to move a popular community  mailing list (3,000 subscribers, 
  60-80 postings/day) from my server to Google Groups. 
  I asked people to joint he Google-based list themselves, 
  and added many others myself, as the list manager. 
  However, after nearly a week, only half of the list had been moved. 
  I somehow needed to learn which people on the old list hadn't yet 
l  signed up for the new list.


  Fortunately, Google will let you export a list of members of a group to 
  CSV format. 
  Also, Mailman (the list-management program I was using on
  my server) allows you to list all of the e-mail addresses being used 
  for a list. Comparing these lists, I think, offers a nice chance to look
  at several different aspects of Python, and to consider how we can 
  solve this real-world problem in a "Pythonic" way.


  The goal of this project is thus to find all of the e-mail addresses on 
  the old list that aren't on the new list. The old list is in a file 
  containing one e-mail address per line, as in:
    
  Hint:
      Refer to mailing.txt for the new and old list of email addresses.
      
"""

#   https://hackhands.com/solving-problems-sets-comprehensions-python/
