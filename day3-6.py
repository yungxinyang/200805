# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 14:46:56 2020

@author: user
"""


d={}
print('welcome')
while True:
    print('1.建立詞彙')
    print('2.列出所有單字')
    print('3.英翻中')
    print('4.中翻英')
    print('5.測驗')
    print('6.離開')
    a=int(input('輸入數字'))  

    if a==1:
        while True:
            c=input('Chinese(輸入0可離開)')
            if c=='0':
               break
            e=input('English')
            d[c]=e
       
    elif a==2:
         print(d)
    elif a==3:
        while True:
            i=input('輸入英文(輸入0可離開)')
            if i=='0':
                   break
            elif 'i' in d:
               print(i,'的中文是',d[i])
            else:
               print('沒有這個字')
                 
    elif a==4:
        while True:
             j=input('輸入中文(輸入0可離開)')
             if j=='0':
                   break
             elif 'j' in d:
                 print(j,'的英文是',d[j])
             else:
                print('沒有這個字')
    elif a==5:
        for key,value in dict.items(d):
            print(key)
            ans=input('請輸入英文')
            if ans==value:
               print('答對了')
            else:
               print('答錯了')
         
    else:
        break
    