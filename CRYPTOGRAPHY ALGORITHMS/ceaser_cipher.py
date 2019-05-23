# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 14:05:01 2018

@author: allokik pranshu
"""

a=list(input("enter the plain text: "))
b=int(input("Enter the shift: "))
def ceaser_cipher(a,b):
    d=[]
    for i in a:
        if i==(" "):
            d+=i
        elif (i.isupper()==True):
            d+=chr(64+((ord(i)-64+b)%26))
        else:
            d+=chr(96+((ord(i)-96+b)%26))
    return(d)
c=''.join(ceaser_cipher(a,b))
print("The cipher text is: ",c)