import sys
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolButton
from PyQt5.QtGui import QPixmap
import items, pycraft



ui_path = r"C:/Users/Decetra/.vscode/Desktop/mr_stuff/GUI_stuff/craft.ui"
gui_folder_path = r"C:\Users\Decetra\.vscode\Desktop\mr_stuff\GUI_stuff"

stick_icon = gui_folder_path + "\Stick_inventory.png"

app = QtWidgets.QApplication(sys.argv)
window = uic.loadUi(ui_path)

#region button defines--
b = [
# Row 1:
[window.craft_1_1, window.craft_2_1, window.craft_3_1],
# Row 2:
[window.craft_1_2, window.craft_2_2, window.craft_3_2],
# Row 3: 
[window.craft_1_3, window.craft_2_3, window.craft_3_3]

]
#endregion button defines--

#buttons = np.rot90(b, 1, (0,1))
buttons = np.transpose(b) # Flipping x and y values

last_clicked_but = None # The last button that was clicked



def arr_output(array=buttons):
    for r in array:
        for c in r:
            print(c,end = " ")
        print()

def deep_index(l, w):
    lst = l.tolist()
    return [(i, sub.index(w)) for (i, sub) in enumerate(lst) if w in sub]

def Change_Button_Content(button, icon):
    # The buttons are just used for modifying the array and showing its contents
    #button.
    #craft_but_1_1.set
    #buttons[]
    button.setIcon(QtGui.QIcon(icon))
    button.setIconSize(QtCore.QSize(90,90))

    pass

def Button_Click(button=None, option=None):

    input_window = window.formFrame
    input_close_button = window.InputCloseButton
    line_edit = window.lineEdit
    c_table = pycraft.crafting_table

    #print("clicked on a button")

    def CraftArray():

        last_clicked_but = button
        global last_index
        last_index = deep_index(buttons, button)[0]
        print(deep_index(buttons, button)[0])
        input_close_button.show()
        input_window.show()
       # Change_Button_Content(last_clicked_but,None)
        
    def CloseInput():
        input_window.hide()
        window.InputCloseButton.hide()

    def Input():
        #print (deep_index(buttons, last_clicked_but))
        print(last_index)
        x, y = last_index
        
        
        item_input = line_edit.text()
        print(item_input)

        if (item_input.lower() is ("empty") or (not line_edit.text()) or None):
            item_input = "empty" # Works
            

        print("Item to be input: ", item_input) # works
        try:
            c_table[x][y] = pycraft.item_dict.get(item_input.lower())
            print (c_table[x][y].name)
        except:
            print("Item doesn't exist!")
            CloseInput()
        Change_Button_Content(buttons[x][y], c_table[x][y].icon)


    def CraftButton():
        # Check if the array matches a recipe
        print("pressed crafting button")
        item = items.stone_pick
        if np.array_equal(c_table, item.recipe):
            print("Crafted a stone pickaxe!")
            img = QPixmap(item.icon)
            window.NewItemIcon.setPixmap(img)

    # Options--

    if option is not None:
        if option.lower() == "craftarray":
            CraftArray()
        if option.lower() == "closeinput":
            CloseInput()
        if option.lower() == "input":
            Input()
        if option.lower() == "craftbutton":
            CraftButton()
        #print(option)
    else:
        print("Ya forgot to input an option, ya wanker!")


def Button_Comparator(array=buttons):
    #clicked_but : QtWidgets.QToolButton() 
    btn = QToolButton
    for y in range(3):
        for x in range(3):
            clicked_but : QtWidgets.QToolButton(parent=window) = buttons[x][y]
            clicked_but.clicked.connect(lambda: Button_Click(clicked_but.sender(), "Craftarray"))


def Initialize_Window():

    window.formFrame.setEnabled(True)
    window.InputCloseButton.setEnabled(True)
    window.InputCloseButton.clicked.connect(lambda: Button_Click(0, option="CloseInput"))
    window.EnterButton.clicked.connect(lambda: Button_Click(0, option="input"))

    window.craftButton.clicked.connect(lambda: Button_Click(0, option="Craftbutton"))

    window.formFrame.hide()
    window.InputCloseButton.hide()
    window.show()

pycraft.Start()
Initialize_Window()
Button_Comparator()
#arr_output()
#print (deep_index(buttons, "poop"))
#print(buttons[0][1], buttons[1][2], buttons[2][1])
#print(buttons[1][0], buttons[2][1], buttons[0][2])
sys.exit(app.exec_())
#k=input()