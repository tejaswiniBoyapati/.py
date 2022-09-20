# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 17:39:01 2022

@author: teju3
"""

"""
Here, li = 1,2,3,4,5 then,
1 and 5, 2 and 4 , 3 and 3 are swapped
"""


# swapping in  python ---> a,b = b,a

#APPROACH 1:
def reverse_list(li):
    length=len(li)
    for i in range(length//2):
        li[i],li[length-(i+1)] = li[length-(i+1)],li[i]   
        
li=[1,2,3,4,5]
reverse_list(li)
print(li)


#APPROACH 2:
def reverse_list_2(li):
    for i in range(len(li)//2):
        li[-i-1],li[i]=li[i],li[-i-1]
    
li=[1,2,3,4,5]
reverse_list_2(li)
print(li)

#Approach 3

def rev_lis(li):
    li=li[::-1]
    return li

li=[1,2,3,4,5]
li=rev_lis(li)
print(li)

    #OR#
def rev_lis(li):
    print(li[::-1])

li=[1,2,3,4,5]
rev_lis(li)    