import numpy as np
calib_values = open('day_1\input.txt').readlines()

az_mul = np.array([
    [10],
    [1]
])
digits_as_str = ['zero', 'one',  'two',
                'three','four', 'five',
                'six',  'seven','eight',
                        'nine']
sum = 0
l = 0


while len(calib_values)>=1:
    l+=1
    # If fisrt = True then searching for the first digit, 
    #          = False then searching for the second digit
    first = True
    # Digits as a 2-D vector
    az_digits = np.array([-1, -1])
    # Pop the next line
    line = calib_values.pop()
    # Print the line
    print(line[:-1])
    
    # place holder for trying to find digits as a composite of str
    digit_from_ch = ''
    

    # Get each character
    for ch in line:
        # Initialize digit as -1
        digit = -1
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
                    # If digit_from_ch contains a digit as a str
                    if num in digit_from_ch:
                        # set the value of digit
                        digit = i
                        # clear the digit_from_ch palceholder
                        digit_from_ch = ''
                        # record digit
                        break
                # If digit is invalid,
                if digit == -1:
                    continue

        ## If we're here, then the character was an int.
        # If this is the first digit,

        # Check our work.
        print(f'got {digit}, first: {first}')

        # If the first digit
        if first:
            # Record the first digit,
            az_digits[0] = digit
            # No longer looking for the first digit.
            first = False
        # If not the first digit 
        else: 
            # Record the second digit
            az_digits[1] = digit


    # If there was only one digit in the line,
    if az_digits[1] == -1:
        # The second digit is the same as the first.
        az_digits[1] = az_digits[0]

    # Matrix multiply to get the sum
    sum += az_digits@az_mul

    # Print the Sum
    print(az_digits, az_mul.T, az_digits@az_mul)


print(sum)