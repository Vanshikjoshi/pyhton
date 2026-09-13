# strings in python - immutable, iterable-indexing allowed
"""
----------------------------------------
name = "Vanshika"
surname = "Joshi"
message = ""This is a
multiline-line string""
print(f"Hi {name} {surname} there is a message for you - {message}")
# name[0] = "b" // not possible
name = "Ruhana"  # here name isn't changed it is just override
print(name)
name = "A" + name[1:]  # this is possible
print(name)
# slicing
print(name[1:4])
email = "rahul@gmail.com"
print(email[: email.index("@")])  # extract name
print(email * 3)  # repeats 3 time
for i in email:
    print(i, end=" ")
print()
# membership operator
user_email = input("Enter the email: ")
if "@" in user_email and "." in user_email:
    print("Valid email")
else:
    print("Not valid")
------------------------------------------
"""

# practice questions
"""
---------------------------------------
name = input("Enter name: ")
print(
    f"1st char is {name[0]} last char is {name[-1]} and length is {len(name)}"
)  # print 1st,last and len of string
print(f"reverse is {name[-1::-1]}")  # reverse of string
count = 0
for i in name:
    if i in "aeiouAEIOU":
        print(i)
        count += 1
print(f"Total vowels are: {count}")  # count vowels
----------------------------------------------
"""
# string methods
"""
------------------------------------------
text = "hello world from Python"
print(text)
print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())  # only first char
print(text.swapcase())  # flips each
sentence = "Hello34"
print(sentence.isalpha())  # checks is all letters?
print(sentence.isalnum())  # checks is mix of num and letter
print(sentence.isdigit())  # checks if all digit
num = "67484"
print(num.isdigit())
sen = "Hello World"
print(" ".isspace())  # checks is all whitespace?
print(sen.isspace())
print(sen.startswith("Hel"))
print(sen.endswith("nois"))
print(sen.endswith("rld"))
print(sen.count("l"))
print(sen.index("o"))  # return error if not found
print(sen.find("l"))  # return -1 if not found
print(sen.find("i"))
print(sen.replace("World", "Earth"))
-------------------------------------------------
"""
# splitting and joining funcitons- split()-break string into list and join()- combine list into string
text = "Hello world, from python!"
print(text.split())  # bydefault whitespce is separator
print(text.split(","))
print(text.split("o"))
lst = ["v", "a", "n", "s", "h", "i", "k", "a"]
print("".join(lst))
print(type("".join(lst)))
# stip method- remove whitespaces from both ends of string
pythontext = " Hello world "
print(pythontext.strip())
# lstip-removes whitespace from left
# rstip-removes whitespace from right
url = "//https://www.code.com/"
print(url.strip("/https:/"))
print(url.lstrip("/"))
print(url.rstrip("/"))
