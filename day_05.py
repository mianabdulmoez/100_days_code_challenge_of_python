# Escape sequence charaters
print("Hello")

# print("Hey, How are you,
#  buddy") This can't be print 

# Now here use escape sequence

print("Hey, How are you,\nbuddy")
# here we use backslash \ and n this is new line escape sequence

print("Hey, How are you,\n\tbuddy")
# here /t is space tab which give sapce before buddy

# print("Hey, I am "Abdul Moeez",How are you my buddy")
# I had to highlight my name in this ""
print("Hey, I am \"Abdul Moeez\",\nHow are you my buddy")
# here \this\ use for highlighting \n this is new line

''' This is multi line comment'''
"""This also a multi line comment"""
print("hello",69,96,  sep="~")
# this is use in next line
print(end="69")
print("hi")
# instead
print("hello",69,96,  sep="~", end="11")
print("hi")
# But We can use it like that
print("hello",69,96,  sep="~", end="11\n")
print("hi")