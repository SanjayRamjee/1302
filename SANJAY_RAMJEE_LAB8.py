num_words = 0
lines = 0
words_per_line = 0
word_list = []
with open('example.txt', 'r') as file:
    for line in file:
        lines += 1
        words = line.split()
        words_per_line = len(words)
        word_list.append(words_per_line)
        num_words += len(words)

with open('output.txt', 'w') as output:
    output.write(f'Total number of words: {num_words}\n')
    output.write(f'Total number of lines: {lines}\n')
    output.write(f'Word count per line (line_number >> word_count):\n')
    for i in range(len(word_list)):
        output.write(f'Line {i+1} >> {word_list[i]} words\n')
