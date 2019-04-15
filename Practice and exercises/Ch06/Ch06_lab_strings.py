text = []
with open('moby_01.txt') as infile, open('moby_01_clean.txt', 'w') as outfile:
    for word in infile:
        word.lower()

        text = text.append(word.lower().rstrip())

text

        # delete poctuations
        # split
        # make rows
        outfile.write(cleaned_words)
