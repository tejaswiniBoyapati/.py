# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 01:08:40 2022

@author: teju3
"""

## Read input as specified in the question.
## Print output as specified in the question.
#recursive approach
n=int(input())
a=1
b=1
count=2
if (n==1):
    print(a)
elif (n==2):
    print(b)
else:
    while(count<n):
        d=a+b
        a=b
        b=d
        count=count+1
    print(b)