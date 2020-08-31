import craftclasses as cc
import items as i

import numpy as np


Cobblestone = i.cobble
Empty = i.empty
Stick = i.stick

spr = [
    [Cobblestone, Cobblestone, Cobblestone],
    [Empty, Stick, Empty],
    [Empty, Stick, Empty]
]

stone_pick_recipe = np.rot90(spr, 1, (0,1))
# Rotation by 90  deg