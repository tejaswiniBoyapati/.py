# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 01:07:26 2022

@author: teju3
"""

n=int(input())
s=n
sum_odd=0
sum_even=0
while(n!=0):
    rem=n%10
    if(rem%2!=0):
        sum_odd=sum_odd+rem
    else:
        sum_even=sum_even+rem
    n=n//10
print(int(sum_even), " ", int(sum_odd))