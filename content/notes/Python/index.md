# Python Basics

## Printing

```
print("Hello World")
# Hello World
count = 3
print(f"Count is {count}")
# Hello World
# Count is 3
```

Use `" "`

## Comparisons

```
==
and
or
```

## Types

```
int/float/complex
string
list, tuple, range
dict
set, frozenset
bool
bytes, bytearry, memoryview
NoneType
# to check the type
type(variable)
```

## Lists

```
list = [0,1,2,3,4,5,6,7,8,9]
# slicing a list [start: stop :step]
even_list = list[::2]
odd_list = list[1::2]
# print(even_list, odd_list)
# [0,2,4,6,9] [1,3,5,7,9]
```

Putting `:` in `[]` is called slicing

## Tuples

Collection of data that is ordered and unchangable.  
Sort of like a list w/ fixed size

```
tuple = ("yep", 69, True)
single_element_tuple = ("nope",)
multiple_tuples = [("1,2,3"),("4,5,6"),("7,8,9")]
# print(multiple_tuples[2,1])
# 4
```

## Dictionaries

Basically maps in other languages  
key -> value pair

```
person = {
    "age": 10
    "race": white
    "blood": O
}
# how to access an index of a dictionary
print(person["age"])
# 10
# del person["race"]
print (person)
# {age: 10, blood: O}
# adding a new key value pair
person['height'] = 169
```

If there are duplicate keys, the old one will be overwritten

## Set

unordered list but each element is unique

```
names = {'Bob', 'John', 'Sam'}
# adding element
names.add('Annie')
# removing element
names.remove('Bob')
# making an empty set
names = set()
# turning a set into a list
list(names)
# returning a list into a set
set(names)
```

## Errors

```
try:
    10/0
# received from the raise exception
except Exception as e:
    print(e)
raise Exception("can't divide by 0")
```
