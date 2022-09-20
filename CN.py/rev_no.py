# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 00:48:33 2022

@author: teju3
"""

#Write Your Code Here
n=int(input())
rev=0
if(n>=0 and n<=100000000):
    while(n!=0):
        rem=n%10
        rev=rev*10+rem
        n=n//10
    print(rev)

    