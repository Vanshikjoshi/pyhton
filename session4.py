
"""
count = 1;
sum = 0;
num = 1;
while(count<=100):
    if(count%3==0 and count%5==0):
        print(count);
    count+=1;
while(num<=100):
    sum  += num;
    num+=1;
print(sum);
"""
#---------------------------------------
"""
num = 1;
sum = 0;
while(num<=100):
    if(num%2==0 and num%7==0):
        sum+=num;
    num+=1;
print(sum);
"""
#------------------------------------------
"""
n=1
num = int(input("Enter a number: "));
print(f"The table of {num} is:");
while(n<=10):
    print(f"{num} * {n} = {num*n}");
    n+=1;
"""
#for loop
"""
for i in range(1,11,2):
    print(i);
for n in range(10,0,-1):
    print(n, end=" ");

sum = 0;
for i in range(1,11):
    sum+=i;
print(f"\nThe sum is : {sum}");
#concept of break
for i in range(1,12):
    if(i==11):
        break;
    if(i%2==0):
        continue;
    print(i);
"""
#practice questions------------------
"""
sum = 0;
while(True):
    num = int(input("Enter a number: "));
    if(num<0):
        continue;
    elif(num>0):
        sum+=num;
    else:
        break;
print(f"The sum of all positive numbers: {sum}");
"""

    