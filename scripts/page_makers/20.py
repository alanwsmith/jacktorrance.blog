#!usr/bin/env python3

import os
import re 

base_filename = os.path.basename(__file__).split('.')[0]
output_path = f'output/{base_filename}.txt'

words = ['All', 'work', 'and', 'no', 'play', 'makes', 'Jack', 'a', 'dull', 'boy']
spaces = [re.sub(r'\w', ' ', x) for x in words]
spaces_reversed = spaces
spaces_reversed.reverse()
words_lower = [x.lower() for x in words]
words_upper = [x.upper() for x in words]

output = ""

for i in range(0, len(words) + 1):
    output += " ".join(spaces_reversed[:-i])
    if i != len(words):
        output += " "
    output += " ".join(words[0:i])
    output += "\n"

with open(output_path, 'w') as _file:
    _file.write(output)


print(output)

