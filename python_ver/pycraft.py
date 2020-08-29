import math, os, random

""" My Modules """
import craftclasses as cc
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

def Output_CTable():

    for column in range(3):
        temp_arr = []
        for row in range(3):
            temp_arr.append(crafting_table[row][column].name)
        print(temp_arr)

def U_Input():
    user_item = input("Enter an item name: ")
    x = int(input("Enter x coordinates: ")) - 1
    y = int(input("Enter y: ")) - 1
    crafting_table[x][y] = item_dict.get(user_item)
    Output_CTable()

def Start():
    Fill_CTable(items.stick)
    Output_CTable()

Start()
while(True):
    U_Input()

Start()
user_input = input() 
crafting_table[0][0] = item_dict.get(user_input)
print(item_dict.get(user_input).name)
Output_CTable()