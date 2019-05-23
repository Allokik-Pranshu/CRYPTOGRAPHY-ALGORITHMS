# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 21:45:21 2018

@author: allokik pranshu
"""
def left_shift(k,i):
    l=k[i:]
    for j in range(i):
        l.append(k[j])
    return(l)


def permutation_10(k):
    p=[]
    p_10=[3,5,2,7,4,10,1,9,8,6]
    for i in range(10):
        p.append(k[p_10[i]-1])
    return(p)


def permutation_8(k):
    p=[]
    p_8=[6,3,7,4,8,5,10,9]
    for i in range(8):
        p.append(k[p_8[i]-1])
    return(p)


def key_generation(b):
    k=[]
    b=permutation_10(b)
    b1=b[0:5]
    b2=b[5:]
    b1=left_shift(b1,1)
    b2=left_shift(b2,1)
    k1=b1+b2
    k1=permutation_8(k1)
    k.append(k1)
    b1=left_shift(b1,2)
    b2=left_shift(b2,2)
    k2=b1+b2
    k2=permutation_8(k2)
    k.append(k2)
    return(k)


def initial_permutation(a):
    p=[]
    i_p=[2,6,3,1,4,8,5,7]
    for i in range(8):
        p.append(a[i_p[i]-1])
    return(p)
    
    
def expansion_permutation(a):
    p=[]
    e_p=[4,1,2,3,2,3,4,1]
    for i in range(8):
        p.append(a[e_p[i]-1])
    return(p)


def xor(k,a2,t):
    p=[]
    for i in range(t):
        p.append(str(int(k[i])^int(a2[i])))
    return(p)
    
       
def s_0(a):
    s0=[[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]
    t_1=[a[0],a[3]]
    t_2=[a[1],a[2]]
    t_1=int((''.join(t_1)),2)
    t_2=int((''.join(t_2)),2)
    t=str(bin(s0[t_1][t_2]))
    t=t[2:]
    if len(t)==1:
        t='0'+t
    return(t)


def s_1(a):
    s1=[[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]
    t_1=[a[0],a[3]]
    t_2=[a[1],a[2]]
    t_1=int((''.join(t_1)),2)
    t_2=int((''.join(t_2)),2)
    t=str(bin(s1[t_1][t_2]))
    t=t[2:]
    if len(t)==1:
        t='0'+t
    return(t)

    
def permutation_4(a2):
    p=[]
    p_4=[2,4,3,1]
    for i in range(4):
        p.append(a2[p_4[i]-1])
    return(p)


def inverse_permutation(c):
    p=[]
    i_p=[4,1,3,5,7,2,8,6]
    for i in range(8):
        p.append(c[i_p[i]-1])
    return(p)
   
    
def encryption(a,b):
    k=key_generation(b)
    a=initial_permutation(a)
    a1=a[0:4]
    a2=a[4:]
    cipher=[]
    for i in range(2):
        a2=expansion_permutation(a2)
        t=8
        a2=xor(k[i],a2,t)
        x=a2[0:4]
        a2_1=s_0(x)
        y=a2[4:]
        a2_2=s_1(y)
        a2=a2_1+a2_2
        a2=permutation_4(a2)
        t=4
        a2=xor(a1,a2,t)
        cipher.append(a2)
        a1=a[4:]
    cipher=cipher[1]+cipher[0]
    cipher=inverse_permutation(cipher)
    cipher=''.join(cipher)
    return(cipher)
    

def decryption(a,b):
    k=key_generation(b)
    a=initial_permutation(a)
    a1=a[0:4]
    a2=a[4:]
    plain=[]
    j=1
    for i in range(2):
        a2=expansion_permutation(a2)
        t=8
        a2=xor(k[j],a2,t)
        j=j-1
        x=a2[0:4]
        a2_1=s_0(x)
        y=a2[4:]
        a2_2=s_1(y)
        a2=a2_1+a2_2
        a2=permutation_4(a2)
        t=4
        a2=xor(a1,a2,t)
        plain.append(a2)
        a1=a[4:]
    plain=plain[1]+plain[0]
    plain=inverse_permutation(plain)
    plain=''.join(plain)
    return(plain)
    

p=int(input("press 0 for encryption and 1 for decryption: " ))
if p==0:
    a=list(input("enter the 8 bit plain text in binary: ")) 
    b=list(input("Enter the 10 bit key in binary: "))
    print("The Encrypted cipher for above plain text is : ",encryption(a,b))
else:
    a=list(input("enter the 8 bit cipher text in binary: ")) 
    b=list(input("Enter the 10 bit key dimensions in binary: "))
    print("The decrypted plain text for above cipher is : ",decryption(a,b))