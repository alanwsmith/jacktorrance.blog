#!usr/bin/env python3

import os
import re

from random import randint 

base_filename = os.path.basename(__file__).split('.')[0]

words = ['All', 'work', 'and', 'no', 'play', 'makes', 'Jack', 'a', 'dull', 'boy']
spaces = [re.sub(r'\w', ' ', x) for x in words]

print(spaces)

def get_output():
    output = ''
    for line_number in range(0,11):
        if line_number == 0:
            output += " ".join(words) + "\n"
        else:
            output += " ".join(words[:2])
            output += " "
            output += " ".join(spaces[2:5])
            output += " "
            output += " ".join(words[5:10])

            output += "\n"
    return output


for file_number in range(1,2):
    output_path = f'output/{base_filename}-{file_number}.txt'
    output_data = get_output()
    with open(output_path, 'w') as _file:
        _file.write(output_data)
    print(output_data)
