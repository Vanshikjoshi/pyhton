name = "Vanshika";
age = 20;
cgpa = 9.5;
is_student = True;
print(age);
print(cgpa, end=" ");
print(is_student);
print(name, "is a student with age", age, "and CGPA", cgpa);
print(type(name), type(age), type(cgpa), type(is_student));
date = 12;
month = "09";
year = 2023;
print(date,month,year, sep="-");
#f-strings
print(f"Your name is {name} and age is {age}. the sum of cpga and age is {cgpa+age}");
#type conversion
print(f"The current type of age is {type(age)} but after converting it explicitly to bool it becomes {type(bool(age))}")
# taking in"put from user
num1=input("Enter somthing: ");
print(f"type of num1 is {type(num1)} and value is {num1}");