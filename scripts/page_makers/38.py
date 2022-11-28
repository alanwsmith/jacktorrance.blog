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
    new_words = []
    for i in range(0, len(words)):
        if i == file_number:
            new_words.append(words_upper[i])
        else:
            new_words.append(words_lower[i])

    output += " ".join(new_words[:file_number])
    output += "\n"
    output += "\n"
    output += "\n"
    output += " ".join(spaces[:file_number])
    output += " " +  new_words[file_number]
    output += "\n"
    output += "\n"
    output += "\n"
    output += " ".join(spaces[:(file_number + 1)])
    output += " " + " ".join(new_words[(file_number + 1):])

    return output


for file_number in range(0,10):
    output_path = f'output/{base_filename}-{file_number}.txt'
    output_data = get_output(file_number)
    with open(output_path, 'w') as _file:
        _file.write(output_data)
    print(output_data)
