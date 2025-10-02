# note_for_pythonsep29

12.30- create new python keynote

python is a popular programming language.
# Guido van rossum creator 1991 .
web developement side ,
mathematics,
system scripting.

why use server and web application


# check python version :-
python3 --version

# check python editor version 
import sys
print(sys.version)

# commandline execution:- 
python3 and filename. like ("myfile",..)

# python indentation :-
indentation refers space at the begining 
 # the indentaion in python is very important 

 the given the following example is right

#       eg:- 
    if 5 > 2:
    print("Five is greater than two!")

# Python Variables :- 
     x = 5
     y = "Hello, World!
     
# Python Comments:- 

* Comments can be used to make the code more readable.

* Comments can be used to prevent execution when testing code.

# Multiline Comments
Python does not really have a syntax for multiline comments.

To add a multiline comment you could insert a # for each line:

Or, not quite as intended, you can use a multiline string.

Since Python will ignore string literals that are not assigned to a variable, you can add a multiline string (triple quotes) in your code, and place your comment inside it:

# Variables:- 
Variables are containers for storing data values.
x = 5
y = "John"
print(x)
print(y)

#   casting:-  
* If you want to specify the data type of a variable, this can be done with casting

# Single or Double Quotes?

String variables can be declared either by using single or double quotes:

# eg:-
    x = "John"
# is the same as
     x = 'John'

# Case-Sensitive
* Variable names are case-sensitive.

# Variable Names
 1. A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).

# Rules for Python variables:

1. A variable name must start with a letter or the underscore character
2. A variable name cannot start with a number
3. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
4. Variable names are case-sensitive (age, Age and AGE are three different variables)
5. A variable name cannot be any of the Python keywords.

# EXAMPLE :- 
    Legal variable names:

    myvar = "John"
    my_var = "John"
    _my_var = "John"
    myVar = "John"
    MYVAR = "John"
    myvar2 = "John"

# Multi Words Variable Names
1. Variable names with more than one word can be difficult to read.

2. There are several techniques you can use to make them more readable:

# Camel Case
Each word, except the first, starts with a capital letter:
# Pascal Case
Each word starts with a capital letter:

# (EX) ;- 
MyVariableName = "John"Snake Case
Each word is separated by an underscore character:

my_variable_name = "John"

# Snake Case
Each word is separated by an underscore character:

my_variable_name = "John"

# Many Values to Multiple Variables
Python allows you to assign values to multiple variables in one line:

# Eg:- 
 x, y, z = "Orange", "Banana", "Cherry"
    print(x)
    print(y)
    print(z)
    
# One Value to Multiple Variables
    And you can assign the same value to multiple variables in one line:
    
# Eg:- 
  x = y = z = "Orange"

# Output Variables
1. The Python print() function is often used to output variables.
2. In the print() function, you output multiple variables, separated by a comma:
3. You can also use the + operator to output multiple variables:

# Python - Global Variables:- 

# Global Variables

1. Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.
  
2. Global variables can be used by everyone, both inside of functions and outside.

# (eg..,) 
Create a variable outside of a function, and use it inside the function

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()


#  The global Keyword:- 
  Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
  
  To create a global variable inside a function, you can use the global keyword.
  
  Example
  If you use the global keyword, the variable belongs to the global scope:
  
  def myfunc():
    global x
    x = "fantastic"
  
  myfunc()
  
  print("Python is " + x)

# python data types:- 

  In programming, data type is an important concept.
  
  Variables can store data of different types, and different types can do different things.
  
  Python has the following data types built-in by default, in these 
  
  # categories:Text Type:	str
    Numeric Types:	int, float, complex
    Sequence Types:	list, tuple, range
    Mapping Type:	dict
    Set Types:	set, frozenset
    Boolean Type:	bool
    Binary Types:	bytes, bytearray, memoryview
    None Type:	NoneType

# Python Numbers
There are three numeric types in Python:

int
float
complex
Variables of numeric types are created when you assign a value to them:

# eg:-
    x = 1    # int
    y = 2.8  # float
    z = 1j   # complex #Note: You cannot convert complex numbers into another number type.

# Type Conversion:-
You can convert from one type to another with the int(), float(), and complex() methods:
 Note: You cannot convert complex numbers into another number type.

# Random Number:-
Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:

    Import the random module, and display a random number from 1 to 9:

    import random

    print(random.randrange(1, 10))
   
# Python Casting:-
* Specify a Variable Type

# String:-
Strings in python are surrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello".

You can display a string literal with the print() function:

# Quotes Inside Quotes
1. You can use quotes inside a string, as long as they don't match the quotes surrounding the string:

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# Multiline Strings assigning
You can assign a multiline string to a variable by using three quotes:

Example
You can use three double quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Strings are Arrays
Like many other popular programming languages, strings in Python are arrays of unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.

Example
Get the character at position 1 (remember that the first character has the position 0):

a = "Hello, World!"
print(a[1])

# String Length
To get the length of a string, use the len() function.

# Example:-
The len() function returns the length of a string:

a = "Hello, World!"
print(len(a))

# Check String:-
*  1.To check if a certain phrase or character is present in a string, we can use the keyword in.

txt = "The best things in life are free!"
print("free" in txt)

# Check if NOT:- 
To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

Example
Check if "expensive" is NOT present in the following text:

txt = "The best things in life are free!"
print("expensive" not in txt)

# Slcing:- 

# Slice From the Start:- 
By leaving out the start index, the range will start at the first character:

# Example:-
Get the characters from the start to position 5 (not included):

# slice to te end
b = "Hello, World!"
print(b[:5]
)Upper Case


# Upper Case
ExampleGet your own Python Server
The upper() method returns the string in upper case:

a = "Hello, World!"
print(a.upper())Upper Case

# Example:- Get your own Python Server
1. The upper(Upper Case
2. ExampleGet your own Python Server
3. The upper() method returns the string in upper case:

a = "Hello, World!"
print(a.upper())) method returns the string in upper case:

a = "Hello, World!"
print(a.upper())

# Method	    Description

# capitalize()	| Converts the first character to upper case
# (eg):- 
    
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)

# casefold()	| Converts string into lower case
# (eg):-
         txt = "Hello, And Welcome To My World!"
         x = txt.casefold()
         print(x)
  
# center()	| Returns a centered string
# eg:-
       txt = "banana"
       x = txt.center(20)
       print(x)

# count() |	Returns the number of times a specified value occurs in a string
# (eg):-
        txt = "I love apples, apple are my favorite fruit"
        x = txt.count("apple")
        print(x)

# encode() |	Returns an encoded version of the string
# (eg):- 
         txt = "My name is Ståle"
         x = txt.encode()
         print(x)

#  endswith() |	Returns true if the string ends with the specified value
# (eg):- 
        txt = "My name is Ståle"
        x = txt.encode()
        print(x)

# expandtabs()	Sets the tab size of the string
# (eg):-
        txt = "H\te\tl\tl\to"
        x =  txt.expandtabs(2)
        print(x)

        print(txt)
        print(txt.expandtabs())
        print(txt.expandtabs(2))
        print(txt.expandtabs(4))
        print(txt.expandtabs(10))

#  find()  | Searches the string for a specified value and returns the position of where it was found
# (eg):-
        txt = "Hello, welcome to my world."
        x = txt.find("welcome") 
        print(x)

# Syntax
    string.find(value, start, end)
    Parameter Values

# Parameter |	Description
#    value:-	Required. The value to search for
#    start	    Optional. Where to start the search. Default is 0
#    end   	    Optional. Where to end the search. Default is to the end of the string

# (ex):-
     txt = "Hello, welcome to my world."
    x = txt.find("e", 5, 10)
    print(x)

#  format()  | 	Formats specified values in a string
# (eg):-
        txt = "For only {price:.2f} dollars!"
        print(txt.format(price = 49))

# Syntax
    string.format(value1, value2...)

     txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
    txt2 = "My name is {0}, I'm {1}".format("John",36)
    txt3 = "My name is {}, I'm {}".format("John",36)

#  format_map()	 |   Formats specified values in a string
    The format_map() method formats the specified values of a dictionary and insert them inside the string's placeholders.

# (eg):-
        myvar = {"name" : "Jane", "age" : 36}
        txt = "Happy birthday {name} you are now on level {age}!"
        print(txt.format_map(myvar))

# The format_map()  |  method returns the formatted string.

# index()   |	Searches the string for a specified value and returns the position of where it was found
# (eg):-

1. The index() method finds the first occurrence of the specified value.
2. The index() method raises an exception if the value is not found.
3. The index() method is almost the same as the find() method, the only difference is that the find() method returns -1 if the value is not found. (See example below)

# Syntax
string.index(value, start, end)

# (eg):-
        txt = "Hello, welcome to my world."
        x = txt.index("e", 5, 10)
        print(x)
     
#  isalnum()  |	Returns True if all characters in the string are alphanumeric

# (eg):-
        txt = "Company12"
        x = txt.isalnum()
        print(x)

# isalpha()	 | Returns True if all characters in the string are in the alphabet

# (eg):-
        txt = "CompanyX"
        x = txt.isalpha()
        print(x)

    isascii()	Returns True if all characters in the string are ascii characters

#  isdecimal() |  Returns True if all characters in the string are decimals
 
# Definition and Usage
    The isdecimal() method returns True if all the characters are decimals (0-9).

    This method can also be used on unicode objects. See example below.

# Syntax
string.isdecimal()


    isdigit()	Returns True if all characters in the string are digits


#   isidentifier()	|  Returns True if the string is an identifier
   Check if the string is a valid identifier:

# (eg):- 
   txt = "Demo"
   x = txt.isidentifier()
   print(x)

    islower()	Returns True if all characters in the string are lower case
    isnumeric()	Returns True if all characters in the string are numeric

# isprintable()	 |  Returns True if all characters in the string are printable

#  Definition and Usage
The isprintable() method returns True if all the characters are printable, otherwise False.

# Example of none printable character can be carriage return and line feed.
     
#  (eg):- 
        txt = "Hello!\nAre you #1?"
        x = txt.isprintable()
        print(x)   

#  isspace() |	Returns True if all characters in the string are whitespaces

# Definition and Usage
    The isspace() method returns True if all the characters in a string are whitespaces, otherwise False.

# Syntax
string.isspace()


    istitle()	Returns True if the string follows the rules of a title
    isupper()	Returns True if all characters in the string are upper case

#  join() | Joins the elements of an iterable to the end of the string
   
# (eg):-
        myTuple = ("John", "Peter", "Vicky")
        x = "#".join(myTuple)
        print(x)


    ljust()	Returns a left justified version of the string
    lower()	Converts a string into lower case
    lstrip()	Returns a left trim version of the string
    maketrans()	Returns a translation table to be used in translations
    partition()	Returns a tuple where the string is parted into three parts
    replace()	Returns a string where a specified value is replaced with a specified value
    rfind()	Searches the string for a specified value and returns the last position of where it was found
    rindex()	Searches the string for a specified value and returns the last position of where it was found
    rjust()	Returns a right justified version of the string
    rpartition()	Returns a tuple where the string is parted into three parts
    rsplit()	Splits the string at the specified separator, and returns a list
    rstrip()	Returns a right trim version of the string


# split() |	Splits the string at the specified separator, and returns a list

#  Definition and Usage
 The split() method splits a string into a list.

 You can specify the separator, default separator is any whitespace.

Note: When maxsplit is specified, the list will contain the specified number of elements plus one.

# Syntax
    string.split(separator, maxsplit)
    Parameter Values
    Parameter	Description
    separator	Optional. Specifies the separator to use when splitting the string. By default any whitespace is a separator
    maxsplit	Optional. Specifies how many splits to do. Default value is -1, which is "all occurrences"

# (eg):- 
        txt = "welcome to the jungle"
        x = txt.split()
        print(x)

# splitlines()	|  Splits the string at line breaks and returns a list
  
#  Definition and Usage
   The splitlines() method splits a string into a list. The splitting is done at line breaks.

#  Syntax
   string.splitlines(keeplinebreaks)
# (eg):- 
        txt = "Thank you for the music\nWelcome to the jungle"
        x = txt.splitlines()
        print(x)
# o/p:- ['Thank you for the music', 'Welcome to the jungle']


# Definition and Usage
The splitlines() method splits a string into a list. The splitting is done at line breaks.

# Syntax
string.splitlines(keeplinebreaks)


#   startswith() |	Returns true if the string starts with the specified value

# Syntax
string.startswith(value, start, end)

# (eg):-
        txt = "Hello, welcome to my world."
        x = txt.startswith("Hello")
        print(x)

#  strip()	Returns a trimmed version of the string
  The strip() method removes any leading, and trailing whitespaces.

  Leading means at the beginning of the string, trailing means at the end.

 You can specify which character(s) to remove, if not, any whitespaces will be removed.

# Syntax
string.strip(characters)

# (eg):-
       txt = "     banana     "
       x = txt.strip()
       print("of all fruits", x, "is my favorite")


#  swapcase()	Swaps cases, lower case becomes upper case and vice versa

# (eg):-
        txt = "Hello My Name Is PETER"
        x = txt.swapcase()
        print(x)

#  title()  | Converts the first character of each word to upper case
# The title() method returns a string where the first character in every word is upper case. Like a header, or a title.

If the word contains a number or a symbol, the first letter after that will be converted to upper case.

# (eg):-
        txt = "Welcome to my 2nd world"
        x = txt.title()
        print(x)

#  translate()  | Returns a translated string

# (eg):-  
# use a dictionary with ascii codes to replace 83 (S) with 80 (P):
        mydict = {83:  80}
        txt = "Hello Sam!"
        print(txt.translate(mydict))

# upper()	Converts a string into upper case 
# (eg):-
        txt = "Hello my friends"
        x = txt.upper()
        print(x)
 
# zfill()	Fills the string with a specified number of 0 values at the beginning:-

 # (eg):-
    txt = "50"

    x = txt.zfill(10)

    print(x)

# Python Booleans
    Booleans represent one of two values: True or False.

    Boolean Values
    In programming you often need to know if an expression is True or False.

    You can evaluate any expression in Python, and get one of two answers, True or False.

    When you compare two values, the expression is evaluated and Python returns the Boolean answer:


    Most Values are True
    Almost any value is evaluated to True if it has some sort of content.

    Any string is True, except empty strings.

    Any number is True, except 0.

    Any list, tuple, set, and dictionary are True, except empty ones

# (eg):- 
        bool("abc")
        bool(123)
        bool(["apple", "cherry", "banana"])


# List 
Lists are used to store multiple items in a single variable.
Lists are created using square brackets:

# Example  
Create a List:

thislist = ["apple", "banana", "cherry"]
print(thislist)

The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
Since lists are indexed, lists can have items with the same value:

# Python Collections (Arrays)
There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

* Set items are unchangeable, but you can remove and/or add items whenever you like.

** As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.


# This example returns the items from the beginning to, but NOT including, "kiwi":

# Access Items
List items are indexed and you can access them by referring to the index number:

# (eg):-  Print the second item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Negative Indexing
Negative indexing means start from the end

-1 refers to the last item, -2 refers to the second last item etc.

# Range of Indexes
You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a new list with the specified items.

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

# Change Item Value
To change the value of a specific item, refer to the index number:

Change the second item:

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Change a Range of Item Values
To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:

# Example:- 
Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# Insert Items
To insert a new list item, without replacing any of the existing values, we can use the insert() method.

The insert() method inserts an item at the specified index:

# (ex):-
        thislist = ["apple", "banana", "cherry"]
        thislist.insert(2, "watermelon")
        print(thislist) 

# append items:- 
append - thislist.append("orange")
insert - thislist.insert(1, "orange")

Extend List
To append elements from another list to the current list, use the extend() method.

# (eg):-
       thislist = ["apple", "banana", "cherry"]
       tropical = ["mango", "pineapple", "papaya"]
       thislist.extend(tropical)
       print(thislist)

# Add Any Iterable
The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

# Example
Add elements of a tuple to a list:

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# remove specified items in list

1. The remove() method removes the specified item.

2. The pop() method removes the specified index.

The del keyword also removes the specified index:
del thislist[0]

# Clear the List
The clear() method empties the list.

The list still remains, but it has no content.

# Example:-
Clear the list content:

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# how to access list items 
  # index
  # negative index
  # range index
  # in
  
# change list items
 # use index
 # ranged
 # inset items

# add list items
  # append()
  # insert items 
  # expend items - any iterable

# remove list items 
  1. remove
  2. pop()
  3. del

# python list though loop
  
  1. for in 

# Loop though the index number
   for i in range(len(thislist))

# while loop 

# Example
 Print all items, using a while loop to go through all the index numbers

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# Looping Using List Comprehension
List Comprehension offers the shortest syntax for looping through lists:

# Example:- 
 A short hand for loop that will print all items in a list:

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

# Python - List Comprehension

# The Syntax;- 
   # newlist = [expression for item in iterable if condition == True]

# Condition
    The condition is like a filter that only accepts the items that evaluate to True.
 
  # example:-
    newlist = [x for x in fruits if x != "apple"]

# Iterable
The iterable can be any iterable object, like a list, tuple, set etc.

# Example
You can use the range() function to create an iterable:

newlist = [x for x in range(10)]

# Python - Sort Lists

  # Sort() 
           List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

  # Sort Descending
           To sort descending, use the keyword argument reverse = True:

 # Example :-  thislist.sort(reverse = True) 

# Customize Sort Function

def myfunc(n):
    return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

# Case Insensitive Sort
    By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:

# example
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

Luckily we can use built-in functions as key functions when sorting a list.

So if you want a case-insensitive sort function, use str.lower as a key function:

# Example
Perform a case-insensitive sort of the list:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# Reverse Order 
  use reverse() sort the list in reverse order 

# PYTHON Copy Lists 

# Copy a list
 You can use the built-in List method copy() to copy a list.

 # eg:-
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# o/p ['apple', 'banana', 'cherry']

# Use the list() method same as copy list

# Use the slice Operator
  
 1. You can also make a copy of a list by using the : (slice) operator.

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

# o/p:-  ['apple', 'banana', 'cherry']

PYTHON - Join lists :- 
 
 list3 = list1 + list2

One of the easiest ways are by using the + operator.

# ex:-
for x in list2:
  list1.append(x)



# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

# Python Tuples:-

1. Tuples are used to store multiple items in a single variable.
2. A tuple is a collection which is ordered and unchangeable.
3. Tuples are written with round brackets.

# example

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# Ordered
When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

# Unchangeable
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

# Allow Duplicates
Since tuples are indexed, they can have items with the same value:

# type()
From Python's perspective, tuples are defined as objects with the data type 'tuple':

# (eg);- 
 print(type(mytuple))

# The tuple() Constructor
It is also possible to use the tuple() constructor to make a tuple.

# (ex):-   
 thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets

 # Python - Access Tuple Items 

 # Access Tuple Items
You can access tuple items by referring to the index number, inside square brackets:

# (eg):- 
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Negative Indexing
Negative indexing means start from the end.

# Python - Update Tuples
Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.

# Change Tuple Values:-

Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

# Example:-

Convert the tuple into a list to be able to change it:

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# Add Items:

# 
Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.

1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.

# Example
Convert the tuple into a list, add "orange", and convert it back into a tuple:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#  Add tuple to a tuple.
 You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:

Example
Create a new tuple with the value "orange", and add that tuple:

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

# Note: When creating a tuple with only one item, remember to include a comma after the item, otherwise it will not be identified as a tuple.

# Remove Items:- 

1. Tuples are unchangeable.
 same as change to the list  convert  after remove and again convert to tuple.

# (ex):-
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

Or you can delete the tuple completely:

# Example:- 
The del keyword can delete the tuple completely:

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

# Python - Unpack Tuples

When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

# Example:-

Packing a tuple:
fruits = ("apple", "banana", "cherry")

# Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.

# Using Asterisk*

If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

# Example
Assign the rest of the values as a list called "red":

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

# If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.

# example:- 
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

# o/p:-
apple
['mango', 'papaya', 'pineapple']
cherry


# Python - Loop Tuples:-

# Loop Through a Tuple
You can loop through the tuple items by using a for loop.

# Example:-

Iterate through the items and print the values:

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

# Loop Through the Index Numbers
You can also loop through the tuple items by referring to their index number.

Use the range() and len() functions to create a suitable iterable.

# Example:- 
Print all items by referring to their index number:

# (eg):-
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

# Using a While Loop
You can loop through the tuple items by using a while loop.

Use the len() function to determine the length of the tuple, then start at 0 and loop your way through the tuple items by referring to their indexes.

Remember to increase the index by 1 after each iteration.

# Example:- 
Print all items, using a while loop to go through all the index numbers:

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

# Python - Join Tuples:-
Join Two Tuples
To join two or more tuples you can use the + operator:

# Example:- 
Join two tuples:

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

Multiply Tuples
If you want to multiply the content of a tuple a given number of times, you can use the * operator:

# Example
Multiply the fruits tuple by 2:

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

# Multiply Tuples

If you want to multiply the content of a tuple a given number of times, you can use the * operator:

# Example
Multiply the fruits tuple by 2:

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

# Tuple Methods
Python has two built-in methods that you can use on tuples.

# Method	|   Description
# count()  |	Returns the number of times a specified value occurs in a tuple
# index() |	Searches the tuple for a specified value and returns the position of where it was found

# Python Sets.

# Set
  # Sets are used to store multiple items in a single variable.

  # A set is a collection which is unordered, unchangeable*, and unindexed.

  # Once a set is created, you cannot change its items, but you can add new items.

# (example):-
           
      myset = {"apple", "banana", "cherry"}
  
# Set Items
  Set items are unordered, unchangeable, and do not allow duplicate values.

# Unordered
  Unordered means that the items in a set do not have a defined order.

  Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

# Unchangeable
  Set items are unchangeable, meaning that we cannot change the items after the set has been created.

 Once a set is created, you cannot change its items, but you can remove items and add new items.

# Duplicates Not Allowed
 Sets cannot have two items with the same value.

# type()
   From Python's perspective, sets are defined as objects with the data type 'set':

# The set() Constructor
   It is also possible to use the set() constructor to make a set

# Access Items :-
  
  # You cannot access items in a set by referring to an index or a key.

  But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

#  example: -

       thisset = {"apple", "banana", "cherry"}
       print("banana" in thisset)

  2) .  
        Check if "banana" is NOT present in the set:

        thisset = {"apple", "banana", "cherry"}

        print("banana" not in thisset)

# Python - add Set Items:- 

# Once a set is created, you cannot change its items, but you can add new items.

To add one item to a set use the add() method.

# (Eg):-
        thisset.add("orange")

#  Add Sets
To add items from another set into the current set, use the update() method.

# (Ex):-
       thisset.update(tropical)

# Add Any Iterable
  # The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

# Python - Remove Set Items :- 
    del
    clear()
    pop() 
    discard()

 # Remove Item
      To remove an item in a set, use the remove(), or the discard() method.

# Remove "banana" by using the discard() method:
   # Eg :-
           thisset.discard("banana")

# Remove a random item by using the pop() method:

# The clear() method empties the set:
  
  # Eg;-
         thisset.clear()

#  The del keyword will delete the set completely:

  # (Eg).,  
     del thisset

#   Python - Loop Sets :-

# Loop Items :-
         You can loop through the set items by using a for loop:

# Python - Join Sets :-

  # Join Sets:- 

  # union() and Update()
  # intersection()
  # difference()
  # symmetric_difference() 


      There are several ways to join two or more sets in Python.

#  The union() and update() methods joins all items from both sets.
   
  # Eg:-
        set3 = set1.union(set2)

# Join Multiple Sets:- 

  # Eg:-
      myset = set1.union(set2, set3, set4)

      The intersection() method keeps ONLY the duplicates.

      The difference() method keeps the items from the first set that are not in the other set(s).

      The symmetric_difference() method keeps all items EXCEPT the duplicates.

# When using the | operator, separate the sets with more | operators:

# Example:-
          Use | to join two sets:

          set1 = {"a", "b", "c"}
          set2 = {1, 2, 3}
          set3 = {"John", "Elena"}
          set4 = {"apple", "bananas", "cherry"}

          myset = set1 | set2 | set3 |set4
          print(myset)

# Join a Set and a Tuple
The union() method allows you to join a set with other data types, like lists or tuples.

Note: Both union() and update() will exclude any duplicate items.

The result will be a set.

# Eg:-
       z = x.union(y)

# Update
The update() method inserts all items from one set into another.

The update() changes the original set, and does not return a new set.

 #  Example
      The update() method inserts the items in set2 into set1:

#  Eg:- 
      set1 = {"a", "b" , "c"}
      set2 = {1, 2, 3}

      set1.update(set2)
      print(set1)

# Intersection
   
#  &
#  intersection_update()


Keep ONLY the duplicates

The intersection() method will return a new set, that only contains the items that are present in both sets.

# Example :-
            set3 = set1.intersection(set2)

 * You can use the & operator instead of the intersection() method, and you will get the same result.

 #  set3 = set1 & set2

 # The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.

 # Difference
    The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.

  # Eg:- 
        set3 = set1.difference(set2)

  You can use the - operator instead of the difference() method, and you will get the same result.
  
  # Eg:- 
        set3 = set1 - set2

  The difference_update() method will also keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.

# Example
    Use the difference_update() method to keep the items that are not present in both sets:

# Eg:- 
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)

#  Symmetric Differences
The symmetric_difference() method will keep only the elements that are NOT present in both sets.

# Example:-
           set3 = set1.symmetric_difference(set2)

# You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.

# Example


Use ^ to join two sets:

set3 = set1 ^ set2

# The symmetric_difference_update()
     method will also keep all but the duplicates, but it will change the original set instead of returning a new set.

# Example:-
            set1.symmetric_difference_update(set2)

# Frozenset Methods:-

       Being immutable means you cannot add or remove elements. However, frozensets support all non-mutating operations of sets.

#    Use the frozenset() constructor to create a frozenset from any iterable.

# Method	   Shortcut    	Description	
copy()	               	Returns a shallow copy	
difference()	  -	        Returns a new frozenset with the difference	
intersection()	&	      Returns a new frozenset with the intersection	
isdisjoint()	         	Returns whether two frozensets have an intersection	
issubset()   	<= / <   	Returns True if this frozenset is a (proper) subset of another	
issuperset()	>= / >  	Returns True if this frozenset is a (proper) superset of another	
symmetric_difference()	^	 Returns a new frozenset with the symmetric differences	
union()	|	Returns a new frozenset containing the union	

# Set Methods:-
    Python has a set of built-in methods that you can use on sets.

# Method	    Shortcut       	Description
  add()	                      Adds an element to the set

  clear()	              	    Removes all the elements from the set

  copy()	                  	Returns a copy of the set

  difference()	- 	          Returns a set containing the difference 
                              between two or more sets

  difference_update()	-=	    Removes the items in this set that are also included in another, specified set

  discard()	                 	Remove the specified item

  intersection()	&         	Returns a set, that is the intersection of two other sets

  intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)

  isdisjoint()	   	Returns whether two sets have a intersection or not

  issubset()	<=	Returns True if all items of this set is present in another set

    <	Returns True if all items of this set is present in another, larger set

  issuperset()	>=	Returns True if all items of another set is present in this set

    >	Returns True if all items of another, smaller set is present in this set
    
  pop()	           	Removes an element from the set

  remove()	       	Removes the specified element

  symmetric_difference()	^	Returns a set with the symmetric differences of two sets

  symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another


  union()	   |	Return a set containing the union of sets
  
  update()	 |=	   Update the set with the union of this set and others
