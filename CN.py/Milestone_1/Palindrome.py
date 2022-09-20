# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 00:54:58 2022

@author: teju3
"""

"""
n=int(input())
temp=n
rev=0
while(n!=0):
    rem=n%10
    rev=rem+rev*10
    n=n//10
if(temp==rev):
    print("Palindrome")
else:
    print("No")
    
"""
def checkPalindrome(num):
#Implement Your Code Here
    rev=0
    s=num
    while(num!=0):
        rem=num%10
        rev=rev*10+rem
        num=num//10
    if(s==rev):
        return True
    else:
        return False
		
num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome):
	print('true')
else:
	print('false')

