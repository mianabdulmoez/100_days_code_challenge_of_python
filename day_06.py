#Every thing in python is object    
#Data types
# Variable is a container that hold data
# variable store in ram
#There are also some data types

#String is always enclosed in " ". like "a","69"
a ='Abdul Moeez' #This is string data type
print(a)
print(type(a))
a1 = "69"
print(type(a1))

#Boolean is always True or False.It no need this " "
b = True #This is boolean data type
print(b)
print(type(b))

#There are 2 type of number.
# 1 is integer which is a number without decimal point
c=69 #This is integer data type
print(c)
print(type(c))

# 2 is Float which is a number usind a decimal point
d = 1.1000 #This is float data type
print(d)
print(type(d))

mian = 96 #This is also integer data type
f = mian
print(f)
print(type(f))

#Complex is a tpye which is contain on 1 real number & imaginary number
g = complex(8,2)#This is complex data type
#So here 8 is real number and 2 is imaginary number
print(g)



# Sequenced data: list, tuple, dict, set
# list: 
# A list is an ordered collection of data with elements separated by a comma and enclosed within square brackets.
# Lists are mutable and can be modified after creation.
# List is also changeable
# List can be contain on any data type
list = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list)

# Tuple:
# A Tuple is an ordered collection of data with elements separated by a comma and enclosed within paranthesis.
# Tuple are imutable and can be modified after creation.
# Tuples can not be changeable
# Tuple would be also contain on any data type
tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)

# Dict:
# A dictionary is an unordered collection of data containing a key:value pair. The key:value pairs are enclosed within curly brackets.
dict1 = {"name":"Sakshi", "age":20, "canVote":True}
print(dict1)
