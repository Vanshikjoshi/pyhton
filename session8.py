# Dictionary in python
# properties- key-value pairs, ordered only after 3.7, mutable, unique keys, immutable keys
"""
-------------------------------------------
marks = {"Maths": 89, "English": 90, "Hindi": 98, 100: "Anirudh", "abc": [1, 2, 3, 4]}
print(marks)
# access elements in dict - dict_name[keyname]
print(marks[100])  # print Anirudh
print(marks["abc"])
print(marks["Maths"])
print(marks.get("English"))
print(
    marks.get("Science", 0)
)  # it will print none if key not exist by default but since we have used 0 so it will print 0 if key do not exist
-------------------------------------------
"""

# adding
"""
--------------------------------
student = {"name": "Abc", "age": 19}
print(student)
student["city"] = "Haldwani"
student["marks"] = 89
print(student)
# updating
student["age"] = 20
student["name"] = "Robot"
print(student)
student.update(
    {"city": "Dehradun", "marks": 99, "roll no": 1170}
)  # used when we need to update multiple values at a time
print(student)
# removing
student.pop("marks")  # shows error if key don't exist
print(student)
del student["age"]
print(student)
student.clear()  # remove all keys and values or emptied the dict
print(student)
del student  # deletes the student permanently from the memory
-------------------------------------
# membership operator
student = {"name": "Vanshika Joshi", "age": 19, "roll no": 1170, "is-std": True}
print("name" in student)
print("marks" in student)
-------------------------------------
"""
# dict_methods
"""
-----------------------------------
marks = {"maths": 89, "science": 100, "comp": 80, "hindi": 99, "history": 78}
print(marks.keys())
print(marks.values())
total = 0
for k in marks.keys():
    print(k, ":", marks[k], end=" ")
    total += marks[k]
print()
print(f"Total marks is: {total}")
------------------------------------------
marks = {"maths": 89, "science": 100, "comp": 80, "hindi": 99, "history": 78}
print(marks.items())
for i in marks.items():
    print(i)
    print(i[0])
for sub, mark in marks.items():
    print(sub, ":", mark)
------------------------------------------
#filtering
marks = {"maths": 89, "science": 56, "comp": 80, "hindi": 99, "history": 78}
for sub, mark in marks.items():
    if mark >= 80:
        print(f"{sub}: Execellent")
    elif mark >= 60:
        print(f"{sub}: Good")
    else:
        print(f"{sub}: need to improve!")
-------------------------------------------------------
"""
# practicing questions
"""
----------------------------------------
std = {"name": "abc", "age": 20, "city": "haldwani", "marks": 79.8}
for i in std:
    print(i, end=" ")  # printing key
-------------------------------------------------------
score = {"science": 78, "maths": 89, "hindi": 67, "english": 90}
n = score.get("maths")
if n in score.values():
    print(n)
else:
    print("NOt available")
-------------------------------------------------------
score = {"science": 78, "maths": 89, "hindi": 67, "english": 90}
total = 0
for i in score.values():
    total += i
print(f"Total is {total}")
avg = total / len(score)
print(f"Average is : {avg}")
-------------------------------------------------------
"""
# inbuilt-methods
"""
-------------------------------------------
score = {"science": 78, "maths": 89, "hindi": 67, "english": 90}
print(len(score))
print(sum(score.values()))
print(min(score.values()))
print(max(score.values()))
print(min(score))  # sorted alphabetically
print(max(score))
print(sorted(score))
-------------------------------------------------------
"""
# nested dict
"""
---------------------------------------------
std = {
    "101": {"name": "abc", "age": 21, "city": "haldwani"},
    "102": {"name": "xyz", "age": 17, "city": "mumbai"},
    "103": {"name": "uwv", "age": 28, "city": "jaipur"},
}
print(std["102"]["city"])
print(std["101"]["name"])
# adding new
std["104"] = {"name": "pqr", "age": 25, "city": "banglore"}
print(std["104"]["age"])
# updating
std["101"]["name"] = "Don"
print(std["101"]["name"])
# looping through nested dict
for roll, info in std.items():
    print(f"Roll {roll}: {info["name"]} from {info["city"]}")
--------------------------------------------------
"""
# lis in dict
"""
----------------------------------------------------
std = {
    "name": "Rahul",
    "age": 23,
    "subjects": ["Maths", "Hindi", "English"],
    "marks": [83, 93, 98],
}
print(std["subjects"])
print(std["subjects"][1])
for i in std["marks"]:
    print(i)
std["subjects"].append("Science")
print(std["subjects"])
std["marks"].append(87)
print(std["marks"])
print(sum(std["marks"]))
--------------------------------------------------
# sorting in nested data with lambda
std = [
    {"name": "Rahul", "marks": 85},
    {"name": "Priya", "marks": 93},
    {"name": "Karan", "marks": 78},
    {"name": "Siya", "marks": 67}
]
marks = sorted(std, key=lambda s: s["marks"])
print("Sorted by marks:")
for s in marks:
    print(s)
--------------------------------------------------
"""
# dict comprehension
squares = {}
for i in range(1, 11):
    squares[i] = i * i
print(squares)
# now using dict comprehension
square = {i: i * i for i in range(1, 6)}
print(square)
marks = {"maths": 98, "hindi": 45, "english": 83, "science": 45}
top = {sub: m for sub, m in marks.items() if m > 80}
print(top)
# creating dict from two list
subject = ["maths", "hindi", "english", "science"]
marks = [83, 90, 78, 59]
result = {s: m for s, m in zip(subject, marks)}
print(result)
