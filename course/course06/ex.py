from math import sqrt

# Functional Abstractions


def square(x):
    return mul(x, x)


def sum_squares(x, y):
    return square(x) + square(y)


"""When we use function, we don't need to understand the detial of the function implment
In this case:
When we use sum_squrae(x, y)
we don't need to know how square run in detail
we just know how to use suqare(x) function
"""

# Choosing Names
"""函数命名规则:
1. 命名应该能够描述函数的功能
2. 在docstring中,编写函数参数的含义
3. 常见的命名形式:
  1. 描述作用(effect): print
  2. 描述行为(behavior): triple
  3. 返回值(returned value): abs
"""

# #Which Value Deserve a Name
# ##重复的表达式

a = 1
b = 2
x = 1
# ###Bad implement
if sqrt(square(a) + square(b)) > 1:
    x = x + sqrt(square(a) + square(b))
# ###Good implement
hypotenuse = sqrt(square(a), square(b))
if hypotenuse > 1:
    x = x + hypotenuse

# ##重要的,有含义的表达式
# ## 变量名可以很长，只要可读性强即可
# ## 对于一些常用的，通用的变量，也可以使用单个字母
"""
n, k, i - Usually intergers
x, y, z - Usually real numbers
f, g, h - Usually funcitons
"""
