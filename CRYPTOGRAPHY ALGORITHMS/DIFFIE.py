# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 15:11:31 2018

@author: ALLOKIK PRANSHU
"""
def generator(p):
    for i in range(2,p):
        s=set()
        for j in range(0,p):
            o=(i**j)%p
            s.add(o)
        if len(s)==p-1:
            return(i)
        
        
def public_key(m,n,p):
    x=(n**m)%p
    return(x)


def shared_secret(a,y,p):
    ssk=(y**a)%p
    return(ssk)
    

p=int(input("Enter any prime no.: "))
g= generator(p)
a=int(input("ALICE, enter your private no. a ; a<p: "))
print("The public key of ALICE is: ",public_key(a,g,p))
b=int(input("BOB, enter your private no. b ; b<p: "))
y=public_key(b,g,p)
print("The public key of BOB is: ",y)
print("The shared secret is: ",shared_secret(a,y,p))