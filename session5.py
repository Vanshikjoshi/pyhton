"""
def is_even(num):
    if(num%2 == 0):
        return True
    else:
        return False    

for  i in range(1,3):
    if is_even(i):
        print(f"{i} is even");
    else:
        print(f"{i} is odd");

"""
"""
--------------------------------------------------
def factors(num):
    for i in range(1,num+1):
        if(num%i == 0):
            print(i,end=" ");

n = input("Enter a number to find its factors: ")
factors(int(n));
--------------------------------
"""

"""
------------------------------------------------
def add(a,b):
    return a+b;
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = add(num1, num2);
print(result);
------------------------------
"""
"""
----------------------------------------
def rect_area(l, b):
    return l*b;
length = int(input("Enter the length: "));
breadth = int(input("Enter the breadth: "));
result = rect_area(length, breadth);
print(f"The are of rectangle is: {result}");
-------------------------------
"""
"""
--------------------------------------
def find_max(a,b,c):
    return max(a,b,c);
num1=int(input("Enter num1: "));
num2=int(input("Enter num2: "));
num3=int(input("Enter num3: "));
res = find_max(num1, num2, num3);
print(f"The largest number is: {res}");
----------------------------------------
"""
"""
---------------------------------------------
def find_min(num1, num2, num3):
    if(num1<num2 and num1<num3):
        return num1;
    elif(num2<num1 and num2<num3):
        return num2;
    else: 
        return num3;
a=5;
b=11;
c=35;
res = find_min(a,b,c);
print(res);
------------------------------------------
"""
#defualt argument
"""
-------------------------------------------
def greet(name, message="Good Morning!"):
    return f"{message} {name}";

print(greet("Radhika", "Welcome to the session1"));
print(greet("Naman"));
-------------------------------------------
"""
#keyword argument-order doesn't matter
"""
-------------------------------------------
def total_marks(hindi, physics, maths, bio, chemistry):
    return hindi+maths+bio+physics+chemistry;
print(total_marks(maths=99, bio=89, chemistry=90, physics=84, hindi=99));
------------------------------------------
"""