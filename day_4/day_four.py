#!/usr/bin/env python

import time
import numpy as np

__author__ = "Sal Greco"
__credits__ = ["Eric Wastl", "Sal Greco"]
__license__ = "MIT"
__email__ = "slgreco@buffalo.edu"

scratchcards = open('day_4/input.in').readlines()

def main():
    score = 0
    for i, card_data in enumerate(scratchcards,1):
        card_score = 0
        game_id, card = card_data.split(': ')
        game_nums, winning_nums = card.split(' | ')
        game_nums = [int(i) for i in  game_nums.split(' ') if i]
        winning_nums = [int(i) for i in  winning_nums.split(' ') if i]

        for game_num in game_nums:
            if game_num == '':
                continue
            if game_num in winning_nums:
                if card_score == 0:
                    card_score += 1
                else:
                    card_score *= 2

                #print(game_id, '|',game_num,'|' ,winning_nums[:-1],'|' , card_score)
        score += card_score
    return score


if __name__ == '__main__':

    ans = main()
    print(ans)