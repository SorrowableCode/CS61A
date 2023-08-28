"""Our first Python source file."""

from operator import floordiv,mod
def divide_exact(n, d):
    """Return the quotient and reminder of divding N by D
    
    >>> q, r = divide_exact(2013, 10)
    >>> q
    201
    >>> r
    3
    """ 
    return floordiv(n, d), mod(n, d)

def absolute_value(x):
    """Reuturn the absolute value of x."""
    if x < 0:
        return -x
    elif x == 0:
        return 0
    else:
        return x

def fib(n):
    """Compute the nth Fibonacci number, for N >= 1."""
    if n == 0:
        return 0
    pred, curr = 0, 1 #0th and 1st Fibonacci numbers
    k = 1 # curr is the kth Fibonacci number
    while k < n:
        pred, curr = curr, pred + curr
        k = k + 1
    return curr


# Return section
def search(f):
    """Find x for the less positive value of a function"""
    x = 0
    while not f(x):
        x += 1
    return x

def is_three(x):
    """True when x equal three"""
    return x == 3

def square(x):
    return x * x

def positive(x):
    return max(0, square(x) - 100)

def inverse(f):
    """Return g(y) such that g(f(x)) -> x."""
    return lambda y: search(lambda x : f(x) == y)

def if_(c, t, f):
    if c:
        t
    else:
        f

from math import sqrt

def real_sqrt(x):
    if_(x > 0, sqrt(x), 0.0)

def has_big_sqrt(x):
    return x > 0 and sqrt(x) > 10

def reasonable(n):
    return n == 0 or 1/n != 0