def end(n, d):
    """Print the final digits of N in reverse order until D is found

    >>> end(34567, 5)
    7
    6
    5
    """
    while n > 0:
        last, n = n % 10, n // 10
        print(last)
        if d == last:
            return None


def search(f):
    x = 0
    while not f(x):
        x += 1
    return x


def is_three(x):
    return x == 3


def square(x):
    return x * x


def positive(x):
    return max(0, square(x) - 100)


def inverse(f):
    """Return g(y) such that g(f(x)) ---> x"""
    return lambda y: search(lambda x: f(x) == y)
