# Lambda, map, filter, reduce examples
from functools import reduce

nums = [1, 2, 3, 4, 5]

# lambda map: square numbers
squares = list(map(lambda x: x * x, nums))
print('Squares:', squares)

# filter: keep even
evens = list(filter(lambda x: x % 2 == 0, nums))
print('Evens:', evens)

# reduce: sum
total = reduce(lambda a, b: a + b, nums, 0)
print('Total:', total)

# higher-order: function returning function
def make_multiplier(n):
    return lambda x: x * n

double = make_multiplier(2)
print('Double 7 ->', double(7))
