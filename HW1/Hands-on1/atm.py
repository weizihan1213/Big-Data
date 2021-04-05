#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 14:49:38 2020

@author: eric
"""

wd = int(input("Enter the amount for withdrwal: "))
bills = {
        100 : 0,
        50 : 0,
        20 : 0,
        10 : 0
        }
for i, j in bills.items():
    while wd >= i:
        wd -= i
        bills[i] += 1
        if wd == 0:
            break
        
if(wd != 0):
    print('The amount cannot be drawn.')
else:
    print('Please collect your bills as follows:')
    for i, j in bills.items():
        if j != 0:
            # print(money)
            # print(f'${i:3}: {j}')
            print('%5s' '%2s' % ('$'+str(i)+':', str(j)))
    
    
    