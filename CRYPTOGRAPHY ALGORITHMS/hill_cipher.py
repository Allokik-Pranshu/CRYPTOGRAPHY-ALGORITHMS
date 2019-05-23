# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 10:45:16 2018

@author: allokik pranshu
"""

def key_matrix(b):
    if b==2:
        key=[[0 for x in range(2)] for y in range(2)]
        for i in range(2):
            key[i][0],key[i][1]=map(int,input("Enter the values of row ").split(" "))
    else:
        key=[[0 for x in range(3)] for y in range(3)]
        for i in range(3):
            key[i][0],key[i][1],key[i][2]=map(int,input("Enter the values of row ").split(" "))
    return(key)


def text_matrix(a,b):
    ch=[]
    for i in a:
        if i!=(" "):
            ch.append(ord(i)-97)
    pt=[]
    if b==3:
        if len(ch)%3==1:
            ch.append(ord('x')-97)
            ch.append(ord('x')-97)
        elif len(ch)%3==2:
            ch.append(ord('x')-97)
        else:
            ch=ch
        k=[]
        for i in range(0,len(ch),3):
            k.append(ch[i])
            k.append(ch[i+1])
            k.append(ch[i+2])
            pt.append(k) 
            k=k[3:]
    else:
        if len(ch)%2==1:
            ch.append(ord('x')-97)
        else:
            ch=ch
        k=[]
        for i in range(0,len(ch),2):
            k.append(ch[i])
            k.append(ch[i+1])
            pt.append(k) 
            k=k[2:]
    return(pt)


def determinant(n,b):
    if b==3:
        det=((n[0][0])*((n[1][1]*n[2][2])-(n[1][2]*n[2][1])))-((n[0][1])*((n[1][0]*n[2][2])-(n[1][2]*n[2][0])))+((n[0][2])*((n[1][0]*n[2][1])-(n[1][1]*n[2][0])))
    else:
        det=(n[0][0]*n[1][1])-(n[0][1]*n[1][0])  
    return(det)


def adjoint(n,b):
    adj=[[0 for x in range(b)] for y in range(b)]
    if b==3:
        for i in range(b):
            for j in range(b):
                 adj[i][j]=((n[(i+1)%3][(j+1)%3]*(n[(i+2)%3][(j+2)%3]))-(n[(i+1)%3][(j+2)%3]*(n[(i+2)%3][(j+1)%3])))
                    
    else:
        for i in range(2):
            for j in range(2):
                adj[i][j]=((-1)**(i+j))*(n[(i+1)%2][(j+1)%2])
    adjoint=[[0 for x in range(b)] for y in range(b)]
    for i in range(b):
        for j in range(b):
            adjoint[i][j]=adj[j][i]
    return(adjoint)
            
            
def mmi(o):
    x=0
    while(((o*x)%26)!=1):
        x+=1
    return(x)

    
def multiplication(m,n,b,i):
    pr=[]
    g=m[i]
    for t in range(b):
        pd=0
        for s in range(b):
            pd+=n[t][s]*g[s]
        pr.append(pd%26)
    return(pr)


def encryption(a,b):
    m=text_matrix(a,b)
    n=key_matrix(b)
    cipher_matrix=[]
    for i in range(b):
        for j in range(b):
            n[i][j]=(n[i][j])%26        
    for i in range(len(m)):
        cipher_matrix.append(multiplication(m,n,b,i))
    cipher_matrix=sum( cipher_matrix,[])    
    for i in range(len(cipher_matrix)):
        cipher_matrix[i]=chr(cipher_matrix[i]+97)
    cipher=''.join(cipher_matrix)    
    return(cipher)



def decryption(a,b):
    m=text_matrix(a,b)
    n=key_matrix(b)
    t=determinant(n,b)
    if t==0:
        return("enter a key for which inverse exists")
    else:
        if t!=1:
            o=mmi(abs(t))
        else:
            o=t
    adj=adjoint(n,b)
    if t<=0:
        for i in range(b):
            for j in range(b):
                adj[i][j]=adj[i][j]*(-1)    
    for i in range(b):
        for j in range(b):
            adj[i][j]=(adj[i][j])%26   
    plain_text=[]
    for i in range(len(m)):
        plain_text.append(multiplication(m,adj,b,i))
    plain_text=sum(plain_text,[])
    for i in range(len(plain_text)):
        plain_text[i]=chr(((plain_text[i]*o)%26)+97)
    p_txt=''.join(plain_text)
    return(p_txt)
        



p=int(input("press 0 for encryption and 1 for decryption: " ))
if p==0:
    a=list(input("enter the plain text: ")) 
    b=int(input("Enter the key dimensions: "))
    print("The Encrypted cipher for above plain text is : ",encryption(a,b))
else:
    a=list(input("enter the cipher text: ")) 
    b=int(input("Enter the key dimensions: "))
    print("The decrypted plain text for above cipher is : ",decryption(a,b))








