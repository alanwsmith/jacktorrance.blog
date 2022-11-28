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
    for i in range(0,4):
        base_string = "".join(words)
        base_string = base_string.lower()
        base_list = list(base_string)
        new_list = [x.upper() if randint(0,1) == 1 else x.lower() for x in base_list]
        output += f"{''.join(new_list)}\n"
        output += "\n"
    return output


for file_number in range(1,2):
    output_path = f'output/{base_filename}-{file_number}.txt'
    output_data = get_output()
    with open(output_path, 'w') as _file:
        _file.write(output_data)
    print(output_data)
