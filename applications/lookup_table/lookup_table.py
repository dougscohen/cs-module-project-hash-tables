import random
import math


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v


cache = {}

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # raise x to the y power
    v = math.pow(x, y)

    # if v is not in cache
    if v not in cache:
        # find the factorial of that number and add to cache
        cache[v] = math.factorial(v)
        # divide that number by (x + y) and add to cache
        cache[v] //= (x + y)
        # find the remainder of that number divided by 982451653 and add to cache
        cache[v] %= 982451653

    # otherwise, return the value at key v
    value = cache[v]

    return value



# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
