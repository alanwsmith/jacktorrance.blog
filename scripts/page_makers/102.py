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
def words_at_positions(*, positions, case='default'):
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
    lines = [''] * (len(word_sets['upper']))

    for i in range(0, len(word_sets['upper'])):
        for x in range(0, len(word_sets['upper'])):
            if x == file_number: 
                lines[i] += word_sets['upper'][x] + " "
            else:
                if i == file_number:
                    lines[i] += word_sets['lower'][x] + " " 
                else:
                    lines[i] += word_sets['spaces'][x] + " "



    return "\n".join(lines)

    # total_lines = randint(6, 12)
    # target_line = randint(1,total_lines)

    # scatter_lines = []
    # for i in range(0, total_lines):
    #     new_line = ""
    #     while len(new_line) < 28:
    #         new_line += word_sets['lower'][randint(0,len(word_sets['upper']) - 1)]
    #         new_line += " " * randint(1, 10)
    #     scatter_lines.append(new_line)

    # max_line_length = 0
    # for line in scatter_lines:
    #     max_line_length = max(max_line_length, len(line))
    # output_line = words_at_positions(positions=[2, 3, 4, 5, 6, 7, 8, 9], case='lower')
    # output_line = (" " * 14) + straight(case='upper') 

    # padding = int((max_line_length - len(output_line)) / 2)

    # for i in range(0, target_line):
    #     output += scatter_lines[i]
    #     output += "\n"

    # output += "\n"
    # # output += " " * padding
    # output += output_line 
    # output += "\n"
    # output += "\n"

    # for i in range(target_line, total_lines):
    #     output += scatter_lines[i]
    #     output += "\n"



if __name__ == '__main__':
    word_sets = {}
    word_sets['default'] = ['All', 'work', 'and', 'no', 'play', 'makes', 'Jack', 'a', 'dull', 'boy']
    word_sets['upper'] = [x.upper() for x in word_sets['default']]
    word_sets['lower'] = [x.lower() for x in word_sets['default']]
    word_sets['capital'] = [x.capitalize() for x in word_sets['default']]
    word_sets['spaces'] = [re.sub(r'\w', ' ', x) for x in word_sets['default']]
    word_sets['random'] = random_case_word_list()
    word_sets['mixed'] = mixed_letters_word_list()

    word_sets['rcapital'] = []
    for i in range(0, len(word_sets['upper'])):
        word = word_sets['upper'][i][0].lower() + word_sets['upper'][i][1:]
        word_sets['rcapital'].append(word)

    word_sets['upper_padded_l_5'] = [x.ljust(5) for x in word_sets['upper']]
    word_sets['lower_padded_l_5'] = [x.ljust(5) for x in word_sets['lower']]
    word_sets['upper_padded_l_9'] = [x.ljust(9) for x in word_sets['upper']]
    word_sets['lower_padded_l_9'] = [x.ljust(9) for x in word_sets['lower']]
    word_sets['upper_padded_l_25'] = [x.ljust(25) for x in word_sets['upper']]
    word_sets['lower_padded_l_25'] = [x.ljust(25) for x in word_sets['lower']]
    word_sets['upper_padded_r_5'] = [x.rjust(5) for x in word_sets['upper']]
    word_sets['lower_padded_r_5'] = [x.rjust(5) for x in word_sets['lower']]
    word_sets['upper_padded_r_9'] = [x.rjust(9) for x in word_sets['upper']]
    word_sets['lower_padded_r_9'] = [x.rjust(9) for x in word_sets['lower']]
    word_sets['upper_padded_r_25'] = [x.rjust(25) for x in word_sets['upper']]
    word_sets['lower_padded_r_25'] = [x.rjust(25) for x in word_sets['lower']]


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

    for file_number in range(0,len(word_sets['default'])):
    # for file_number in range(0,2):
        output_path = f'output/{base_filename}-{file_number}.txt'
        output_data = get_output(file_number)
        with open(output_path, 'w') as _file:
            _file.write(output_data)
        print(output_data)

