#!/usr/bin/env python

"""day_three.py: Solution to Advent of Code 2023 Day3: Gear Ratios."""

import time

__author__ = "Sal Greco"
__credits__ = ["Eric Wastl", "Sal Greco"]
__license__ = "MIT"
__email__ = "slgreco@buffalo.edu"

symbols = '-@*=%/$#+&'
# Load schematic, using list comprehension convert each line to a list of str.
schematic =[list(l) for l in open("day_3/input.in").readlines()]

sum = 0

def get_window_item(rel_l, rel_s) -> bool:
    try:
        # If there is an int relative the the symbol
        # at (l,s) then return True
        int(schematic[rel_l][rel_s])
        return True
    except ValueError as e:
        # If the character relative to (l,s) is not an int-like
        return False

def account_for_part_at_pos(l, s) -> int:
    l_bound = 0
    r_bound = 1
    num = ''
    
    while l_bound >= 0:
        # Try to read the character to the left of (l,s)
        try:
            # If there is a character, it should not be '.'
            if schematic[l][s-l_bound] not in '.\n' and\
               schematic[l][s-l_bound] not in symbols:
                # Left append digits we find
                num = schematic[l][s-l_bound] + num
                # Move the left side boundary
                l_bound += 1
            else:
                # adjust l_bound to be relative to center
                l_bound -= 1
                # Loop exit condition
                break
            
        except Exception as e:
            # adjust l_bound to be relative to center
            l_bound -= 1
            # Loop exit condition
            break

    while r_bound >= 0:
        try:
            if schematic[l][s+r_bound] not in '.\n' and\
               schematic[l][s+r_bound] not in symbols:
                # Right append digits we find
                num = num + schematic[l][s+r_bound]
                # Move the right boundary relative to center
                r_bound += 1
            else:
                # Loop exit condition
                break
            
        except Exception as e:
            # Loop exit condition
            break
    # get the left side of the data
    left = schematic[l][:s-l_bound]
    # get the right side of the data
    right = schematic[l][s+r_bound:]
    # rejoin left + n-dots + right
    # this removes the num so its not double counted 
    schematic[l] = left + ['.']*len(num) + right
    if not num:
        # if num is blank, set it to zero, so we return int-like str
        num = '0'
    return num


def find_in_window(l, s) -> int:
    # initialize empty sum for this window
    sum_in_window = 0
    # check if there are integers in the window
    window = [
                [get_window_item(l-1,s-1), get_window_item(l-1,s), get_window_item(l-1,s+1)],
                [get_window_item(l,s-1),                     False, get_window_item(l,s+1)],
                [get_window_item(l+1,s-1), get_window_item(l+1,s), get_window_item(l+1,s+1)]
            ]
    # get eash line from the window with its relative index,
    for rel_l,line in enumerate(window,-1):
        # get each symbol with its relative index
        for rel_s,item in enumerate(line,-1):
            # check if item in window is True (int in this position)
            if item:
                # grab the entire integer and add it to the sum.
                sum_in_window += int(account_for_part_at_pos(l+rel_l, s+rel_s))
    # return the sum of values within the window
    return sum_in_window


st = time.monotonic()

for l,line in enumerate(schematic,0):
    for s,symb in enumerate(line):
        if symb in symbols:

            ans = int(find_in_window(l,s))

            # print(ans)

            sum += ans 

et = time.monotonic()

print(sum,et-st)
