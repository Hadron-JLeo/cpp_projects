import math, os, random
import numpy as np


""" My Modules """
import classes as cc
import items 


Item = cc.Item
item_dict = items.item_shortcuts


crafting_table = [[None for x in range(3)] for y in range(3)]

def Fill_CTable(fill_item:Item):
    for y in range(3):
        for x in range(3):
            crafting_table[x][y] = fill_item

def Input_Field(fill_item:Item, x,y):
    crafting_table[x][y] = fill_item

def Output_CTable(arr):

    for column in range(3):
        temp_arr = []
        for row in range(3):
            temp_arr.append(arr[row][column].name)
        print(temp_arr)

def U_Input():
    user_item = input("Enter an item name: ")
    x = int(input("Enter x coordinates: ")) - 1
    y = int(input("Enter y: ")) - 1
    crafting_table[x][y] = item_dict.get(user_item)
    Output_CTable(crafting_table)


stone_pick_recipe = items.short_declare()
"""
def Array_Comparator(arr1, arr2):

    if arr1 == arr2:
        print("True")
        return True
    else:
        print("oof")
        return False
"""


def Start():
    #items.short_declare()
    Fill_CTable(items.empty)
   # Output_CTable(crafting_table)
    # Output_CTable(stone_pick_recipe)
    
    #print(items.stone_pick_recipe)

#Array_Comparator(crafting_table, i)

if __name__ == "__main__":    
    Start()
    #while(Array_Comparator(crafting_table, i) == False):
    while(True):
        U_Input()
        if np.array_equal(crafting_table, stone_pick_recipe):
            print("Done! Success at crafting!")
            break
