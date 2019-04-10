with open('moby_01.txt') as infile, open('moby_01_clean', 'w') as outfile:
    for word in infile:
        word.lower()
        text = word.translate('-')

text
        # text lowercased
        # delete poctuations
        # split
        # make rows
        outfile.write(cleaned_words)
