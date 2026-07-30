print("Hello, World!")
print(2+2)
#here nothing gets exicuted when I press enter. 
#how can I run this code? 
#two ways: 
#1. You can put the caret on the line and press shift + enter. 
# It is going to send the line to a REPL and run it. 
print("Hello, World!")
# the second way is to run the whole file.
# send the entire content of the file to Python and all of the lines will be exicuted in sequence. 
# press the run botton at the top right of the central panel. 
# you will want to do this when you have finnished writing your script. 

# reminder 1: we  can create bibles in python and assign content to them 
name = "Alice"
print(name) # this is printing the content of the bible
# let's send line 16 (print) to the REPL. 
# I get a name error because the variable name is not defined in the REPL.

# four big types of data in python: 
# 1. Strings (text) = "Hello, World!"
# 2. Integers (whole numbers) = 10 
# 3. Floats (decimal numbers) = 10.5
# 4. Booleans (True or False) = True

# print using the print function.
print("Hello, World!") # this is a string
print(2+2) # this is an integer
print(10.5) # this is a float
print(True) # this is a boolean
# we can print multiple things at once, seperated by a comma. 
print("Hello, World!", 2+2, 10.5, True)
# print() is somthing called a function. A function is something that takes between 0 and 
# many arguments that has a specific behavior. It is an actionIn this case, the print function takes any number of arguments and prints them to the console.

#you can print:
# A value: 
print(3.14)
print("Hello, World!")
# A variable:
name = "Alice"
print(name)
# An expression:
print(2+2)  
# reminder: expressions are calculated 'inside out' 
# SKILL: when reading code, try to understand what is happening in which order. Tracing code

# how do you figure out the type of a variable?
# you can use the type() function to figure out the type of a variable.
print(type(name)) # this is a string
print(type(2+2)) # this is an integer
print(type(10.5)) # this is a float
print(type(True)) # this is a boolean   

#calculations in python:
print(2+3)
print( 2 + 3 * 4) # this is an expression, it is calculated 'inside out'
print( (2 + 3) * 4) # this is an expression, it is calculated 'inside out' PEMDAS 

print(1+2)
print((1+2) == 3) # logical comparisions always return a boolean value.
print(0.1 + 0.2) #WTF?
print((0.1 + 0.2) == 0.3) #WTF?
# this is a floating point error. very very common in data science. Do not expect floats to be exact. 
# what can you do? 
my_rouded_value = round(0.1 + 0.2, 1) # function takes two arguments round to 1 decimal place
print(my_rouded_value) # functions take multiplal arguments a lot. 
round(3.14) #functions can have non-complorsy this will round to 0 since nothing is specified. 

#logical comparisons 
print(5 > 3) # this is true greater
print(5 < 3) # this is false less 
print(5 == 5) # this is true equeal
print(5 != 5) # this is false  not equeal

#you can combine logical comparisons with logical operators.
# logical operators: and, or, not
print(5 > 3 and 5 < 10) # this is true
print(5 > 3 or 5 < 10) # this is true
print(not 5 > 3) # this is false
condition_1 = True 
condition_2 = False
condition_3 = True
condition_4 = False
print(condition_1 and condition_2) # this is false
print(condition_1 or condition_2) # this is true
print(condition_1 and condition_3) # this is true
print(condition_2 or condition_4) # this is false
print(condition_1 and condition_2) # false 
#and only returns true if both conditions are true.
# or returns true if at least one condition is true.

#lets do a few more calculations. 
print(True + True) # true are 1 and false are 0 so 1+1
print(True == 1) # this is true
print(True * 5) # this is 5
print(10/0) # this is an error, you cannot divide by 0.
print(10/False) # this is an error, you cannot divide by 0.
print(10/True) # this is 10, because True is 1.

#lets do some strings manipulation.
print("Hello, World!") # this is a string
print("Hello, " + "World!") # this is string concatenation
print("Hello, " * 3) # this is string repetition
greeting = "Hello, World!"
print(greeting)
print("hello * 8.9") # this is an error be careful mixing different types 
very_complicated_laugh = "ha" * ("hello" == "hello") * 3 # this is string repetition
print(very_complicated_laugh) # this is "hahaha" because "hello" == "hello" is True which is 1 so "ha" * 1 * 3 is "hahaha"
# dont do this line before keep things simple (stupid)

#how do we keep things simple?
# we can use variables to store values and then use those variables in our calculations.
#make sure to convert variables before working with them. 
number = 42
is_this_a_number = '42'
print(number + int(is_this_a_number)) # this is 84 because we converted the string
# str turnes something that is not a string into a string 
# int turns something that is not an integer into an integer
int('fifteen') # this is an error because 'fifteen' is not a number
int('15') # this is 15 because '15' is a number
int(False) # this is 0 because False is 0
int(True) # this is 1 because True is 1
str(42) # this is '42' because we convert the integer to a string

# one more example
my_age = 30
my_age_in_5_years = my_age + 5
print(my_age_in_5_years) # this is 35
my_name = "Jameson"

my_intro = f"Hello, my name is {my_name} and I am {my_age} years old."
print(my_intro) # this is "Hello, my name is Jameson and I am 30 years old."

#str, #float, #int, #bool are all data types in python. Can turn input into desired data type if possible. 

