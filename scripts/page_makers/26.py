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

    for i in range(0, 10):
        for x in range(0, 10):
            output += words_upper[i]
        output += "\n"
    

    # target_line = randint(1, 7)
    # for i in range(0,target_line):
    #     output += " ".join(spaces[:file_number])
    #     output += f" {words_upper[file_number]}"
    #     output += "\n"
    # # main line
    # output += " ".join(words_lower[:file_number]) 
    # output += f" {spaces[file_number]} "
    # output += ' '.join(words_lower[(file_number + 1):])
    # output += "\n"
    # for i in range(0, 6 - target_line):
    #     output += " ".join(spaces[:file_number])
    #     output += f" {words_upper[file_number]}"
    #     output += "\n"

    return output


for file_number in range(0,1):
    output_path = f'output/{base_filename}-{file_number}.txt'
    output_data = get_output(file_number)
    with open(output_path, 'w') as _file:
        _file.write(output_data)
    print(output_data)
