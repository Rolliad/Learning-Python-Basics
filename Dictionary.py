# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 20:05:10 2021

@author: emmar
"""
#Using a dictionary
rhymes = {"1": "fun",
          "2": "blue",
          "3": "me",
          "4": "floor",
          "5": "live"
          }

n = input("Type a number:")
if n in rhymes:
    rhyme = rhymes[n]
    print(rhyme)
else:
    print("Not found.")
