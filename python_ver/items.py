import craftclasses as cc

stone_pick_recipe = None


Item = cc.Item
C_Item = cc.Craftable_Item

def short_declare():
    import recipes as r
    stone_pick_recipe = r.stone_pick_recipe
    print(stone_pick_recipe)
    
    return stone_pick_recipe



crafting_table = [[None for x in range(3)] for y in range(3)]


cobble = Item("Cobblestone", 1, 150, False)
stick = Item("Stick", 0.5, 152, True)
diamond = Item("Diamond", 50, 200, False)
empty = Item("#", 0, 0, False)

stone_pick = C_Item("Stone Pickaxe", 15, 175, stone_pick_recipe)

item_shortcuts = {
    "empty" : empty,
    "cobblestone" : cobble,
    "Cobblestone" : cobble,
    "cobble" : cobble,
    "Cobble" : cobble,
    "Stick" : stick,
    "stick" : stick,
    "Diamond" : diamond,
    "diamond" : diamond,
    "dia" : diamond,
    "stone pick" : stone_pick,
    "stonepick" : stone_pick,
    "stone_pick" : stone_pick,
    "Stone Pick" : stone_pick,
    "Stonepick" : stone_pick
}

#STONE_PICK = C_Item()