# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 16:00:03 2018

@author: ALLOKIK PRANSHU
"""
def mmi(o):
    x=0
    while(((o*x)%26)!=1):
        x+=1
    return(x)

def key_generation():
    alpha=[1,3,5,7,9,11,15,17,19,21,23,25]
    flag=1
    key=[1,2]
    while(flag==1):
        a,b=map(int,input("Enter the value of alpha and beta: ").split())    
        if (b<26 and b>=0 and a in alpha):
            key[0]=a
            key[1]=b
            flag=0
            break
        else: 
            print("please enter a valid value of alpha and beta")
    return(key)

def encryption(t):
    key=key_generation()
    a=key[0]
    b=key[1]
    t=list(t)
    for i in range(len(t)):
        t[i]=t[i].lower()
    cipher=[]
    for i in t:
        if (i!=' '):
            cip=((a*(ord(i)-97))+b)%26
            cipher.append(chr(cip+97))
        else:
            cipher.append(' ')
    c=''.join(cipher)
    return(c)
def decryption(t):
    key=key_generation()
    a=key[0]
    b=key[1]
    t=list(t)
    for i in range(len(t)):
        t[i]=t[i].lower()
    text=[]
    m=mmi(a)
    for i in t:
        if (i!=' '):
            cip=(m*(ord(i)-97-b))%26
            text.append(chr(cip+97))
        else:
            text.append(' ')
    c=''.join(text)
    return(c)
    
            
      
p=int(input("press 0 for encryption and 1 for decryption: " ))
if p==0:
    t=list(input("enter the plain text: ")) 
    print("The Encrypted cipher for above plain text is : ",encryption(t))
else:
    t=list(input("enter the cipher text: ")) 
    print("The decrypted plain text for above cipher is : ",decryption(t))
