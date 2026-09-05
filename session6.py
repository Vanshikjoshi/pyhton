"""
------------------------------------
l= ["xyz", 55, "abc", True];
for i in l:
    print(i, end=" ");
print();
print(l*3); #duplicate the list 3 times
print(type(l));
------------------------------------
"""

"""
-----------------------------------------
marks = [34,67,55,90,45,24,7];
print(len(marks));
print(max(marks));
print(min(marks));
print(sum(marks));
print(sorted(marks));
print(sorted(marks, reverse=True));
avg = sum(marks)/len(marks);
print(avg);
-----------------------------------------------
"""
# indexing
"""
--------------------------------------------
lst = ["ABc", 89, True, 90, "Apple"]
print(lst[3])
print(lst[0])
print(lst[-1])
---------------------------------------------
"""
# updating list
"""
----------------------------------------------
lst = ["aman", 89, True, "Saumya", 90, "Apple", 67]
print(lst)
lst[2] = False
lst[1] = "Nadia"
print(lst)
movie = ["abcd", "tiger", "god", "kanha", "taare"]
print(movie[0])
print(movie[-1])
n = int((len(movie) - 1) / 2)
print(movie[n])
----------------------------------------
"""
# slicing in python
"""
--------------------------------------
lst = [23, 45, 3, 23, 46, 78, 56, 9, 6, 34, 26, 58, 90]
lst1 = lst[0:5]
lst2 = lst[2:]  # goes till end
print(lst1)
print(lst2)
lst3 = lst[0::3]  # skips 2 values
lst4 = lst[::-1]  # reverse the list
print(lst4)
print(lst3)
--------------------------------------------
"""
# looping in list
fruit = ["Apple", "Mango", "Banana", "Grapes", "Blueberry"]
i = 0
while i < len(fruit):
    print(fruit[i], end=",")
    i += 1
print()
for i in fruit:
    print(i, end=" ")
print()

for idx, val in enumerate(fruit):  # used when idx and value both are required
    print(f"Index: {idx} and valuse is : {val}")
