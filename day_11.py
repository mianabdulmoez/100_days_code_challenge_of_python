# String
# Anything that you enclose between single or double quotation marks is considered a string. 
# A string is essentially a sequence or array of textual data. 
# Strings are used when working with Unicode characters.
name =  "Abdul Moeez"
name2 = "David Jhonsan"
name3 = 'Brain Dean'#We can enclose string in a single quation mark
print(name,name2,name3, sep=", ")#Here we use seprator function to seprate the different strings

# Printing " doble quation mark in string
# apple = "He said, "I want to eat an apple" => This cant be print because of double quation mark in mark
apple = "He said, \"I want to eat an apple"#We use escape sequence to print doble quation mark in string
apple = 'He said, \"I want to eat an apple'#Here we use single quation mark to print double quation mark in string
print(apple)
# Printing \ back slash in string using escape sequnce method
apple1= "He said, \I want to eat an apple"#We can print it like that \
apple1= "He said, \\I want to eat an apple"#we can print it using escape sequnce \\
apple1 = 'He said, \\I want to eat an apple'
print(apple1)

# Printing MultiLine string
# This can be print with """double quation triple mark """
# This can be print with '''single quation triple mark '''
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

# String Indexing
# Indexing starts from ascending to descending
name = "Abdul Moeez"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
# Here i remove[5] because it is a space in Abdul Moeez
print(name[6])
print(name[7])
print(name[8])
print(name[9])
print(name[10])
# print(name[11]) This throw an index error
# The error which come from use indexing is index error. This said there is no more number to index 
print(name[0:])#Here we strat from 0 to so on 
print(name[0:100])#Here we strat from 0 to so on mean there is no limitation in indexing 
print(name[0:4])#Here we can see it exclude 4 and limit it to 3
print(name[0:5])
print(name[0:10])#Here we can see it exclude 10 and limit it to 9
print(name[0:11])
print(name[6:11])
print(name[11:6])
# Negative indexing
# Negative indexing always is Descending
print(name[-11:-1])#so here it aslo exclude -1 which is z
print(name[-1:-12])#It show nothing

# Using loop in string indexing
print("let's use a for loop in string \n")
for i in name:#Here I am declaring name to 'i' and loop using on 'i'
    print(i)#Here I am printing 'i' which come from name variable 
