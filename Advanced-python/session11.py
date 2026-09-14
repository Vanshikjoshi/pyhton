# shallow and deep copy
from copy import deepcopy

"""
-----------------------------------
original = [1, 2, 3]
cop = original
cop.append(100)
print(cop)
print(id(cop))
print(id(original))
print(original)  # original also changed
# both original and cop points to same location so here cop copied the reference and to resolve this we either use shallow copy or the deep copy
# shallow way- .copy()
origin = [1, 2, 3, 4, 5]
copy = origin.copy()
copy.append(100)
print(original, id(original))
print(copy, id(copy))
---------------------------------------
"""

# deep copy-
original = [54, 32, 78, 90, [59, 67, 45], 3, 47]
copy = original.copy()
copy.append(89)
print(copy)
print(original)
copy[4][1] = 5674
print(original)
print(copy)
# here using shallow method if change the list which is inside the list the changes reflected in original list also so to overcome deep copy comes in the picture
origin = [54, 32, 78, 90, [59, 67, 45], 3, 47]
cop = deepcopy(origin)  # from copy import deepcopy
cop.append(89)
print(cop)
print(origin)
cop[4][1] = 5674
print(origin)
print(cop)
