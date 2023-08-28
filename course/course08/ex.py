# Recursive Functions 递归函数
# 1.Digit Sums
# 递归函数分为3大部分
j  # 函数头：和其他函数相同


# 结束调节：一个if statment,递的终点，从这开始归
# 递归体：返回值为函数本身，其中包含递归的逻辑
def split(n):
    """Split positive n into all but its last digit and its last digit."""
    return n // 10, n % 10


def sum_digits(n):
    """Return the sum of the digits of positive integer n."""
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


fact(3)


# Verifying Recursive Functions
# 1. Verify the base case
# 2. Treat fact as a functional abtraction!
# 3. Assumen that fact(n-1) is correct.
# 4. Verify that fact(n) is corrent, assuming that fact(n-1) correct.


# 相互递归函数Mutual Recursion
# luhn 算法（银行卡检查算法）
def split(n):
    return n // 10, n % 10


def sum_digits(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last


def luhn_sum(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last


def luhn_sum_double(n):
    all_but_last, last = split(n)
    luhn_digit = sum_digits(2 * last)
    if n < 10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit


# 递归函数转换为迭代函数
# 难点：递归本质上是一种特殊的迭代方式
# Idea: Figure out what state must be maintained by the interative function.
