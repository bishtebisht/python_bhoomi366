# i=1
# print(type(i))
# print(id(i))

#multiple variable
# a,b,c=1,2,3
# print(a,b,c)

# print(id(a))
# print(id(b))
# print(id(c))

# a=b=c
# print(id(a))
# print(id(b))
# print(id(c)) #(same as c)

#variable name-
# 1-camel style:- myVariable
# 2-snake style:- my_variable
# 3-pascal style:- MyVariable

# NUMERIC DATATYPE
# var1=1   
# var2=True
# var3=10.08
# var4=10+9j

# print(type(var1))
# print(type(var2))
# print(type(var3))
# print(type(var4))

# OUTPUT
# <class 'int'>
# <class 'bool'>
# <class 'float'>
# <class 'complex'>

#STRING DATATYPE
#(multiline string)
# print("hello world")
# a="""name-Bhoomi Bisht
# course-Btech
# branch-CSE"""
# print(a)

# #in
# print("Btech" in a)  #True
# if "Bhoomi" in a:
#     print("yes")
# else: 
#     print("no")

# print("yes" not in a)

# str="Hello"
# print(str[:])
# print(str[2:4])
# print(str[2:])
# print(str[:4])
# print(str[-4:-2])
#hello
# ll
# llo
# hell
# el
# print(str.upper())  #HELLO
# print(str.lower())  #HELLO

# a=" bhoomi "
# print(a.strip()) #removes spaces

# #replace
# print(a.replace("Hello","bhoomi"))

# a="Hello, world"
# print(a.split(","))  #['Hello', ' world']
# a="Hello world, bhoomi here"
# print(a.split(","))  #['Hello world', ' bhoomi here']
#here "," works as a seperator

#string concatenation
# a="hello"
# b="world"
# c=a+" "+b
# print(c)   #hello world

# #format-strings (F-string)
# age=19
# t=f"my name is bhoomi,I am {age}"
# print(t)

# price=12.5567
# txt=f"the price is {price:.2f} dollar"
# print(txt)

# output
# my name is bhoomi,I am 19
# the price is 12.56 dollar

#Escape character-to insert characters that are illegal in a string(backlash-\)
#for eg- using double quote inside a string surrounded by double quote
# txt="we are the so-called \"vikings\" from the north."
# print(txt)    #we are the so-called "vikings" from the north.

#Boolean-(True or False)
# print(10>9)           # True
# print(10<9)           # False
# print(bool("hello"))  # True
# print(bool(10))       # True
# print(bool(0))        # False

# #function returning boolean
# def fun():
#     return True

# if fun():
#     print("yes")
# else:
#     print('no')

#SEQUENCE DATA TYPES- LIST , TUPLE , RANGE
 
#list
l=["bhoomi",19,"16-may-2006","BTech"]
tiny_l=["CSE",14]
print(type(l))
print(l)
print(l[0])
print(l[1:3])
print(l[2:])
print(tiny_l *2)
print(l+tiny_l)
#output
# <class 'list'>
# ['bhoomi', 19, '16-may-2006', 'BTech']
# bhoomi
# [19, '16-may-2006']
# ['16-may-2006', 'BTech']
# ['CSE', 14, 'CSE', 14]
# ['bhoomi', 19, '16-may-2006', 'BTech', 'CSE', 14]

#tuple
tup=("abcd",789,4.56,"john",20+8j)
tiny_tup=(123,"hello")
print(type(tup))
print(tup)
print(tup[0])
print(tup[1:3])
print(tup[2:])
print(tiny_tup *2)
print(tup+tiny_tup)
#output
# <class 'tuple'>
# ('abcd', 789, 4.56, 'john', (20+8j))
# abcd
# (789, 4.56)
# (4.56, 'john', (20+8j))
# (123, 'hello', 123, 'hello')
# ('abcd', 789, 4.56, 'john', (20+8j), 123, 'hello')

#range(start,stop,step)
for i in range(5):
    print(i)   #01234

for i in range(1,10,2):
    print(i)   #13579