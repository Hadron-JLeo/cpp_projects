import craftclasses as cc

Item = cc.Item
C_Item = cc.Craftable_Item

cobble = Item("Cobblestone", 1, 150, False)
stick = Item("Stick", 0.5, 152, True)
diamond = Item("Diamond", 50, 200, False)


item_shortcuts = {
    "cobblestone" : cobble,
    "Cobblestone" : cobble,
    "cobble" : cobble,
    "Cobble" : cobble,
    "Stick" : stick,
    "stick" : stick,
    "Diamond" : diamond,
    "diamond" : diamond,
    "dia" : diamond
}

#STONE_PICK = C_Item()