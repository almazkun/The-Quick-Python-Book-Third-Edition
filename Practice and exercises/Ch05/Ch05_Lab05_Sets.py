temperatures = []
with open('lab_05.txt') as infile:
    for row in infile:
        temperatures.append(float(row.strip()))


min_tem = min(temperatures)
max_tem = max(temperatures)
avr_tem = sum(temperatures)/len(temperatures)
temperatures.sort()
median = temperatures[len(temperatures)//2]
unique = len(set(temperatures))


def results():
    print('Lowest temperature: {}'.format(min_tem))
    print('Highest temperature: {}'.format(max_tem))
    print('Average temperature: {}'.format(avr_tem))
    print('Median temperature: {}'.format(median))
    print('Unique temperatures: {}'.format(unique))


results()

