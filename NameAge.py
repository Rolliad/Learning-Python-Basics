# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 12:52:42 2021

@author: emmar
"""
# This program says "hello" and asks for your name

print("Hello!")
print("What is your name?") # Ask for their name.
myName = input()
print("It's good to meet you, " +myName)
print("Your length of your name is:")
print(len(myName))
print("How old are you?") # Ask for their age.
myAge=input()
print("You will be " + str(int(myAge) + 1)+  " in a year.")