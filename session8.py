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
"""
# membership operator
student = {"name": "Vanshika Joshi", "age": 19, "roll no": 1170, "is-std": True}
print("name" in student)
print("marks" in student)
