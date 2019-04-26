### Try this:


## Create Dictionary

name_age = {'one': 1, 'two': 2, 'three': 3}
for i in range(3):
    name = input('Name: ')
    age = int(input('Age: '))
    name_age[name] = age

name_choice = input('Name to find: ')
print(name_age[name_choice])


## Operations on dictionaries

x = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
y = {'a': 6, 'e': 5, 'f': 6}

del x['d']
print(x)

z = x.setdefault('g', 7)
print(x)

x.update(y)
print(x)


## Possible keys to dictionaries

possible_keys = [1, 'bob',   "filename", ("filename",  "extension")]
impossible_keys = [('tom', [1, 2, 3]), ["file-name"]]


## Working with Dictionaries

sheet = {}
sheet[('A', 1)] = 100
sheet[('B', 1)] = 1000

print(sheet[('A', 1)])


### LAB WORK #07

moby_words = []

with open('moby_01_clean.txt') as infile:
    for word in infile:
        moby_words.append(word.strip())


word_count = {}
for word in moby_words:
    count = word_count.setdefault(word, 0)
    count += 1
    word_count[word] += 1


word_list = list(word_count.items())
word_list.sort(key=lambda x: x[1])
print('Most common words: ')
for word in reversed(word_list[-5:]):
    print(word)
print('\nLeast common words: ')
for word in word_list[:5]:
    print(word)

