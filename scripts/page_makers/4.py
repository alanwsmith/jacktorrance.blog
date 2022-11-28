#!usr/bin/env python3

import os
import random

base_filename = os.path.basename(__file__).split('.')[0]

words = ['All', 'work', 'and', 'no', 'play', 'makes', 'Jack', 'a', 'dull', 'boy']

line_order = [*range(0, len(words))]

for i in range(0, 5):
    output = ""
    random.shuffle(line_order)
    for line in line_order: 
        for word_index, word in enumerate(words):
            if word_index == line:
                output += f"{word}  "
            else:
                for space in range(0, len(word)):
                    output += ' '
                output += '  ' 
        output += "\n"
    output_path = f'output/{base_filename}-{i}.txt'

    with open(output_path, 'w') as _file:
        _file.write(output)

    print(output)
