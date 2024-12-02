#!/usr/bin/env python

import time
import numpy as np

__author__ = "Sal Greco"
__credits__ = ["Eric Wastl", "Sal Greco"]
__license__ = "MIT"
__email__ = "slgreco@buffalo.edu"

scratchcards = open('day_4/input.in').readlines()

def get_winning_nums(card_data):
    # Split the card in the the
    # game id string and the card nums
    s_game_id, card = card_data.split(': ')
    # Split the card nums into the game nums
    # and the winning nums
    game_nums, winning_nums = card.split(' | ')
    # Using set comprehension, convert the ' ' delimeted
    # list from a string to sets of int
    game_nums = set(int(i) for i in  game_nums.split(' ') if i)
    winning_nums = set(int(i) for i in  winning_nums.split(' ') if i)

    return int(s_game_id.split()[1]), list(game_nums & winning_nums)

def main():
    score = 0
    cards = np.ones(len(scratchcards))
    for card_data in scratchcards:
        # Init card score
        card_score = 0
        # get the game id string and winning numbers
        game_id, winning_nums = get_winning_nums(card_data)
        # Calculate the card score
        card_score = len(winning_nums) * 2
        
        #print(game_id, '|',game_num,'|' ,winning_nums[:-1],'|' , card_score)
        # Update the total score
        score += card_score
        
        # Calculate the number of cards processed
        cards[game_id:game_id+len(winning_nums)] += np.ones(len(winning_nums))*cards[game_id-1]
        
    return score, np.sum(cards)


if __name__ == '__main__':

    st = time.monotonic()

    ans = main()

    et = time.monotonic()

    print(ans, et-st)
