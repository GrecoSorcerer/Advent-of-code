#!/usr/bin/env python

"""/2024/day_one.py: Solution to 
Advent of Code 2024 Day 1: Historian Histeria"""

from pprint import pprint
import numpy as np

__author__ = "Sal Greco"
__credits__ = ["Eric Wastl", "Sal Greco"]
__license__ = "MIT"
__email__ = "slgreco@buffalo.edu"

with open("./input.txt") as input_file:
    input_lines = input_file.readlines()


def process_input(lines):
    left_list = []
    right_list = []
    for line in lines:
        lsv, rsv = line.split("   ")
        left_list += [int(lsv)]
        right_list += [int(rsv)]
    return left_list, right_list

def post_process_input(left_list, right_list):
    
    # Sort the lists
    sorted_left_list = sorted(left_list)
    sorted_right_list = sorted(right_list)

    # Calculate the distances between the sorted left side values 
    # and sorted right side values.
    distances = np.subtract(sorted_left_list, sorted_right_list)
    # Take the absolute value of these distances
    abs_distance = np.abs(distances)
    # Then get the total distance
    total_distance = np.sum(abs_distance)
    
    return total_distance
    

left_list, right_list = process_input(input_lines)
pprint(post_process_input(left_list, right_list))