#!usr/bin/env python3

import os
base_filename = os.path.basename(__file__).split('.')[0]
output_path = f'output/{base_filename}.txt'

words = ['All', 'work', 'and', 'no', 'play', 'makes', 'Jack', 'a', 'dull', 'boy']

output = ""

for i in range(0, len(words), 2):
    output += f"{words[i].lower()} {words[i+1].lower()}\n"

with open(output_path, 'w') as _file:
    _file.write(output)

print(output)
