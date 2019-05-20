#!/usr/bin/env python

import math

# Using lists examples
my_first_list = ["hello", "world"]
another_list = ["hello", 12.5]

# Anything can be placed in a list
objects_in_a_list = [math.sin, 12.5, math.pi]
print(objects_in_a_list[0](math.pi))

# Nested lists (list within a list)
nesting_list = [
    [0, 2],
    [1, 4],
    [2, 6],
]

# How to append new values to the end of a list
nesting_list.append([3, 8])
nesting_list.append([7, 10, "my_result"])

# How to update a list element "in place"
print(nesting_list)  # Check list before you change things
nesting_list[0] = [10, 12]
print(nesting_list)  # check list after you change things

# How to join lists
join_me1 = [[0, 2], [1, 4]]
join_me2 = [[2, 6], [3, 8]]
print(join_me1 + join_me2)

# Using dictionaries examples
my_first_dictionary = {
    "key1": "value1"
}

# Like lists, you can put whatever you like in a dictionary
nesting_list_in_dictionary = {
    "my_list": [[0, 2], [1, 4], [2, 6]],
    "results": {
        "run1": 10,
        "run2": 15,
    }
}

# Use your keys to access a list item
print(nesting_list_in_dictionary["results"])
print(nesting_list_in_dictionary["results"]["run1"])

# Runnign nesting_list_in_dictionary["run1"] will give you
# an error. If you want to handle this gracefully and not
# crash your program, use the .get() method
print(nesting_list_in_dictionary.get("run1"))  # Returns None
print(nesting_list_in_dictionary.get("run1", "Doesn't exist"))  # Returns "Doesn't exist"
print(nesting_list_in_dictionary.get("results"))  # Returns {"run1": 10, "run2": 15}

# Both of these will return the same thing
print(nesting_list_in_dictionary["results"]["run1"])
print(nesting_list_in_dictionary.get("results").get("run1"))

# Creating a tuple from an existing list
example_tuple = tuple(nesting_list)

# Manually create a tuple
manual_tuple = (10, 12, 5)

# Tuples can be accessed similar to lists
print(example_tuple[0])

# But you cannot change values inside a tuple
# The following is not allowed, and is commented out so
# it doesn't cause a runtime error
#
# example_tuple[0] = ["new", "values"]

# Sets let you find unique values in a list of values
example_set = set([10, 12, 15, 10])
print(example_set)

# for loops in Python
# Most basic example with range()
for i in range(10):
    print(i)

# Usually, you want to use values that change with each loop
# Here we find the cumulative sum of the numbers 0 through 9
population = 0
print(population)
for i in range(10):
    population += i
    print(population)

# Putting lists in loops iterates over each value in sequence
for item in nesting_list:
    print("element 1 =", item[0])
    print("element 2 =", item[1])
    
# Looping over dictionaries is similar, but requires that you
# take the variable storing the dictionary and add .items()
# on the end of it.
for key, value in nesting_list_in_dictionary.items():
    print(key, value)
    
# DON'T USE COUNTER VARIABLES
# A counter variable in other languages is needed if you want to
# access an array or list sequentially. In Python, it would look
# like this
for i in range(7):
    print(nesting_list[i])
    
# The "Pythonic" way to access elements of a list would be this:
# Take note, in this example, i contains values taken from the
# list. In the previous example, i just takes on integer values
# 0 through 6
for i in nesting_list:
    print(i)
    
# If you need the index values along with the list values, use
# the enumerate() function as follows:
for index, value in enumerate(nesting_list):
    print(index, value)

################################################################

a = [1, 2]
print(a)

def test_case(input1):
    input1.append(3)
    

test_case(a)
print(a)    
    
    
def test_case_alt():
    return 3

a = [1, 2]
print(a)
tmp_var = test_case_alt()
a.append(tmp_var)
print(a)


