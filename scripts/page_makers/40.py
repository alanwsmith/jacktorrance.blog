#!usr/bin/env python3

import os
import re

from random import randint 

base_filename = os.path.basename(__file__).split('.')[0]

words = ['All', 'work', 'and', 'no', 'play', 'makes', 'Jack', 'a', 'dull', 'boy']
spaces = [re.sub(r'\w', ' ', x) for x in words]
words_lower = [x.lower() for x in words]
words_upper = [x.upper() for x in words]

def straight_sentence(*, case=None):
    if case == 'upper':
        return " ".join(words_upper)
    if case == 'lower':
        return " ".join(words_lower)
    if case =='random':
        random_line = []
        for word in words:
            if randint(0,1):
                random_line.append(word.upper())
            else:
                random_line.append(word.lower())
        return " ".join(random_line)
    else:
        return " ".join(words)



# mixed_case = [x for x in words]
# for i in range(0, len(mixed_case)):
#     new_string = ""
#     for letter in mixed_case[i]:
#         if randint(0,1):
#             new_string += letter.upper()
#         else:
#             new_string += letter.lower()
#     mixed_case[i] = new_string


def get_output(file_number):
    output = ''
    output += straight_sentence(case='upper')
    output += "\n"
    for i in range(0, 5):
        output += straight_sentence(case='lower')
        output += "\n"
    output += straight_sentence(case='upper')
    return output


# This one is currently turned off as the last one that this 
# genrates is hard coded so it stays in place

for file_number in range(0,1):
    output_path = f'output/{base_filename}-{file_number}.txt'
    output_data = get_output(file_number)
    with open(output_path, 'w') as _file:
        _file.write(output_data)
    print(output_data)
