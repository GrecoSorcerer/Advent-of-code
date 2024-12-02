#!/usr/bin/env python

"""day_three.py: Solution to Advent of Code 2023 - Day 3: Gear Ratios."""

import time
import numpy as np

__author__ = "Sal Greco"
__credits__ = ["Eric Wastl", "Sal Greco"]
__license__ = "MIT"
__email__ = "slgreco@buffalo.edu"

symbols = '-@*=%/$#+&'
# Load schematic, using list comprehension convert each line to a list of str.
schematic =[list(l) for l in open("day_3/input.in").readlines()]

sum = 0
gear_ratio = 0

def get_window_item(rel_l, rel_s) -> bool:
    # If the position being checked on the
    # schematic is out of bounds, return False.
    if rel_s < 0\
    or rel_s >= len(schematic[0]):
        return False
    if rel_l < 0\
    or rel_l >= len(schematic):
        return False
    
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
    # initialize empty lit of gears
    gears = []
    # Grab the current symbol
    sym = schematic[l][s]
    # initialize empty sum for this window
    sum_in_window = 0
    # check if there are integers in the window
    window = [
                [get_window_item(l-1,s-1), get_window_item(l-1,s), get_window_item(l-1,s+1)],
                [get_window_item(l,s-1),                     False, get_window_item(l,s+1)],
                [get_window_item(l+1,s-1), get_window_item(l+1,s), get_window_item(l+1,s+1)]
            ]
    
    # Determine if parts in window count as a gear
    window_count = 0
    for line in window:
        # Count the part entries on a line.
        lc = line.count(True)
        # If there are no parts, skip this line.
        if lc == 0:
            continue
        # If the part fills a line of a window, it is one part.
        elif lc == 1\
          or lc == 3:
            window_count += 1
        # If there are 2 parts entries on a line,
        # and they are next to each other, its 1 part.
        elif lc == 2\
        and  line[0] != line[2]:
            window_count += 1
        # If there is a gap between the parts there are two parts.
        else:
            window_count +=2

        

    # get eash line from the window with its relative index,
    for rel_l,line in enumerate(window,-1):
        # get each symbol with its relative index
        for rel_s,item in enumerate(line,-1):
            # check if item in window is True (int in this position)
            if item:
                # Get the symbol relative to the current symbol
                rel_sym = schematic[l+rel_l][s+rel_s]
                # Get the part number AND clear it from the line as dots.
                part_number = int(account_for_part_at_pos(l+rel_l, s+rel_s))
                # If the current symbol denotes a possible gear,
                # and there are only two parts,
                # where there is a distict part.
                # Unless we already have two gears.
                if sym == '*' and rel_sym != '.' and\
                   window_count == 2 and\
                   len(gears)<2:
                    # Add the part to the list of gears
                    gears += [part_number]
                    # print(gears)
                # grab the entire integer and add it to the sum.
                sum_in_window += part_number
    # If there are gears, take their product.
    # Otherwise return 0
    if gears:
        gear_ratio_in_window = np.prod(gears)
    else:
        gear_ratio_in_window = 0

    return sum_in_window, gear_ratio_in_window


st = time.monotonic()

for l,line in enumerate(schematic,0):
    for s,symb in enumerate(line):
        if symb in symbols:

            sum_ans,gear_ratio_ans = find_in_window(l,s)

            # print(ans)

            sum += sum_ans
            gear_ratio += gear_ratio_ans

et = time.monotonic()

print(sum,gear_ratio,et-st)
