# tuples -collection of values stored in single variable. Tuples are immutable. once created you cannot change
# properties-ordered, immutable, allows duplicates, can hold any data type.
tup = ("Delhi", 4, "Mumbai", "Pune", 2, 3, True, 4)
print(tup)
# tup.append("New York")    //not possible
print(tup.count(4))
print(tup.index("Pune"))
print(tup[::-1])
# tuple packing and unpacking
my_tup = (1,)
print(type(my_tup))
a, b, c = 3, 4, 5  # this is unpacking of tuple
