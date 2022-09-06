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


