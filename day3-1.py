# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 09:26:45 2020

@author: user
"""

for i in range(1,10):
    for j  in range(1,i):
        print(i,'*',j,'=',i*j,end=', ')
    print()
    
for i in range(1,10):
    for j in range(1,10):
        print(i,'*',j,'=',i*j,end='. ')
    print()

q=input("number1")
q=int(q)
p=input('number2')
p=int(p)
print(q,'*',p,'=',q*p)
