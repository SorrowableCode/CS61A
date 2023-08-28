# def apply_twice(f, x):
#     return f(f(x))


# def square(x):
#     return x * x


# result = apply_twice(square, 2)
# print(result)


# Nested Definitions Function
# def make_adder(n):
#     def adder(k):
#         return k + n

#     return adder


# The obver function is a Definitions Functions
# If you use the Python tutor to draw ENviroment Diagram.
# You will see the parent's of the fufnction


# Function Composition
# def square(x):
#     return x * x


# def triple(x):
#     return x * 3


# def compose1(f, g):
#     def h(x):
#         return f(g(x))

#     return h


# print(compose1(square, triple)(3))


# Self-Refernce
def print_sum(x):
    print(x)

    def next_sum(y):
        return print_sum(x + y)

    return next_sum


print_sum(1)(3)(5)


# Function Currying
def curry2(f):
    def g(x):
        def h(y):
            return f(x, y)

        return h

    return g
