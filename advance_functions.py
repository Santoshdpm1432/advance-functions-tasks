# Lambda Function:
# Definition: A lambda function is an anonymous function in Python, defined
# using the lambda keyword. It is often used for short, one-time operations.


# lambda arguments: expression
# add = lambda x, y: x + y
# result = add(3, 5)
# print(result) 


# def square(a):
#     return a**5
# obj = square(5)
# print(obj)


# Filter Function:

# Definition: the filter function is an advanced function that is used to filter
# elements from an iterable (e.g., a list) based on a specified function for which
# the provided function returns True

# Syntax:
# filter(function, iterable)

# list_of_numbers = [1,2,3,4,5,6,7,8,9,10]
# def odd(i):
#     return i % 2 != 0
# result = filter(odd,list_of_numbers)
# print(list(result))

# list_of_numbers = [1,2,3,4,5,6,7,8,9,10]
# def even(i):
#     return i % 2 == 0
# result = filter(even,list_of_numbers)
# print(list(result))


# lambda arg:exp
# filter(function,iterable)



# Use cases:
# Transforming data: Apply a function to each element of a list to transform it
# into another form.
# Performing element-wise operations on multiple iterables simultaneously.
# Generating new sequences based on existing data.


# Higher-Order Functions

# A function that takes another function as an argument or returns a function.

# Example: Using map(), filter(), and reduce()



# from functools import reduce

# numbers = [1, 2, 3, 4, 5]

# squared = list(map(lambda x: x ** 2, numbers))
# print(squared)  # Output: [1, 4, 9, 16, 25]

# # filter() selects elements that satisfy a condition
# evens = list(filter(lambda x: x % 2 == 0, numbers))
# print(evens)  # Output: [2, 4]

# # reduce() applies a function cumulatively
# product = reduce(lambda x, y: x * y, numbers)
# print(product)  # Output: 120

# Function Decorators

# A decorator is a function that modifies another function’s behavior.


# Example: Creating a Timer Decorator

import time

# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"{func.__name__} took {end - start:.4f} seconds")
#         return result
#     return wrapper

# @timer
# def slow_function():
#     time.sleep(2)
#     print("Function finished")

# slow_function()


# Recursive Functions

# A function that calls itself to solve a problem.

# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n - 1)

# print(factorial(5))  # Output: 120

# Generator function

# Generator-Function : A generator-function is defined like a normal function,
# but whenever it needs to generate a value, it does with the yield keyword rather
# than return. If the body of a def contains yield, the function automatically
# becomes a generator function.

# def count_up_to(n):
#     count = 1
#     while count <= n:
#         yield count
#         count += 1

# gen = count_up_to(5)
# for num in gen:
#     print(num)  # Output: 1 2 3 4 5


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for _ in range(5):
    print(next(fib))  # Output: 0 1 1 2 3


