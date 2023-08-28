def likes(n):
    """Returns whether George Boole likes the non-negative interger n."""


def mystery1(n):
    k = 1
    while k < n:
        if likes(n):
            print(k)
        k = k + 2


# Generating Enviroment Diagram
def flip(flop):
    if flop > 2:
        return None
    flip = lambda flip: flip + 2
    return flip


def flop(flip):
    return flop


flip, flop = flop, flip
flip(flop(1)(2))(3)


# Implementing Functions
def remove(n, digit):
    """Return all digits of non-negative N
    that are not DIGIT, for some
    non-negative DIGIT less than 10.

    >>> remove(231, 3)
    21
    >>> remove(243132, 2)
    4313
    """
    digits, kept = 0, 0
    while n:
        last = n % 10
        n = n // 10
        if last != digit:
            kept += last * 10**digits
            digits += 1
    return kept


# Decorators装饰器
# 使用高阶函数的特性
def trace1(fn):
    """Returns a version of fn that first print when
    it is called

    fn - a function of 1 argument
    """

    def traced(x):
        print("Calling", fn, "on argument", x)
        return fn(x)

    return traced


@trace1
def square(x):
    return x * x


@trace1
def sum_squares_up_to(n):
    k = 1
    total = 0
    while k <= n:
        total, k = total + square(k), k + 1
    return total
