# #SQUARE
# n=int(input("enter a number: "))
# print(f"the square of {n} is",n**2)

# #print sum of two number
# a=int(input("enter number 1: "))
# b=int(input("enter number 2: "))
# print("sum= ",a+b)

# #swapping
# print("value of a and b before swapping: ",a,b)
# a,b=b,a
# print("value of a and b after swapping: ",a,b)

# #number guessing game
# i=4
# x=int(input("guess the number:"))
# if(x==i):
#     print("u guessed it right!!")
# else:
#     print("u guessed it wrong!!")
        
# #even/odd
# if(n%2==0):
#     print(f"{n} is an even number")
# else:
#     print(f"{n} is an odd number")

#temperature
# c=int(input("enter the temp in celsius: "))
# print(f"temperature in farenheit: {c*(9/5)+32}")

# #type
# a=9
# b=3.4
# c="hello"
# print(f"a vairiable type: {type(a)} \nb variable type: {type(b)} \nc variable type: {type(c)}")

# #simple interest
# p=int(input("enter the principle amount:"))
# r=int(input("enter te rate:"))
# t=int(input("enter the time:"))
# print(f"Simple interest: {p*r*t/100}")

#reverse a string
str=input("enter a string")
n=len(str)

for i in range (0,n/2,1):
    temp=str[len-1]
    str[len-i]=str[i]
    str[i]=temp
    
