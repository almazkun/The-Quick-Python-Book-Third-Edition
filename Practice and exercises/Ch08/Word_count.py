"""Reads a file and returns count of lines, words and characters"""
line_count = 0
word_count = 0
char_count = 0

with open('word_count.tst') as infile:
    for line in infile:
        line_count += 1
        char_count += len(line)
        words = line.split()
        word_count = len(words)


print('File has {0} lines, {1} words, {2} characters'.format(line_count, word_count, char_count))
