#!/usr/bin/env python

"""day_two.py: Solution to Advent of Code 2023 - Day 2: Cube Conundrum"""

import time
import numpy as np

__author__ = "Sal Greco"
__credits__ = ["Eric Wastl", "Sal Greco"]
__license__ = "MIT"
__email__ = "slgreco@buffalo.edu"

# Load the input data
cube_games = open('day_2\input.in').readlines()

# The rule for part 1
cube_game_rule = {
    "red":12,
    "green":13,
    "blue":14
    }


def game_set_to_dict(rgb_set) -> dict:
    """Given a list with str entries with the patern
    "{i} {color}, ...", return a dict where color is the key
    and i is the value."""

    # remove commas, then split by spaces
    #   ["{i} {color}", "{i} {color}", ...] -> 
    #   [{i}, {color}, {i}, {color}, ...]
    rgb_set = rgb_set.replace(',','').split(' ')

    # using dict comprehension, convert rgb_set to a dict
    rgb_dict = {
        rgb_set[i+1] : rgb_set[i]\
                for i in range(0, len(rgb_set),2)
        }
    
    return rgb_dict

def check_rgb_dict(set, rules=cube_game_rule) -> bool:
    """A Set should only contain 12 red cubes,
    13 green cubes, and 14 blue cubes for part 1."""
    
    # Check each set,
    for color,n in set.items():
        # If one of the sets has more cubes than the rules allow:
        if int(n) > rules[color]:
            return 1
    # If none of the sets return False,
    return 0

def update_game_rule_mins(set, mins):
    """Update the min rule for part 2 when called"""
    for color,n in set.items():
        if int(n) > mins[color]:
            mins[color] = int(n)
    
    return mins


def get_power_level(set):
    """The power level of a set is 
    the min r* min g * min b"""

    return np.prod([i for i in set.values()])


def main() -> int:

    # Initialize sum
    sum = 0
    power_sum = 0
    while len(cube_games) >=1:
        
        # The rule for part 2
        cube_game_min = {
            "red":1,
            "green":1,
            "blue":1
            }
        # Pop a game from the list of cube games
        # [:-1] to clip off the \n character 
        game_line = cube_games.pop()[:-1]
        # split "Game n: " from the sets of games
        game_RGBCubes = game_line.split(": ")
        # split the sets of games
        game_rgb_sets = [game_RGBCubes[0], 
                         game_RGBCubes[1].split('; ')]
        # used to count the number of failed checks for part 1
        # if greater than 0, the game was impossible by the rule.
        failed_checks = 0
        # get each set of cubes from a game
        for rgb_set in game_rgb_sets[1]:
            # convert the set of cubes to a dict
            rgb_dict = game_set_to_dict(rgb_set)
            # count the number of failed checks
            failed_checks += check_rgb_dict(rgb_dict)
            # get the min values from all rgb_dict in this set
            update_game_rule_mins(rgb_dict, cube_game_min)

        if failed_checks == 0:  
            # Convert the digit from "Game n" to an int,
            game_id = int(game_rgb_sets[0].split(' ')[1])
            # then add it to the sum.
            sum += game_id

        # print(f"{game_RGBCubes[0]}: Possible: {failed_checks == 0}; Power Level: {get_power_level(set=cube_game_min)}")
        power_sum += get_power_level(set=cube_game_min)

    
    return sum,power_sum


if __name__ == '__main__':
    
    st = time.monotonic()
    
    ans = main()
    
    et = time.monotonic()
     
    print(ans, et - st)
    
    