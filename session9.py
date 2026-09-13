# sets- sets is a collection of unique elements-unique,mutable,no-indexing,immutable-elements
lst = {"abc@gmail.com", "xyz@gmail.com", 3, True}
print(type(lst))
print(lst)
# empty set
sett = set()
print(type(sett))
lst.add("pyq")
lst.remove("abc@gmail.com")
lst.discard("aplle")  # gives no error if do not exist
print(lst)
b = {8, False, "mango", 3}
print(lst | b)  # union operator
print(lst.union(b))  # using union() method
print(lst & b)  # interstion operator
print(lst.intersection(b))  # intersection() method
c = lst | b
for i in c:
    print(i, end=" ")
print()
d = {3, 5, 2, 6, 76, 3, 56, 89}
print(len(d))
print(sum(d))
print(max(d))
print(min(d))
print(sorted(d))
