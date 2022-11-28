#!usr/bin/env python3

import os
import re

from random import randint 

base_filename = os.path.basename(__file__).split('.')[0]

words = ['All', 'work', 'and', 'no', 'play', 'makes', 'Jack', 'a', 'dull', 'boy']
spaces = [re.sub(r'\w', ' ', x) for x in words]
words_lower = [x.lower() for x in words]
words_upper = [x.upper() for x in words]

def get_output(file_number):
    output = ''

    for x in range(0, file_number + 2):
        for i in range(0, 11):
            output += "DULL"
        output += "\n"
    output += " "
    output += " ".join(words_lower)
    output += "\n"
    for x in range(0, file_number + 3):
        for i in range(0, 11):
            output += "DULL"
        output += "\n"

    return output


for file_number in range(0,3):
    output_path = f'output/{base_filename}-{file_number}.txt'
    output_data = get_output(file_number)
    with open(output_path, 'w') as _file:
        _file.write(output_data)
    print(output_data)
