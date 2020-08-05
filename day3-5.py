# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 14:24:22 2020

@author: user
"""

while True:
    print('______________________________')
    print('1.加法')
    print('2.減法')
    print('3.乘法')
    print('4.除法')
    print('5.離開')
    a=int(input('輸入選項'))
    if a==1:
        b=int(input('num1'))
        c=int(input('num2'))
        print('ans =',b+c)
    elif a==2:
        b=int(input('num1'))
        c=int(input('num2'))
        print('ans =',b-c)
    elif a==3:
        b=int(input('num1'))
        c=int(input('num2'))
        print('ans =',b*c)
    elif a==4:
        b=int(input('num1'))
        c=int(input('num2'))
        print('ans =',b/c)
    else:
        break
