# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 16:17:48 2021

@author: emmar
"""

# Color guessing game.

colors = ["purple", "orange", "green", "blue", "yellow", "red", "black", "pink"]

guess = input("Guess a color:")

if guess in colors:
    print("Congrats! You've guessed correctly!")
else:
    print("I'm sorry to report that you've guessed wrong...Try again.")