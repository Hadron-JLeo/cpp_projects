class Item():

    name = ""
    value = ""
    item_id = 0    
    craftable = False

    def __init__(self, n:str, v:float, i:float, c=False):
        self.name = n
        self.value = v
        self.item_id = i
        self.craftable = c

    def Output_Name(self):
        print(self.name)

class Craftable_Item():
    
    my_item = None
    my_recipe = [[None for x in range(3)] for y in range(3)]

    print() 

    def __init__(self, mi:Item, mr):
        self.my_item = mi
        self.my_recipe = mr
    
    def Output_Item(self):
        print(self.my_item)