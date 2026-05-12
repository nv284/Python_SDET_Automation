from functools import reduce

def stats(nums):
    total = 0
    count = 0
    for n in nums:
        total += n
        count += 1
    avg = total / count if count else 0
    # min and max
    if count:
        minimum = nums[0]
        maximum = nums[0]
        for n in nums:
            if n < minimum:
                minimum = n
            if n > maximum:
                maximum = n
    else:
        minimum = 0
        maximum = 0
    return {'total': total, 'count': count, 'avg': avg, 'min': minimum, 'max': maximum}
