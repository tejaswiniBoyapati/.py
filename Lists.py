# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 13:20:45 2022

@author: teju3
"""

#creation of list
li = []  #empty list
print(type(li))
print(len(li))    #size of empty list is 0
li= [1,2,3,"data",3,4]
print(li)

#Access and change elements in list
"""
Accessing of elements is through indexing.
"""
print(li[2])
print(li[-1]) #negative numbering to access from end of the list

"""
changing elements of a list
"""
li[4]="vizualisation"
print(li)

#li[10]="abc"     # error coz size of list li is 6 with 0 to 5 indexes only
#print(li)

#Slicing of a list --  incase u want to access part of a list

print(li[1:3])     #from 1st index to 2

print(li[1:])      #from 1 to last((n-1))

print(li[:])#from 0 to n-1 (complete)

print(li[1:10])   # no inex no. 9 yet from 1 to last is printed

#insert and Append elements in list

"""
by default, append will  create a new index at end and fill up that space with this new value
"""
li.append("Ankush")

print(li)

"""
To insert at some particular index without earsing the previous value , we use insert(index_no,value to be inserted) 
"""
li.insert(1,"hihi")

print(li)

li.insert(100,"hey")   #value inserts at end, as there is no 100th index

print(li)


#list inside list
li.append([9,10,11])

print(li)

#inserting multiple elements into the list at the same time --> extend function

li.extend([9,10,11])

print(li)

# removing elements form the list

li.remove(2)

print(li)

"""
if there are multiple same valued elements, then if we remove that kind of element, then that element from the least ndex will be removed
"""
li.append(4)

print(li)

li.remove(4)

print(li)

#li.remove(1000)  #shows error as there is no value 1000 in list li
#print(li)

#removing element at particular index                            -- pop()
li.pop()   #if no index position is mentioned, then element present at the 

print(li)

li.pop(2)

print(li)

#li.pop(1000)    #error, coz no such index
#print(li)

#looping on lists
"""
1. using range()
2. (a) for i in li:        (direct loop in that list)
   (b)  for i in li[2:]    (slicing part, to start from particular index)
"""
for i in range(len(li)):
    print(li[i])
for i in range(2,len(li)):
    print(li[i])
for x in li:
    print(x)
for x in li[2:]:
    print(x)
    
#negative indexing in list
print(li[-1])  #prints last element
#print(li[-100])  #error coz no such index

# sequencing in list 
"""
li[start:end:step]  by default, start --> 0, end --> len of list , step -->1
"""
print(li[1:5:1])
print(li[1::])  
print(li[::])
print(li[:3]) # --> start = 1, end=2, step =1

#Taking input in list
"""
1. Line separated Input of elements in a List
"""
#EXAMPLE 1:
n=int(input())
lala=[]
for i in range(n):
    curr=int(input())   #int will considered
    lala.append(curr)
print(lala)

#EXAMPLE 2:
n1 = int(input())
lis = []
for i in range(n1):
    lis.append(input())   #input will be in the form of ana integer
print(lis)