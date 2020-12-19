import cv2
import math

print("Hello World \n")

print(math.gcd(3, 6))

print(5 + 8)

# variables

a = 74
b = 52
c = 25
d = 52.62

print(a + b)
print(a + c)
print(a - c)
print(a + d)

# type of variables

print(type(d))

# type casting

e = "52"
print(e)

e = int(e)

print(type(e))
print(e + 4)

# Strings

name = "Mark"

print(name)

print(name[0])
print(name[2:3])
print(name.strip())  # remove extra spaces
print(len(name))
print(name.lower())
print(name.upper())
print(name.replace("k", "e"))

name1 = "Mark"
name2 = "is a good boy"

# temp = "His name is {} and he {}".format(name1, name2)

temp = f"His name is {name1} and he {name2}"

print(temp)

# Operators

print(2 ** 3)
print(4 // 5)
print(5 % 6)

# List

lst = [2, 3, 6, 7, 8, 0, 9]

print(lst)

lst.append(100)
print(lst)

lst.pop()
print(lst)

lst.remove(8)
print(lst)

lst.insert(1, 5)
print(lst)

var = len(lst)
print(var)

var = lst[1:4]
print(var)

lst.clear()
print(lst)

# Tuple
 
tup = (2, 3, 5, 6, 7 , 9)

print(tup)
print(type(tup))

var = list(tup)
print(var)

# Set

s1 = {1, 3, 4, 5, 6, 7, 8, 9, 5, 7, 3, 2}
s2 = {1, 2, 4, 5, 6, 7, 8, 9, 3, 0, 2, 4}

print(s1)
print("The union is", s1.union(s2))
print("The intersection is", s1.intersection(s2))
print(len(s1))

s1.pop()
print(s1)

s1.clear()
print(s1)

# Dictonary

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)
print(thisdict["model"])

thisdict["model"] = "Swift"
print(thisdict)

thisdict.pop("model")
print(thisdict)

# conditional statement

age = input("Enter your age")
age = int(age)

print(age)

if(age > 18):
    print("You can vote")
else:
    print("You can not vote")

# Loops

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

i = 1
while (i < 100):
  print(i + 1)
  i += 1

# Functions

def sum(a, b):
    c = a + b
    return c

print("the sum is", sum(2, 4))

# Oops


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

x = ['ab', 'cd']

print(list(map(list, x)))

z = float(3)

print(z)

list1 = ["abc", 34, True, 40, "male"]

print(list1)

print(2 * 3 ** 3 * 4)

x = 100

y = 50 

print(x and y)

a = [10, 20]

b = a 

b += [30, 40]

print(a)
print(b)

tuple1 = (1120, 'a')

print(max(tuple1))

