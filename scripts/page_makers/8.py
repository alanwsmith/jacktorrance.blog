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
    base_string = "".join(words)
    base_string = base_string.lower()
    for i in range(0,8):
        output += f"{base_string}\n"
    return output


for file_number in range(1,2):
    output_path = f'output/{base_filename}-{file_number}.txt'
    output_data = get_output()
    with open(output_path, 'w') as _file:
        _file.write(output_data)
    print(output_data)
