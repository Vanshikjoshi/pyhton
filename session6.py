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
"""
----------------------------------------------------
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



def new_lst(lst1, lst2):
    new_lst = []
    n = len(lst1)
    for i in range(0, n):
        total = lst1[i] + lst2[i]
        new_lst.append(total)
    return new_lst


num1 = [6, 5, 3, 5, 6, 5, -6, 80]
num2 = [5, 76, 8, 4, 56, 9, 46, 3]
lst = new_lst(num1, num2)
print(lst)
-----------------------------------------
def is_sorted(lst):
    n = len(lst)
    sorted = True
    for i in range(0, n):
        if i == n - 1:
            break
        if lst[i] <= lst[i + 1]:
            sorted = True
        else:
            sorted = False
            break
    return sorted


nums = [3, 6, 8, 9, 9, 17, 18, 23, 45, 58, 79, 100]
lst = is_sorted(nums)
if lst == True:
    print(f"Yes Sorted!")
else:
    print(f"Not sorted")
    ---------------------------------------------------
"""
# list methods
"""
-----------------------------------------
#manipulating method
fruits = ["apple", "Banana", "Grapes"]
print(fruits)
fruits.append("Orange")
fruits.insert(1, "Kiwi")
# adds at a paticular index;
print(fruits)
fruits.remove("Banana")
# removes by value
print(fruits)
fruits.pop()
# remove the last value by default
print(fruits)
fruits.pop(0)
# remove element at index 0
print(fruits)
-----------------------------------------------
"""
# sorting,reversing,searching and counting methods
"""
-------------------------------------------
num = [20, 40, 10, 30, 50]
num.sort()
print(num)
num.sort(reverse=True)
print(num)
print(num.index(50))
fruit = ["Apple", "Banana", "Orange", "Apple", "Payaya"]
print(fruit.count("Apple"))
--------------------------------------------
"""
# clearing and membership operators
"""
-----------------------------------------
lst = [2, 34, 23, 56, 11, 67, 15]
lst.clear()  # removes all elements;
print(lst)
nums = [2, 34, 23, 56, 11, 67, 15]
print(5 in nums)  # returns Ture is exist else False
print(34 in nums)
print(10 not in nums)  # returns True is not rxist else False
print(56 not in nums)
-----------------------------------
"""
# practice questions
"""
-------------------------------------
nums = [3, 1, 5, 11, 2]
max = 0
for i in nums:
    if i > max:
        max = i
print(max)
-----------------------------
nums = [1, 2, 3, 4, 5]
n = len(nums)
for i in range(n // 2):
    temp = nums[i]
    nums[i] = nums[n - 1 - i]
    nums[n - 1 - i] = temp
print(nums)
-----------------------
lst1 = [1, 2, 3, 4]
lst2 = [5, 6, 7, 8]
lst3 = lst1 + lst2
print(lst3)
----------------------------------------------
data = [10, 20, 30, 20, 10, 40, 50, 40]
n = len(data)
for i in range(0, n):
    j = i + 1
    while j < len(data):
        if data[i] == data[j]:
            data.pop(j)
        else:
            j += 1
print(data)
--------------------------------------
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = []
odd = []
n = len(nums)
for i in range(0, n):
    if nums[i] % 2 == 0:
        even.append(nums[i])
    else:
        odd.append(nums[i])
print(even)
print(odd)
---------------------------------------------
"""
# nested list
"""
---------------------------------------------
marks = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(marks[2])
print(marks[1][0])
for i in range(0, 3):
    for j in range(0, 3):
        print(marks[i][j], end=" ")
    print()
# dynamic matrix
mat = [[1, 2, 3, 4, 5], [3, 4, 5, 2, 1], [6, 7, 8, 9, 2], [4, 9, 2, 5, 3]]
rows = len(mat)
cols = len(mat[0])
for i in range(0, rows):
    for j in range(0, cols):
        print(mat[i][j], end=" ")
    print()
=----------------------------------------
"""
# practice questions
"""
---------------------------------------
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rows = len(mat)
cols = len(mat[0])
for i in range(0, rows):
    for j in range(0, cols):
        if i != j:
            mat[i][j] = "*"
        print(mat[i][j], end=" ")
    print()
---------------------------------------------
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rows = len(mat)
cols = len(mat[0])
for i in range(0, rows):
    for j in range(0, cols):
        if i < j:
            mat[i][j] = "*"
        print(mat[i][j], end=" ")
    print()
---------------------------------------------
"""
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rows = len(mat)
cols = len(mat[0])
for i in range(0, rows):
    for j in range(0, cols):
        if i + j == rows - 1:
            print(mat[i][j], end=" ")
        else:
            print("*", end=" ")
    print()
