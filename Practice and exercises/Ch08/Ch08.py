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

