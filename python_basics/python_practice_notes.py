'''
This is a basic write up of some of the python stuff we covered
at the RUAutomonous Imaging meeting on Monday, Septmber 30th, 2019

NOTE: the useage of 3 ' to form block comments in python, this can also be done with " 
as long as they are the same for opening and closing the block comment
- single comments can be done with #

'''

#NOTE: when declaring a variable you do not give it a specific type, 
# but you must give it a value
hello = 'apostrophe mark'


#NOTE: the useage of ' ' and " " for strings. There is no diffrence between them
# as long as you use the same for opening anc closing
print(hello)
print("quotation mark")


#NOTE: Indentation in python matters, for conditionals, loops, functions, classes, etc
# you must indent properly so python knows then the grouping starts and ends. 
# you may use spaces or indents but you just keep them consisent throughout the program
# most text editors do this for you, so you do not need to worry about it
# just make to back space out of the groupings and things in the grouping are indented properly

#NOTE: When indentations are used are when the : is used. : indecates the start of a grouping
# this is used in loops, conditionals, functions, classes, etc. 
#you will see them below, so just keep an eye out for them

#NOTE: Sytnax useage below for various statements

x = 5

#NOTE: parenteses can be used for, it does not matter since (True) = True, (False) = False etc.
# they can be useful for order of operations
if x == 5:
	print('x is equal to 5')
if (x == 5):
	print('x is equal to 5')


if x == 4:
	print("x equals 4")

elif x == 3 and x == 5:
	print("x equals 3 and 5?????")

elif x == 3 or x == 5:
	print("x euqals 3 or 5")

else:
	print("x does not queal 4, 3, or 5")


#NOTE: Lists in python. They are dynamically sized arrays
# the objects in the list all dont have to be the same class/type
l = [1, 2, 3, 4, 5, 6]
p = [1, "2", "three", [4], (5), {6}]

print(l)
print(p)

#NOTE: in a for loop, you have an internal variable that you use. That variable here is 
# i, it can be anything you want. That variable is set to the current item in the 
# iterable that you are on.
# - after the "in" , you put an interable. this is what the for loop is interating though

for i in l:
	print(i, end = " ")

print("\n") # this will print an empty line

#NOTE: the len() function will return the lenght of an iterable (list, string, etc.)
# that you give it
list_length = len(l)

#NOTE: the range() function will create a range object that is an iterable from 0 to 
# the integer given -1. eg: range(3) = 0, 1, 2
# range() can be given a staring value like range(1, 3) = 1, 2. 

#NOTE: range() is often used for indexing, you index an iterable by using iterable[index]

for index in range(list_length):
	k = l[index]
	print(k)


#NOTE: this is how you declare a function in python, note the syntax and
# and what is happeing in the function. This will return the legnth of an iterable given
# the return statement will imediatly end the function and anyhting inside of it
# functions dont need to have a return if you dont need to return something

#NOTE: you cannot do int++ or int-- in python, you must do it manually
def length(iterable):
	count = 0
	for i in iterable:
		count += 1
		#same as count = count + 1
	return count

length = length(p)
#NOTE: Printing cannot change the types of the variables, you need to do that mantually
# str() will return a string of the given item
print("The length is: " + str(length))






















