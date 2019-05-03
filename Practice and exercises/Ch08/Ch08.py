### Try this:


## If and cicles
x = [1, 3, 5, 0, -1, 3, -2]
for i in x:
    if i < 0:
        x.remove(i)

print(x)


y = [[1, -1, 0], [2, 5, -9], [-2, -3, 0]]
count = 0
for n in y:
    for i in n:
        if i < 0:
            count += 1

print(count)


number = -5

if number < -5:
    print('Very low')
elif number < 0:
    print('Low')
elif number == 0:
    print('Neutral')
elif number < 5:
    print('High')
else:
    print('Very high')


## Try this: Comprehension
x = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
x = [i for i in x if i > 0]


x = [i for i in range(100) if i % 2]


x = {i: i**3 for i in range(11, 16)}


## Try This: Ligical expressions and is True
1 == True

0 == False

-1 == True

[0] True

1 and 0 == False

1 > 0 or [] == True

