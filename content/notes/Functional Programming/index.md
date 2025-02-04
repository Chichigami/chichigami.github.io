# FP Basics

Functional programming (FP) is a style/paradigm of programming. We compose functions instead of mutating/updating variables.

- FP is more about declaring what you want to happen vs how you want it to happen
  `return walk(drink_water(create_person())))` - In this example, we never change the value of person variable, we compose functions that return new values with outermost function. `walk` returning final result.
- Imperative/Procedural programming declares what and the how.

```
person = create_person()
person.drink_water(10)
person.walk()
```

## Python not BiS

Python isn't best for FP for various reasons

- No static typing
- Mutable
- No tail call optimization
- Side effects are common
- Imperative & OOP styles are more popular
- Purity (pure functions) not enforced
- Sum types hard to define
- Pattern matching is weak

## Immutability

Immutability meaning not changable.
FP wants data to be immutable.
**WHY?**
Easier to work with when 10 different functions have access to same variable. Can't accidentally change it, so easier for debugging.

## Declarative Programming

FP wants to be declaraitive. Because of this programming style, FP tends to be more popular with mathimatical background.

`avg = Σx/N`

- Math equation isn't procedural. It's declarative.

Imperative programming example

```
def get_average(nums):
    total = 0
    for num in nums:
        total += num
    return total / len(nums)
```

Declaritive Programming example

```
def get_average(nums):
    return sum(nums) / len(nums)
```

## Classes vs Functions

If unsure, default to functions.

> Classes encourage you to think about the world as a hierarchical collection of objects. Objects bundle behavior, data, and state together in a way that draws boundaries between instances of things, like chess pieces on a board.

> Functions encourage you to think about the world as a series of data transformations. Functions take data as input and return a transformed output. For example, a function might take the entire state of a chess board and a move as inputs, and return the new state of the board as output.

Both are just styles of programming. Nothing superior. They both share some of the ideas of OOP. ![5bbb7583b7ef7537d275580d1e2b6477.png](/images/5bbb7583b7ef7537d275580d1e2b6477.png)
Inheritance isn't part of FP due to the nature of mutable classes.

## Debugging

It's hard to debug chains of functions. Break it down and print everything.

```
def get_player_position(position, velocity, friction, gravity):
    return calc_gravity(calc_friction(calc_move(position, velocity), friction), gravity)
```

# First class and higher order functions

First class function: You can use functions as values.
Higher Order Functions: A function that accepts another function as an argument or returns a function.

First class function example

```
def square(x):
	return x * x
f = square
```

Higher order function example

```
def square(x):
	return x * x
def my_map(func, list):
	result = []
	for number in list:
		result.append(func(number))
	return result
squared_list = my_map(square, [1, 2, 3, 4, 5])
print(squared_list)
# [1, 4, 9, 16, 25]
```

## Anonymous functions

First class function. They have no name.
In Python they're called lambda. Usually used for small, simple evals.

```
add_one = lambda x: x + 1
print(add_one(68))
# 69
```

## Common higher order functions

`Map Filter Reduce`

In Python, `map` takes a function and iterable, and applies the function to each element in the iterable and returns a new iterable. Like the example above.

`filter`: Takes a function and iterable and returns a new iterable that contains the resulting elements that returns true from the function.

```
def is_even(x):
	return x % 2 == 0
evens = list(filter(is_even, [1, 2, 3, 4, 5]))
print(evens)
# [2, 4, 6]
```

`Reduce`: From a library called functools. Takes a function and a list of values. Applies the function to each value in the list to accumulate a single result.

```
def add(sum, x):
	print(f"sum_so_far: {sum_so_far}, x: {x}")
	return sum + x
reduced_sum_list = functools.reduce(add, [1, 2, 3, 4, 5])
# sum_so_far: 1, x: 2
# sum_so_far: 3, x: 3
# sum_so_far: 6, x: 4
# sum_so_far: 10, x: 5
print(reduced_sum_list)
# 15
```

With these functions, we can avoid stateful iterations and mutations of variables.
Another example

```
import functools
def factorial(n):
    return functools.reduce(lambda x, y: x * y, range(1, n + 1))
```

There are more functions like `.intersection()` and `.zip()`

- Intersection takes 2 sets and will return a set where the elements are in both sets
- Zip takes 2 iterables and return a new interable where each element is a tuple based on their indexes.

```
a = [1, 2, 3]
b = [4, 5, 6]
c = list(zip(a, b))
print(c)
# [(1, 4), (2, 5), (3, 5)]
```

# Pure vs Impure function

Pure functions **always return the same value given the same arguments** and **running them causes no side effects**.

> **Pure functions don't do anything with anything that exists outside of their scope**
> Example of a pure function

```
def findMax(nums):
    max_val = float('-inf')
    for num in nums:
        if max_val < num:
            max_val = num
    return max_val
```

Example of an impure function

```
global_max = float('-inf')
def findMax(nums):
    global global_max
    for num in nums:
        if global_max < num:
            global_max = num
```

This function modifies the global_max variable.

Pure functions also do not perform I/O operations like reading from disk, accessing internet. or writing from console.

## Reference vs Value passed into a function

When passing value into a function. It can be by reference or by value.

- Reference: The function has access to the value, and can change it
  - Lists, Dictionaries, Sets
- Value: The funtion only has a copy of it. Changes to copy doesn't affect the original.
  - Integers, Floats, Strings, Booleans, Tuples

There are some nuances to this, but most collections are passed as references (besides tuples) and most primitive types are passed by values.

Because of references in Python, we can accidentally mutate values, thus leading to impurity.

Biggest difference between good and great devs is how often they can incorporate pure functions into their code. Pure functions are easier to read, easier to reason, easier to test, easier to combine.

## No-Op

This is an operation that does nothing. If a function doesn't return anything, it's probably impure because the only reason why it exist is to do a side effect.

```
y = 1
def add_to_y(x):
	global y
	y += x
print(add_to_y(2))
# 3
```

`global` allows Python to access the y outside of scope.

## Memoized

It's sort of like caching. Trade memory usage for speed. If function is fast enough no need to cache.

```
dict = {}
if new in dict.keys():
	dict[new] = compute[new]
else:
	return dict[new]
```

## I/O containment and conclusion

Because I/O are impure and overall some impurity is needed, this should be contained. So one part of the code base should be pure and another part should be impure.

## Function transformation

Sort of like multiplication and squaring a number

```
def functionName():
	def innerFunction(param):
		return whatYouWant
	return functionName
```

## Currying

```
function(1,2,3)
function(1)(2)(3)
```

## \*ARGS AND \*KWARGS

```
def args_logger(*args, **kwargs):
    for i in range(len(args)):
        print(f'{i+1}. {args[i]}')
    for key, value in sorted(kwargs.items()):
        print(f'* {key}: {value}')
args_logger("hi", True, age=24, f_name=Gary, l_name=Feng)
# 1. hi
# 2. True
# * age: 24
# * f_name: Gary
# * l_name: Feng
```

Accepts multiple arguments and key value dictionary argument

```
substitute(document, **edit)
def substitute(document, insert_text, line_number, start, end):
  #stuff
edit = {'insert_text': stuff, 'line_number': stuff, 'start': stuff, 'end': stuff}
```

Can name parameter based on the key string and it'll split it up
