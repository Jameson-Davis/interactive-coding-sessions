this_is_an_intiger = 10
this_is_a_string = "Hello, World!"
type(this_is_an_intiger) # this is an integer
type(this_is_a_string) # this is a string
#everything you create in python is an object. Objects have methods and attributes. Methods are functions that belong to an object. Attributes are variables that belong to an object.
#an object is a bundle of many things. 

#after creating a variable in puython, you can check all the things
#that are contained in that variable using the .dot in VScode
#after you press dogt, it will reveal a list of things contained in the object. 
#These things come in two flavors
# PROPERTIES: are signaled by the wrench icon, contains information data. 
# METHODS: decribed by the purple box, decribes all actions that can be preformed by the object. 
this_is_an_intiger.numerator
this_is_an_intiger.denominator
this_is_an_intiger.real
#properties are decribing the state of the object that we created. 
another_intiger = 10
print(another_intiger.numerator) # this is an integer
print(another_intiger.denominator) # this is an integer
#can we check some properties of a string?
print(this_is_a_string.upper()) # this is a string
print(this_is_a_string.lower()) # this is a string
print(this_is_a_string.capitalize()) # this is a string

#what is really useful are methods, methods allow us to do stuff with the objects we created. 
#they are like a function in that they can do things, but they are attached (bound) to the object.
#examples of methods for this is a string
this_is_a_string.upper() # a methods requires parentheses because they are actions likea a function. 
#calling a function calling a method
#all objects of a given type have the same methods. 

my_str = "Hello, World!"
my_str.endswith("!") # this is a method that checks if the string ends with a certain character.
#some objhects have other things than methods: properties are only mennt to read they dont do anything
#strings contain a lot of methods 
#because there are a lot of things that we can do with them
#we've already seen upper(), lower(), and capitalize() methods.
my_sentence = "this is a sentence."
my_sentence.title() # this is a method that capitalizes the first letter of each word in the string.
lots_of_white_space = "     this is a sentence with lots of white space.     "
lots_of_white_space.strip() # this is a method that removes whitespace from the beginning and end of the string.
#let me show you a practical example of how methods can be used to manipulate strings.
entry = "     this is a sentence with lots of white space.     "
#we can use the strip() method to remove the whitespace from the beginning and end of the string.
entry = entry.strip()
#I want to check if this person has a .edu email address
is_it_edu = entry.endswith(".edu")
print(is_it_edu) #it is false becaause of the white space
is_it_edu = entry.strip().endswith(".edu") #this is a method chaining, we can call multiple methods on the same object.
print(is_it_edu) #it is false because of the white space

#this is called chaining. You will call methods on an object that is returned by another method.

#a few more exploration
#so far we have seen the four big types of objects in python: integers, floats, strings, and booleans.
# in python, you are often going to create other jobjects 
# let me show you one object that is going to solve a problem we had before 

from decimal import Decimal #not seen yet, soon! dont worry 
#what is decimal? It is a factory for manufactoring a new type of object called a Decimal.
#we can use the Decimal object to create decimal numbers that are more accurate than floats.
my_decimal = Decimal("0.1") #this is a decimal object
print(my_decimal) #this is a decimal object
# to create a str you only need to put quotes around soemthing 
# to create a float or an int, you just needed to type a float or an int
# to create a boolean, you just needed to type true or false, or have a logical condition

#to create decimal objects, we are going to use teh decimal triangle we just imported
a = Decimal("0.1")
# we hvae created a new decimal object with the value of 0.1. We can use this object to do math with other decimal objects.
b = Decimal("0.2")
type(a) #this is a decimal object
c = a + b
print(c) #this is a decimal object
# this is because, by default, python represents floats with a limited number of zeros. 
print(a+b) # if you print the sum of two decimal objects, you get the exact number. 
# decimal objects were created to do exact representations. 
# thats the problem that decimal is solving. 

# if you reach into a decimal object with a dot, you are going to see a lot of new methods and properties. 

