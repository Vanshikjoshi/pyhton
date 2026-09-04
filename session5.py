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
def factors(num):
    for i in range(1,num+1):
        if(num%i == 0):
            print(i,end=" ");

n = input("Enter a number to find its factors: ")
factors(int(n));
