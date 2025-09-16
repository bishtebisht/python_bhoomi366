# list1=["rohan",2,1,"apple","orange"]
# print(list1)
# print(len(list1))

# #list constructor
# list2=list(("rohan",1,2,"hello"))
# print(list2)
# print(type(list2))

# n=0
# while(n!=len(list2)):
#     print(list2[n])
#     n+=1

list1=["rohan",1,3,"apple","orange","hello"]
# print(list1[2:5])
# print(list1[-4:-1])
#same output
# [3, 'apple', 'orange']
# [3, 'apple', 'orange']

# if "apple" in list1:
#     print("yes")
 
# modifying elements   
list1[0]="bhoomi"
print(list1)
#['bhoomi', 1, 3, 'apple', 'orange', 'hello']

list1[1:3]=[16,"may"]
print(list1)
#['bhoomi', 16, 'may', 'apple', 'orange', 'hello']

list1.insert(5,"mango") #insert mango at index 5 and shift rest elements 
print(list1)
#['bhoomi', 16, 'may', 'apple', 'orange', 'mango', 'hello']

#append->add at last
list1.append("world")
print(list1)
#['bhoomi', 16, 'may', 'apple', 'orange', 'mango', 'hello', 'world']

#extend
list2=["pink","blue",7]
list1.extend(list2)
print(list1)
#['bhoomi', 16, 'may', 'apple', 'orange', 'mango', 'hello', 'world', 'pink', 'blue', 7]

#remove
list1.remove("orange")
print(list1)
#['bhoomi', 16, 'may', 'apple', 'mango', 'hello', 'world', 'pink', 'blue', 7]

#pop
list1.pop(3)
print(list1)
#['bhoomi', 16, 'may', 'mango', 'hello', 'world', 'pink', 'blue', 7]
