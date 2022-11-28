#!usr/bin/env python3

import os
import re

from random import randint

base_filename = os.path.basename(__file__).split('.')[0]

# Build list with each word having a random case
def random_case_word_list():
    random_list = []
    for word in word_sets['default']:
        if randint(0,1):
            random_list.append(word.upper())
        else:
            random_list.append(word.lower())
    return random_list

# Basic sentence with different cases for the words
def straight(*, case='default'):
    return " ".join(word_sets[case])

    # if case =='random':
    #     random_line = []
    #     for word in word_sets['default']:
    #         if randint(0,1):
    #             random_line.append(word.upper())
    #         else:
    #             random_line.append(word.lower())
    #     return " ".join(random_line)
    # else:
    #     return " ".join(word_sets[case])


# build a list with each 
def mixed_letters_word_list():
    mixed_case_assembly = [x for x in word_sets['default']]
    for i in range(0, len(mixed_case_assembly)):
        new_string = ""
        for letter in mixed_case_assembly[i]:
            if randint(0,1):
                new_string += letter.upper()
            else:
                new_string += letter.lower()
        mixed_case_assembly[i] = new_string
    return mixed_case_assembly

# output a single word at its default position 
def word_at_positions(*, positions, case='default'):
    line = []
    for i in range(0, len(word_sets['default'])):
        if i in positions:
            line.append(word_sets[case][i])
        else:
            line.append(word_sets['spaces'][i])
    return " ".join(line)

def letters_removed(*, letters=[], case='default'):
    return_list = []
    for word in word_sets[case]:
        updated_word = word
        for letter in letters:
            updated_word = re.sub(letter, ' ', updated_word)
        return_list.append(updated_word)
    return " ".join(return_list)

def only_letters(*, letters=[], case='default'):
    return_list = []
    for word in word_sets[case]:
        updated_word = word
        for letter in letters:
            updated_word = re.sub(r'[^' + letter + ']' , ' ', updated_word)
        return_list.append(updated_word)
    return " ".join(return_list)

def get_output(file_number):
    output = ''
    first_position = 4
    last_position = 5
    for i in range(0,4):
        output += word_at_positions(positions=[0,1, 5, 6, 7, 8, 9], case='upper')
        output += "\n"
    for i in range(2,-1,-1):
        output += word_at_positions(positions=[first_position - i], case='upper')
        output += "\n"
    output += word_at_positions(positions=[0, 1, 5,6,7,8,9], case='upper')
    return output

if __name__ == '__main__':
    word_sets = {}
    word_sets['default'] = ['All', 'work', 'and', 'no', 'play', 'makes', 'Jack', 'a', 'dull', 'boy']
    word_sets['upper'] = [x.upper() for x in word_sets['default']]
    word_sets['lower'] = [x.lower() for x in word_sets['default']]
    word_sets['spaces'] = [re.sub(r'\w', ' ', x) for x in word_sets['default']]
    word_sets['random'] = random_case_word_list()
    word_sets['mixed'] = mixed_letters_word_list()

    letter_sets = {}
    basic_lower_set = set()
    for word in word_sets['lower']:
        for letter in word:
            basic_lower_set.add(letter)
    letter_sets['lower_all'] = list(basic_lower_set)
    letter_sets['lower_all'].sort()

    basic_upper_set = set()
    for word in word_sets['upper']:
        for letter in word:
            basic_upper_set.add(letter)
    letter_sets['upper_all'] = list(basic_upper_set)
    letter_sets['upper_all'].sort()

    # for file_number in range(0,len(word_sets['default'])):
    # for file_number in range(0,len(letter_sets['lower_all'])):
    for file_number in range(0,1):
        output_path = f'output/{base_filename}-{file_number}.txt'
        output_data = get_output(file_number)
        with open(output_path, 'w') as _file:
            _file.write(output_data)
        print(output_data)
