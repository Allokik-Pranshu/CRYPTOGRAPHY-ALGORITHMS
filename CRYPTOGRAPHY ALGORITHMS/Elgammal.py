# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 19:45:42 2019

@author: ALLOKIK PRANSHU
"""
import random

def rand(p):
    a=random.randint(2,p-2)
    return(a)


def generator(p):
    for i in range(2,p):
        s=set()
        for j in range(0,p):
            o=(i**j)%p
            s.add(o)
        if len(s)==p-1:
            return(i)
    
def key_generation(p):
    g=generator(p)
    a=rand(p)
    x=(g**a)%p
    print("your randomly generated keys are as follows: ")
    print("Public key: ",g ," , ", p ," , ", x )
    print("Private key: ",g ," , ", p ," , ", a )
    
def encryption_elg(r,g,p,x):
    k=rand(p)
    q=(g**k)%p
    y=(r*(x**k))%p
    print("The Encrypted cipher for above plain text is : (", q,",",y,")")
    
    

def decryption_elg(r1,r2,g,p,a):
    m=((r1**(p-1-a))*r2)%p
    return(m)



t=int(input("press 0 for encryption and 1 for decryption: " ))
if t==0:
    p=int(input("Enter any prime no.: "))
    k=key_generation(p)
    r=int(input("enter the plain text: "))
    g,p,x=map(int,input("Enter the public key g,p,x with spaces: ").split(" "))
    encryption_elg(r,g,p,x)
else:
    r1,r2=map(int,input("enter the cipher text with spaces: ").split(" "))
    g,p,a=map(int,input("Enter the private key g,p,a with spaces: ").split(" "))
    print("The decrypted plain text for above cipher is : ",decryption_elg(r1,r2,g,p,a))

   