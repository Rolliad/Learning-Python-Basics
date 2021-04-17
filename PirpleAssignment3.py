# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 11:52:04 2021

@author: emmar

Function and if statements to check for equivilance. 
"""
a = 10
b = "10"
c = 5
a = int(a)
b = int(b)
c = int(c)
equivNumber = False
def equivTest(a, b, c):
    if a == b or a == c:
        equivNumber = True
    if equivNumber == True:
        print(equivNumber)
        
equivTest(a, b, c)