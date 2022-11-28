#!usr/bin/env python3

import os
import re

from random import randint 

base_filename = os.path.basename(__file__).split('.')[0]

words = ['All', 'work', 'and', 'no', 'play', 'makes', 'Jack', 'a', 'dull', 'boy']
spaces = [re.sub(r'\w', ' ', x) for x in words]
words_lower = [x.lower() for x in words]
words_upper = [x.upper() for x in words]

def get_output():
    output = ''
    for i in range(0,5):
        if i == 0 or i == 2 or i == 4:
            output += f"{' '.join(words_upper[:2])}        "
        else:
            output += f"{' '.join(words_lower[:2])}        "
    output += "\n"
    for i in range(0,5):
        if i == 0 or i == 2 or i == 4:
            output += f"{' '.join(words_upper[2:5])}     "
        else:
            output += f"{' '.join(words_lower[2:5])}     "
    output += "\n"
    for i in range(0,5):
        if i == 0 or i == 2 or i == 4:
            output += f"{' '.join(words_upper[5:7])}      "
        else:
            output += f"{' '.join(words_lower[5:7])}      "
    output += "\n"
    for i in range(0,5):
        if i == 0 or i == 2 or i == 4:
            output += f"{' '.join(words_upper[7:10])}      "
        else:
            output += f"{' '.join(words_lower[7:10])}      "
    output += "\n"
    return output


for file_number in range(1,2):
    output_path = f'output/{base_filename}-{file_number}.txt'
    output_data = get_output()
    with open(output_path, 'w') as _file:
        _file.write(output_data)
    print(output_data)
