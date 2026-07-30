count = 0 
while count < 5: 
    print(count)
    count = count + 1 

#A while loop is going to exicute as long as the condion is true. 
# As soon as the condition becomes false, it will no longer run. 
# A very common use case in the while loop is to wait until some condition becomes true.

user_input = ""
while user_input == "":
    user_input = input("Please enter something:")

print("You entered" + user_input)

#lets use a while loop to process a to do list 
to_do = ["laundry", "dishes", "yard cleaning", "dog washing"] # initialization 
while len(to_do) != 0:
    task = to_do.pop()
    print("now I'm doing this:" + task)



# remember a while loop is something that chekc sif something is true and runs until its true
# 
# what is a for loop
# it is something that ITERATES on a object, and runs as many times as the number of elements in the objects

for number in [1, 2, 3, 4, 5]:
    print(f"The number is {number}")

for letter in "Quentin": 
    print(letter)

#We can do more complicated things 
list_of_numbers = [1, 2, 3, 4, 5]
for number in list_of_numbers:
# this is my code