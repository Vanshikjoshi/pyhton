# pass by value and reference
def add(c):
    c = c + 1
    print(f"Inside function = {c}")


num = 10
add(num)  # 11
print(f"Outside function = {num}")  # 10


# for immutable objects like number it's value is passed not the reference
def add_item(x):
    x.append(100)
    print(f"Inside funtion= {x}")


nums = [3, 78, 56, 2]
add_item(nums)
print(f"Outside function={nums}")
# here for mutable objects it;s refernce is passed so the list changes outside the function also so use the shallow copy or deep copy for mutable objects


def add_mut(y):
    y = y.copy()
    y.append(100)
    print(f"Inside funtion= {y}")


number = [3, 78, 56, 2]
add_mut(number)
print(f"Outside function={number}")
