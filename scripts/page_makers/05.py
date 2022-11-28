#!usr/bin/env python3

import os

from random import randint 

base_filename = os.path.basename(__file__).split('.')[0]

words = ['All', 'work', 'and', 'no', 'play', 'makes', 'Jack', 'a', 'dull', 'boy']

def get_output():
    output = ''
    line_count = randint(3,6)
    for line_num in range(0, line_count):
        newList = []
        for word in words:
            if randint(0,1) == 1:
                newList.append(word.upper())
            else:
                newList.append(word.lower())
        output += " ".join(newList)
        output += "\n"
    return output


for file_number in range(0,5):
    output_path = f'output/{base_filename}-{file_number}.txt'
    output_data = get_output()
    with open(output_path, 'w') as _file:
        _file.write(output_data)
    print(output_data)
