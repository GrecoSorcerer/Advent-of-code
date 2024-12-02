#!/usr/bin/env python

"""day_one.py: Solution to Advent of Code 2023 - Day 1: Trebuchet?!"""

import numpy as np
import time

__author__ = "Sal Greco"
__credits__ = ["Eric Wastl", "Sal Greco"]
__license__ = "MIT"
__email__ = "slgreco@buffalo.edu"

# Load the input data
calib_values = open('day_1/input.in').readlines()

# Vector used to combine vector of digits
az_mul = np.array([
    [10],
    [1]
])

# Digits as words
digits_as_str = ['zero', 'one',  'two',
                'three','four', 'five',
                'six',  'seven','eight',
                        'nine']

sum_s1 = 0
sum_s2 = 0

sum_with_words = 0


st = time.monotonic()

while len(calib_values)>=1:
    # If fisrt = True then searching for the first digit, 
    #          = False then searching for the second digit
    first_s1 = True
    first_s2 = True
    # Digits as a 2-D vector
    az_digits_s1 = np.array([-1, -1])
    az_digits_s2 = np.array([-1, -1])
    # Pop the next line
    line = calib_values.pop()
    # Print the line
    # print(line[:-1])
    
    # place holder for trying to find digits as a composite of str
    digit_from_ch = ''
    

    # Get each character
    for ch in line:
        # Initialize digit as -1
        digit = -1
        # Initialize digit from word as -1
        digit_from_word = -1
        # Check if the character is an int.
        try:
            # The character is an int.
            digit = int(ch)
            digit_from_ch = ''
            
        # The char wasn't an int, lets see if we can match
        # a group of char to a digit.
        except ValueError as e:
            # append this character to search for a
            # digit as a str.
            digit_from_ch += ch

            # If digit_from_ch is non-empty,
            if digit_from_ch:
                
                # for each digit as a str (num),
                # see if it matches 'digit' from chars
                for i,num in enumerate(digits_as_str):
                    if len(digit_from_ch) < 3:
                        break
                    # If digit_from_ch contains a digit as a str
                    if num in digit_from_ch:
                        # set the value of digit
                        digit_from_word = i
                        # clear the digit_from_ch palceholder
                        digit_from_ch = ''
                        # record digit
                        break
                # If digit is invalid,
                if digit_from_word == -1:
                    continue

        ## If we're here, then the character was an int.
        # If this is the first digit,

        # Check our work.
        # print(f'got {digit}, first: {first}')

        # If the first digit
        if first_s1 and digit != -1:
            # Record the first digit,
            az_digits_s1[0] = digit
            # No longer looking for the first digit.
            first_s1 = False
        if first_s2:
            # Record the first digit,
            if digit != -1:
                az_digits_s2[0] = digit
            if digit_from_word != -1:
                az_digits_s2[0] = digit_from_word
            
            # No longer looking for the first digit.
            first_s2 = False
        # If not the first digit 
        else: 
            # Record the second digit
            if digit != -1:
                az_digits_s1[1] = digit
                az_digits_s2[1] = digit
            if digit_from_word != -1:
                az_digits_s2[1] = digit_from_word


    # If there was only one digit in the line,
    if az_digits_s1[1] == -1:
        # The second digit is the same as the first.
        az_digits_s1[1] = az_digits_s1[0]
    
    # If there was only one digit in the line,
    if az_digits_s2[1] == -1:
        # The second digit is the same as the first.
        az_digits_s2[1] = az_digits_s2[0]

    # if az_digits_s2[0] == -1 and\
    #    az_digits_s2[1] == -1:
    #     az_digits_s2 = az_digits_s1
        

    # Matrix multiply to get the sum
    sum_s1 += az_digits_s1@az_mul
    sum_s2 += az_digits_s2@az_mul

    # Print the Sum
    #print(f'{az_digits_s1}, {az_mul.T}, {az_digits_s1@az_mul}, {line[:-1]}')
    #print(f'{az_digits_s2}, {az_mul.T}, {az_digits_s2@az_mul}, {line[:-1]}')

et = time.monotonic()

print(sum_s1[0], sum_s2[0], et-st)