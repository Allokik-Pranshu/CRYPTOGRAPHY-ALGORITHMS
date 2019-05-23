# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 22:45:42 2019

@author: ALLOKIK PRANSHU
"""
import random

def rand(phi):
    a=random.randint(2,phi-1)
    return(a)



def private_key(e,phi):
    x=0
    while(((e*x)%phi)!=1):
        x+=1
    return(x)
    

def hcf(phi,e):
    if(e==0): 
        return phi 
    else: 
        return hcf(e,phi%e)
    

def key_generation(p,q): 
    key=[]
    n=p*q
    phi=(p-1)*(q-1)
    e=rand(phi)
    while(hcf(e,phi)!=1):
        e=rand(phi)
    d=private_key(e,phi)
    key.append(n)
    key.append(e)
    key.append(d)
    print("your randomly generated keys are as follows: ")
    print("Public key: ",e ," , ", n )
    print("Private key: ",d ," , ", n )
    return(key)
    
    
def encryption_rsa(r,e,n):
    c=(r**e)%n
    return c

def decryption_rsa(r,d,n):
    p=(r**d)%n
    return(p)



t=int(input("press 0 for encryption and 1 for decryption: " ))
if t==0:
    p=int(input("Enter the first prime no.: "))
    q=int(input("Enter the second prime no.: "))
    k=key_generation(p,q)
    r=int(input("enter the plain text: "))
    e,n=map(int,input("Enter the public key with spaces: ").split(" "))
    print("The Encrypted cipher for above plain text is : ",encryption_rsa(r,e,n))
else:
    r=int(input("enter the cipher text: ")) 
    d,n=map(int,input("Enter the private key with spaces: ").split(" "))
    print("The decrypted plain text for above cipher is : ",decryption_rsa(r,d,n))


    