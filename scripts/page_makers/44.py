#!usr/bin/env python3

import os
import re

from random import randint 

base_filename = os.path.basename(__file__).split('.')[0]

words = ['All', 'work', 'and', 'no', 'play', 'makes', 'Jack', 'a', 'dull', 'boy']
spaces = [re.sub(r'\w', ' ', x) for x in words]
words_lower = [x.lower() for x in words]
words_upper = [x.upper() for x in words]

word_sets = {}
word_sets['default'] = ['All', 'work', 'and', 'no', 'play', 'makes', 'Jack', 'a', 'dull', 'boy']
word_sets['upper'] = [x.upper() for x in word_sets['default']]
word_sets['lower'] = [x.lower() for x in word_sets['default']]
word_sets['spaces'] = [re.sub(r'\w', ' ', x) for x in words]



def straight_sentence(*, case='default'):
    if case =='random':
        random_line = []
        for word in word_sets['default']:
            if randint(0,1):
                random_line.append(word.upper())
            else:
                random_line.append(word.lower())
        return " ".join(random_line)
    else:
        return " ".join(word_sets[case])

def mixed_case_letters():
    mixed_case = [x for x in word_sets['default']]
    for i in range(0, len(mixed_case)):
        new_string = ""
        for letter in mixed_case[i]:
            if randint(0,1):
                new_string += letter.upper()
            else:
                new_string += letter.lower()
        mixed_case[i] = new_string
    return " ".join(mixed_case)

def word_at_positions(*, positions, case='default'):
    line = []
    for i in range(0, len(word_sets['default'])):
        if i in positions:
            line.append(word_sets[case][i])
        else:
            line.append(word_sets['spaces'][i])
    return " ".join(line)


def get_output(file_number):
    output = ''
    for i in range(0,3):
        output += word_at_positions(positions=range(0,2), case='lower')
        output += "\n"
        output += word_at_positions(positions=range(0,5), case='lower')
        output += "\n"
        output += word_at_positions(positions=range(0,7), case='lower')
        output += "\n"

    output += word_at_positions(positions=range(7,10), case='upper')

    return output


# This one is currently turned off as the last one that this 
# genrates is hard coded so it stays in place

for file_number in range(0,1):
    output_path = f'output/{base_filename}-{file_number}.txt'
    output_data = get_output(file_number)
    with open(output_path, 'w') as _file:
        _file.write(output_data)
    print(output_data)
