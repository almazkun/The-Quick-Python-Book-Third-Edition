def power(x, y=2):
    """ X in power y """
    r = 1
    while y > 0:
        r = x * r
        y = y - 1
    return r


def max(*numbers):
    """ Returns largest number """
    if len(numbers) == 0:
        return None
    else:
        maxnum = numbers[0]
        for n in numbers[1:]:
            if n > maxnum:
                maxnum = n
        return maxnum


def example_fun(x, y, **other):
    print("x: {0}, y: {1}, keys in 'other': {2}".format(x, y, list(other.keys())))
    other_total = 0
    for k in other.keys():
        other_total = other_total + other[k]
    print("The total of values in 'other' is {0}".format(other_total))


## Try this: Functions and parameters


def reversed(*params):
    x = []
    for i in params:
        x.append(i)
    rev = x.reverse()
    print(x, rev)

