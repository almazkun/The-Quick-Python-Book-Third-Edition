def power(x, y=2):
    """X in power y"""
    r = 1
    while y > 0:
        r = x * r
        y = y - 1
    return r


def max(*numbers):
    if len(numbers) == 0:
        return None
    else:
        maxnum = numbers[0]
        for n in numbers[1:]:
            if n > maxnum:
                maxnum = n
        return maxnum

