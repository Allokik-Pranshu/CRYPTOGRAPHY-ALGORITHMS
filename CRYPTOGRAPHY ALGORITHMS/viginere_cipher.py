# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 14:30:02 2018

@author: allokik pranshu
"""
a=list(input("enter the plain text: "))
b=list(input("Enter the key: "))
def viginere_cipher(a,b):
    d=[]
    h=0
    for i in a:
        if i==(" "):
            d+=i
        elif (i.isupper()==True):
            k=b[h]
            d+=chr(65+(((ord(i)-65)+(ord(k)-65))%26))
            if h==(len(b)-1):
                h=0
            else:
                h+=1
        else:
            k=b[h]
            d+=chr(97+(((ord(i)-97)+(ord(k)-97))%26))
            if h==(len(b)-1):
                h=0
            else:
                h+=1
    return(d)
c=''.join(viginere_cipher(a,b))
print("The cipher text is: ",c)
