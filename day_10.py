# User input
# Input() standard function always come with string
# a = input()
# print(a)

x = input("Enter First Value = ")
y = input("Enter Second Value = ")
# Here we dont define the data type so this is concatination as a string
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x ** y)
print(x // y)
print(x % y)
# From here we can see that string can only be add noting other operation can be performed on string

# Here we define the data type is integer so it operate the number as numeric
print(int(x) + int(y))
print(int(x) - int(y))
print(int(x) * int(y))
print(int(x) / int(y))
print(int(x) ** int(y))
print(int(x) // int(y))
print(int(x) % int(y))

# We can also write it like that
x = int(input("Enter First Value = "))
y = int(input("Enter Second Value = "))
# Here user can only type integer nothing else
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x ** y)
print(x // y)
print(x % y)

# Let's Play with this Function
name = str(input("Enter your name :"))
print("Hello,",name)
# age = int(input(name,"Enter your age :")) it show error through name because it is in input which is int but name is string
# age = int(name,input("Enter your age :")) This is alo in integer data type
age = name,int(input("Enter your age :"))
# So here i make print function into a variable thats why is not running
# print = ("You are",age)
# print = (name,"You are too young")
print("You are",age)
print(name,"You are too young")
