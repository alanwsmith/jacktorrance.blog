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
def words_at_positions(*, positions, case='default', spaces='spaces'):
    line = []
    for i in range(0, len(word_sets['default'])):
        if i in positions:
            line.append(word_sets[case][i])
        else:
            if spaces:
                line.append(word_sets[spaces][i])
    return " ".join(line) 

def letters_removed(*, letters=[], case='default'):
    return_list = []
    for word in word_sets[case]:
        updated_word = word
        for letter in letters:
            updated_word = re.sub(letter, ' ', updated_word)
        return_list.append(updated_word)
    return " ".join(return_list)


# get just the specific letters at the original positions
def only_letters(*, letters=[], case='default'):
    return_list = []
    for word in word_sets[case]:
        updated_word = word
        for letter in letters:
            updated_word = re.sub(r'[^' + letter + ']' , ' ', updated_word)
        return_list.append(updated_word)
    return " ".join(return_list)

def letter_set(case='default'):
    letters = set()

    for word in word_sets[case]:
        for letter in word[:]:
            letters.add(letter)

    return list(letters)


def get_output(file_number):
    lines = []

    for i in range(0, 3):
        line = ""
        while len(line) < 51:
            line += word_sets['upper'][randint(0,9)]
            if len(line) > 51:
                line = ''
        lines.append(line)
    
    preface = ''
    while len(preface) < 8:
        preface += word_sets['upper'][randint(0,9)]
        if len(preface) > 8:
            preface = ''
    afterword = ''
    while len(afterword) < 8:
        afterword += word_sets['upper'][randint(0,9)]
        if len(afterword) > 8:
            afterword = ''

    lines.append(preface + ' ' + ''.join(word_sets['lower']) + ' ' + afterword)


    for i in range(0, 3):
        line = ""
        while len(line) < 51:
            line += word_sets['upper'][randint(0,9)]
            if len(line) > 51:
                line = ''
        lines.append(line)

    return "\n".join(lines)


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

    word_sets['spaces_padded_r_5'] = [x.ljust(5) for x in word_sets['spaces']]
    word_sets['mixed_padded_l_5'] = [x.ljust(5) for x in word_sets['mixed']]

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
    for file_number in range(0,7):
        output_path = f'output/{base_filename}-{file_number}.txt'
        output_data = get_output(file_number)
        with open(output_path, 'w') as _file:
            _file.write(output_data)
        print(output_data)

