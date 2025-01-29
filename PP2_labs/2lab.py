#Python Booleans

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#Python Operators

print(5 + 4 - 7 + 3)
print(100 + 5 * 3)

#Python Lists

list1 = ["abc", 34, True, 40, "male"]

#Python - Access List Items

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#Python - Change List Items

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#Python - Add List Items

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#Python - Remove List Items

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#Python - Loop Lists

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#Python - List Comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


#Python - Sort Lists

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#Python - Copy Lists

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

#Python - Join Lists

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

#Python - List Methods

fruits = ['apple', 'banana', 'cherry']

x = fruits.index("cherry")

#Python Tuples

thistuple = ("apple",)
print(type(thistuple))

thistuple = ("apple")
print(type(thistuple))

#Python - Access Tuple Items

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#Python - Update Tuples

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

#Python - Unpack Tuples

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

#Python - Loop Tuples

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

#Python - Join Tuples

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

#Python - Tuple Methods

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8)

print(x)

#Python Sets

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#Python - Access Set Items

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#Python - Add Set Items

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#Python - Remove Set Items

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#Sets Loop

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#Join Sets

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)

#Python - Set Methods

x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}

z = x.issuperset(y)

print(z)

#Python Dictionaries

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#Access Dictionary Items

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

#Python - Change Dictionary Items

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

#Add Dictionary Items

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

#Python - Remove Dictionary Items

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

#Python - Loop Dictionaries

for x in thisdict.values():
  print(x)

#Copy Dictionaries

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

#Nested Dictionaries

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

#Python Dictionary Methods

x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x, y)

print(thisdict)

#Python If ... Else

a = 33
b = 200
if b > a:
  print("b is greater than a")

#Python While Loops

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#For loop

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)