import time

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
            return False
    # If none of the sets return False,
    return True
    

def main() -> int:

    # Initialize sum
    sum = 0
    i = 0
    while len(cube_games) >=1:
        i+=1
        # Pop a game from the list of cube games
        # [:-1] to clip off the \n character 
        game_line = cube_games.pop()[:-1]
        # split "Game n: " from the sets of games
        game_RGBCubes = game_line.split(": ")
        # split the sets of games
        game_rgb_sets = [game_RGBCubes[0], 
                         game_RGBCubes[1].split('; ')]
        # Convert the digit from "Game n" to an int,
        game_id = int(game_rgb_sets[0].split(' ')[1])
        # then add it to the sum.
        sum += game_id
        
        # get each set of cubes from a game
        for rgb_set in game_rgb_sets[1]:
            # convert the set of cubes to a dict
            rgb_dict = game_set_to_dict(rgb_set)
            # check if the set breaks the rules
            if not check_rgb_dict(rgb_dict):
                # remove the game_id from the sum
                sum -= game_id
                # check the next
                break
    
    return sum


if __name__ == '__main__':
    
    st = time.monotonic_ns()
    
    ans = main()
    
    et = time.monotonic_ns()
     
    print(ans, et - st)
    
    