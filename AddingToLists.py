# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 13:19:26 2021

@author: emmar
"""
"""
A program that creates a list, looks at values to see if they are in the list 
and then adds them if they aren't part of the list.
"""
#The empty lists
myUniqueList = []
MyLeftOvers = []

print("Add five pieces of data to the collection!")

#Function to add items to the list and return True or False.
def add_to_list():
    n = input("Add data to the collection:")
    if n not in myUniqueList:
        myUniqueList.append(n)
        print(True)
        
    else:
        MyLeftOvers.append(n)
        print(False)
        
#Loop to call the function multiple times.        
for i in range(5):
    add_to_list()
 
#Both lists are printed before program termination.       
print("The unique collection is:", myUniqueList)
print("The Leftovers are:", MyLeftOvers)