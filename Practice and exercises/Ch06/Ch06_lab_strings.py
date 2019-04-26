punct = str.maketrans("", "", "!.,:;-?")


with open('moby_01.txt') as infile, open('moby_01_clean.txt', 'w') as outfile:
    for word in infile:
        cleaned_line = word.lower()
        cleaned_line = cleaned_line.translate(punct)
        words = cleaned_line.split()
        cleaned_words = '\n'.join(words) + '\n'
        outfile.write(cleaned_words)
