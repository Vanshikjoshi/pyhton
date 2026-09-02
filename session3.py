#conditional statements
"""
marks = int(input("Enter the marks: "));
if(marks>=90 and marks<=100):
    print("A");
elif(marks>=80 and marks<=90):
    print("B");
elif(marks>=70 and marks<=80):
    print("C");
elif(marks>=60 and marks<=70):
    print("D");
elif(marks>=0 and marks<60):
    print("Failed: F");
else:
    print("Invalid marks");
"""
#pratcice questions-----------------------
"""
num = int(input("Enter a number: "));
if(num>0):
    print("Positive");
elif(num<0):
    print("Nagative");
else:
    print("Zero");
"""
"""
a = int(input("Enter a number: "));
b = int(input("Enter another number: "));
if(a>b):
    print(f"{a} is greater than {b}");
elif(a<b):
    print(f"{b} is greater than {a}");
else:
    print(f"{a} is equal to {b}");
"""
year = int(input("Enter a year: "));
if(year%4==0 and year%100!=0 or year%400==0):
    print(f"{year} is a leap year");
else:
    print("Not a leap year");
