# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 10:38:25 2020

@author: user
"""

name=list()
score=list()
total=0
avg=0
n=input('how many people?')
n=int(n)
def f(total,n):
    return total/n

for i in range(n):
    na=input('your name')
    name.append(na)
    sc=input('your score')
    sc=int(sc)
    score.append(sc)
    total=total+sc
print('avg is',total/n)

highest=0
for i in range(n):
    if score[i]>highest:
       highest=score[i]
       na=name[i]
print(na,'you got the highest',highest)
lowest=100
for j in range(n):
    if score[j]<lowest:
       lowest=score[j]
       na=name[j]
print(na,'you got the lowest',lowest)

