# This is my introduction to programming. I have no previous programming experience.
# Created using multiple sources including: tutorialspoint.com; python-course.eu; w3schools.com; Corey Schafer's YouTube tutorial. I do not mean to infringe any copyright laws, this file was compiled to put all of the knowledge required in one place. If there's any issue with the copyrights, please message me and I will delete requested data immediately.
# Using Visual Studio Code on Windows machine, using better comments extension for better visuals
# Word wrap is set.
# Git https://github.com/WarGamezz/python_intro


# comment

'''
This is a multiline
comment.
'''

#! There is no declaration of variables required in Python. It's not even possible. If there is need of a variable, you think of a name and start using it as a variable. 
#!Not only the value of a variable may change during program execution but the type as well. You can assign an integer value to a variable, use it as an integer for a while and then assign a string to the same variable. The following code is perfectly okay

x = 42			# data type is implicitly set to integer
print(x)
x = 42 + 0.11		# data type is changed to float
print(x)
x = "forty"		# and now it will be a string  
print(x)
y=x # now x and y are reference to the same object -> "forty"
#Python variables are references to objects, but the actual data is contained in the objects. In this case both x and y are reference to the same object. You can prove it using identity function id() 
print(id(x))
print(id(y))

#! Python allows you to assign a single value to several variables simultaneously.
a = b = c = 1 #all 3 variables will have value of 1
a, b, c = 1, 2, "john" # will assign a=1, b=2, c="john"

#! variables / identifiers name convention. Python 3.x is based on Unicode. That means that variables can use upper case letters, lower case letters, no spaces (use underscore instead), numbers 0-9 and Unicode characters. No identifier can have the same name as one of the Python keywords! You can find them using help() -> keywords
# and, as, assert, break, class, continue, def, del, elif, else, except, False, finally, for, from, global, if, import, in, is, lambda, None, nonlocal, not, or, pass, raise, return, True, try, while, with, yield. 

#! number variables
#Integer - whole number; a number that is not a fraction.
#Floating-point numbers - representation of real numbers as an approximation so as to support a trade-off between range and precision
#Complex - written as <real part> + <imaginary part>j

#? integer division
#"true division" performed by "/" - standard division
x = 10 / 3 
print(x)
x = 10.0 / 3.0
print(x)
x = 10.5 / 3.5
print(x)

#"floor division" performed by "//" - floor of the result will be returned. The floor is the largest integer number smaller than the result of the true division. This number will be turned into a float, if either the dividend or the divisor or both are float values. If both are integers, the result will be an integer as well. In other words, "//" always truncates towards negative infinity. 

x = 9 // 3
print(x)
x = 10 // 3
print(x)
x = 11 // 3
print(x)
x = 12 // 3
print(x)
x= 10.0 // 3
print(x)

#! string variables
#There are different ways to define strings in Python:
string1 = 'I am a string enclosed in single quotes.'
print(string1)
string2 = "I am another string, but I am enclosed in double quotes"
print(string2)
#Single quotes will have to be escaped with a backslash (\), if the string is defined with single quotes:
string3 = 'It doesn\'t matter!'
print(string3)
#This is not necessary, if the string is represented by double quotes:
string4 = "It doesn't matter!"
print(string4)
#Analogously, we will have to escape a double quote inside a double quoted string:
string5 = "He said: \"It doesn't matter, if you enclose a string in single or double quotes!\""
print(string5)
#They can also be enclosed in matching groups of three single or double quotes. In this case they are called triple-quoted strings. In triple-quoted strings, unescaped newlines and quotes are allowed (and are retained), except that three unescaped quotes in a row terminate the string.
string6 = '''A string in triple quotes can extend
over multiple lines like this one, and can contain
'single' and "double" quotes.'''
print(string6)
#A string in Python consists of a series or sequence of characters - letters, numbers, and special characters. Strings can be subscripted or indexed. Similar to C, the first character of a string has the index 0.
string7 = "Hello World"
print(len(string7))
#The last character of a string can be accessed like this:
print(string7[len(string7)-1])
#Yet, there is an easier way in Python. The last character can be accessed with -1, the second to last with -2 and so on:
print(string7[-1])

#?operators and functions for strings
#Concatenation - Strings can be glued together (concatenated) with the + operator:
string8 = "Hello "
string9 = "world"
string10 = string8 + string9
print(string10)
#Repetition - String can be repeated or repeatedly concatenated with the asterisk operator "*":
string11 = "HI "
print(string11 * 3)
#Indexing & slicing - Individual index, as well index ranges can be accessed using [x:y]; print(var[x:y]), x is inclusive, y is not you can also use print(var[x:]) = from x to infity or print(var[:y]) - upto x, first index = 0
string12 = "Hello world"
print(string12[0]) #prints first character (index 0)
print(string12[4:7]) #prints characters 3,4,5 (index 4,5,6)
print(string12[3:]) #prints characters from 2 (index 3) to infinity
print(string12[:7]) #prints characters from first to the 6th (indexes 0-7)
#Size - the length of the string in python (in index value) can be accessed using len(string):
print(len(string12))

#? Like strings in Java and unlike C or C++, Python strings cannot be changed. Trying to change an indexed position will raise an error. You can change the entire object but not individual characters:

string13 = "Some things are immutable!"
print(string13)
string13[-1] = "." # you cannot replace individual character (in this case replace ! with the .). You can however replace the entire string
string13 = "But you can re-define the entire string object." # this will work just fine since the entire object is replaced
print(string13) 

#! Escape Sequences in Strings
#The backslash (\) character is used to escape characters, i.e., to "escape" the special meaning, which this character would otherwise have. Examples for such characters are newline, backslash itself, or the quote character. String literals may optionally be prefixed with a letter 'r' or 'R'; these strings are called raw strings. Raw strings use different rules for interpreting backslash escape sequences. 
# \\	Backslash (\)
print('This is how you youse backslash \\ in the string without actually escaping anyting')
# \'	Single quote (')
print('This is how you escape single quote\'s and still finish the string')
# \"	Double quote (")
print("This is how you escape \"double quote\" and still finish the string")

#\n adds a new line
print("Hello","\n","world")

#! Python lists
#The values stored in a list can be accessed using the slice operator ([ ] and [:]) with indexes starting at 0 in the beginning of the list and working their way to end -1. The plus (+) sign is the list concatenation operator, and the asterisk (*) is the repetition operator.

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print (list)          # Prints complete list
print (list[0])       # Prints first element of the list
print (list[1:3])     # Prints elements starting from 2nd till 3rd 
print (list[2:])      # Prints elements starting from 3rd element
print (tinylist * 2)  # Prints list two times
print (list + tinylist) # Prints concatenated lists

#in list you can update individual item on the list
list[2] = "Hello"
print (list) 

#! Python Tuples
#A tuple consists of a number of values separated by commas. Unlike lists, however, tuples are enclosed within parenthesis. The main difference between lists and tuples are − Lists are enclosed in brackets ( [ ] ) and their elements and size can be changed, while tuples are enclosed in parentheses ( ( ) ) and cannot be updated. Tuples can be thought of as read-only lists.

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')
print (tuple)           # Prints complete tuple
print (tuple[0])        # Prints first element of the tuple
print (tuple[1:3])      # Prints elements starting from 2nd till 3rd 
print (tuple[2:])       # Prints elements starting from 3rd element
print (tinytuple * 2)   # Prints tuple two times
print (tuple + tinytuple) # Prints concatenated tuple

#trying to update individual tuple will result in an error
tuple[2] = "Hello"

#! Python Dictionary
#Python's dictionaries are kind of hash-table type. They work like associative arrays or hashes found in Perl and consist of key-value pairs. Dictionaries are enclosed by curly braces ({ }) and values can be assigned and accessed using square braces ([]). Dictionaries have no concept of order among the elements. It is incorrect to say that the elements are "out of order"; they are simply unordered.

dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values

#! Data Type Conversion
int(x [,base]) #Converts x to an integer. The base specifies the base if x is a string.
float(x) #Converts x to a floating-point number.
complex(real [,imag]) #Creates a complex number.
str(x) #Converts object x to a string representation.
repr(x) #Converts object x to an expression string.
eval(str) #Evaluates a string and returns an object.
tuple(s) #Converts s to a tuple.
list(s) #Converts s to a list.
set(s) #Converts s to a set.
dict(d) #Creates a dictionary. d must be a sequence of (key,value) tuples.
frozenset(s) #Converts s to a frozen set.
chr(x) #Converts an integer to a character.
unichr(x) #Converts an integer to a Unicode character.
ord(x) #Converts a single character to its integer value.
hex(x) #Converts an integer to a hexadecimal string.
oct(x) #Converts an integer to an octal string.