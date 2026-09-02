
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
n=1
num = int(input("Enter a number: "));
print(f"The table of {num} is:");
while(n<=10):
    print(f"{num} * {n} = {num*n}");
    n+=1;
