#!usr/bin/env python3

import os
base_filename = os.path.basename(__file__).split('.')[0]
output_path = f'output/{base_filename}-0.txt'

words = ['All', 'work', 'and', 'no', 'play', 'makes', 'Jack', 'a', 'dull', 'boy']

output = ""

for i in range(0, len(words)):
    output += " ".join(words[0:i+1])
    output += "\n"

with open(output_path, 'w') as _file:
    _file.write(output)


