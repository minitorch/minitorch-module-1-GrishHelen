"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable


#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# Implement for Task 0.1.

def mul(num1, num2):
    return num1 * num2


def id(inp):
    return inp


def add(num1, num2):
    return num1 + num2


def neg(num):
    return -num


def lt(num1, num2):
    return num1 < num2


def eq(num1, num2):
    return num1 == num2


def max(num1, num2):
    return num2 if lt(num1, num2) else num1


def is_close(num1, num2, atol=1e-2):
    return abs(num1 - num2) < atol


def exp(num):
    return math.exp(num)


def inv(num):
    return 1 / num


def sigmoid(num):
    if lt(num, 0.0):
        return mul(exp(num), inv(add(1.0, exp(num))))
    return inv(add(1.0, exp(neg(num))))


def relu(num):
    return max(0.0, num)


def log(num):
    return math.log(num)


def log_back(num1, num2):
    return mul(num2, inv(num1))


def inv_back(num1, num2):
    return mul(num2, inv(mul(num1, num1)))


def relu_back(num1, num2):
    derivative = 1.0 if lt(0.0, num1) else 0.0
    return mul(derivative, num2)


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# Implement for Task 0.3.

def map(f: Callable, list_a: Iterable):
    res = []
    for a in list_a:
        res.append(f(a))
    return res


def zipWith(f: Callable, list_a: Iterable, list_b: Iterable):
    res = []
    for (a, b) in zip(list_a, list_b):
        res.append(f(a, b))
    return res


def reduce(f: Callable, list_a: Iterable):
    # used https://github.com/python/cpython/blob/282bd0fe98bf1c3432fd5a079ecf65f165a52587/Lib/functools.py#L238
    it = iter(list_a)

    try:
        value = next(it)
    except StopIteration:
        return None

    for element in it:
        value = f(value, element)
    return value


def negList(list_a):
    return map(neg, list_a)


def addLists(list_a, list_b):
    return zipWith(add, list_a, list_b)


def sum(list_a):
    if len(list_a) == 0:
        return 0
    return reduce(add, list_a)


def prod(list_a):
    return reduce(mul, list_a)
