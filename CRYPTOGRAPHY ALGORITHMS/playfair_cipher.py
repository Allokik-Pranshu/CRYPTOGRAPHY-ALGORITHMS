# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 14:51:33 2018

@author: allokik pranshu
"""

a=list(input("enter the plain text: "))
b=list(input("Enter the key: "))


def plain_text(a):
    pt=[]
    pt+=a[0]
    for i in range(1,len(a)):
        if a[i]!=(" "):
            if (a[i-1]==a[i]) and (len(pt)%2!=0) :
                pt.append('x')
                pt.append(a[i])
            else:
                pt.append(a[i])
    if ((len(pt)%2)!=0):
        pt+=("x")
    return(pt)

def key_matrix(b):
    matrix = [[0 for x in range(5)] for y in range(5)]
    ch=[]
    j=0
    k=0
    for i in b:
        if i!=(" "):
            if ord(i) not in ch:
                matrix[j][k]=i
                ch.append(ord(i))
                if k==4:
                    j=j+1
                    k=0
                else:
                    k=k+1
    p=[]
    for t in range(26):
        p.append(chr(97+t))
    for i in p:
        if (ord(i) not in ch) and i!='j':
            matrix[j][k]=i
            ch.append(ord(i))
            if k==4:
                j=j+1
                k=0
            else:
                k=k+1
    return(matrix)



def encryption(text,matrix):
    cipher=[]
    for i in range(0,int(len(text)/2)+2,2):
        q=text[i]
        w=text[i+1]
        for j in range(5):
            for k in range(5):
                if matrix[j][k]==q:
                    break
            else:
                continue
            break
        for s in range(5):
            for t in range(5):
                if matrix[s][t]==w:
                    break
            else:
                continue
            break
        if j==s:
            cipher.append(matrix[j][(k+1)%5])
            cipher.append(matrix[j][(t+1)%5])
        elif k==t:
            cipher.append(matrix[(j+1)%5][k])
            cipher.append(matrix[(s+1)%5][k])
        else:
            cipher.append(matrix[j][t])
            cipher.append(matrix[s][k])
    return(cipher)



text=plain_text(a)
matrix=key_matrix(b)
cipher_text=''.join(encryption(text,matrix))
print(text)
print(matrix)
print(cipher_text)                
        
        
    













        