# we have been using functions from day 1 (or almost):
# print(), type(), str(), float(), int(), bool(), len()
len('quentin') #number of elements in a string, or sequence. 

#what is a function?

# a function is like a machine: It does somthing. 
# it usually takes one or more inputs and usually returns a result

# print() what does it take? it takes any expression that we want to print
#what does it do? It prints stuff to the user 

#str() = what does it take? 
# It takes any expression 
str(False)
#what does it do? It turnes it into a string, and returns it to the user. 

#what does it mean to return something? 
#lets take print() as an example
print('1234') # it is going to print 1234 in the terminal 
my_content = print('1234')
my_content # my content is empty, print('1234') did not store anything in it

#most functions return something, think of them like a convator belt, 
# they are going to take an objectd and take waht it did onb the other side of the machine

# other functions are just doing stuff; think of them like an engine
#you ARE GOING to put seome gas into them, they are going to do something
# but they are not going to hand you back anything 

#lets write functions together to better understand this distinction. 
# we are going to write a functio;n that takes a price, a rate, and returns
# the price updated with the rate

# how do we create a new function? We use this syntax; 
def print_total(price, rate): # def, followed by function name, parenthesis (arguments)
    # you will see that your curser moved to the right: 
    #this defines the body of the function, every piece of code inside defines what the function will do
    total = price * (1+rate)
    print(total)

calculate_total(10, 0.1)

#same functions take a cariable number of arguments. 
round(3.14) #here the second argument is not composolory. It has a default and it is zero 
print("abc") #print abc
print('abc', 'def', 'ghi')
#print is an example of a function that takes an abratary number of arguments. 
#you can give as many as you want, and its going to print them all

order_id = '1042'
units = 12
price = 3.99

print(type())