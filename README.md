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
The Python print() function is often used to output variables.