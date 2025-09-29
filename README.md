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
    Parameter	Description
    value	Required. The value to search for
    start	Optional. Where to start the search. Default is 0
    end	Optional. Where to end the search. Default is to the end of the string

     
    format()	Formats specified values in a string
    format_map()	Formats specified values in a string
    index()	Searches the string for a specified value and returns the position of where it was found
    isalnum()	Returns True if all characters in the string are alphanumeric
    isalpha()	Returns True if all characters in the string are in the alphabet
    isascii()	Returns True if all characters in the string are ascii characters
    isdecimal()	Returns True if all characters in the string are decimals
    isdigit()	Returns True if all characters in the string are digits
    isidentifier()	Returns True if the string is an identifier
    islower()	Returns True if all characters in the string are lower case
    isnumeric()	Returns True if all characters in the string are numeric
    isprintable()	Returns True if all characters in the string are printable
    isspace()	Returns True if all characters in the string are whitespaces
    istitle()	Returns True if the string follows the rules of a title
    isupper()	Returns True if all characters in the string are upper case
    join()	Joins the elements of an iterable to the end of the string
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
    split()	Splits the string at the specified separator, and returns a list
    splitlines()	Splits the string at line breaks and returns a list
    startswith()	Returns true if the string starts with the specified value
    strip()	Returns a trimmed version of the string
    swapcase()	Swaps cases, lower case becomes upper case and vice versa
    title()	Converts the first character of each word to upper case
    translate()	Returns a translated string
    upper()	Converts a string into upper case
   
 zfill()	Fills the string with a specified number of 0 values at the beginning
 # (eg):-
    txt = "50"

    x = txt.zfill(10)

    print(x)