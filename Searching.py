# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 12:51:17 2022

@author: teju3
"""
#Linear search

flag=0
n=int(input())
li=[int(x) for x in input().split()]
no=int(input())
for i in range(len(li)):
    if(li[i]==no):
        flag=1
        print(i)
        break
if(flag==0):
    print("-1")

#Linear search through Functions

def linear_search(lis,no):
    for i in range(len(lis)):
        if(lis[i]==no):
            return i
    return -1

li=[1,2,3,6,5]
index=linear_search(li,5)
print(index)


