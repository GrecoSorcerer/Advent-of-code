
# data = open('day_5/test_input.in').readlines()

import time

__author__ = "Sal Greco"
__credits__ = ["Eric Wastl", "Sal Greco"]
__license__ = "MIT"
__email__ = "slgreco@buffalo.edu"

with open('day_5/input.in', 'r') as data:

    conversion_data = data.readline()
    data.readline()

    # seeds as a list
    # [s1, s2, s3, ... , sn]
    seeds = conversion_data.strip().split(' ')[1:]
    
    # List of seeds as ints
    seed_ids = [int(seed_id) for seed_id in seeds]

    conversion_category = 'seeds'
    
    st = time.monotonic()

    # Dictionary to track the the 
    # conversion categories.
    # Theres even room for writing the 
    # conversion down in there.
    almanac = {}
    almanac[conversion_category] = seed_ids

    for conversion_data in data:

        if not conversion_data\
            or conversion_data == '\n':
            continue
        
        new_seed_ids = seed_ids.copy()
        # Try to map the ranges on this line
        try:
            # Will raise and exception if character
            # is not an int.
            int(conversion_data[0])

            dst, src, sz = conversion_data[:-1].split(' ')
            
            # Convert the range values to ints
            dest_start = int(dst)
            srce_start = int(src)
            range_size = int(sz)

            # get each range value
            # dest_range = range(dest_start,dest_start+range_size)
            srce_range = range(srce_start,srce_start+range_size)

            # Pre-calculate the difference between the destination
            # range start and the source range start.
            # This will be used to map into the destination range.
            diff = dest_start - srce_start
            
            for i, seed_id in enumerate(almanac[conversion_category]):
               
                if seed_id in srce_range:
                    # Map the source in to the destination.
                    new_seed_ids[i] += diff

                    # print(f"{i} {conversion_category} [{srce_start} ... {seed_id} ... {srce_start+range_size}] : {seed_ids} -> {new_seed_ids}")

            # add the pairs of range values to their converson category
            seed_ids = new_seed_ids

        except ValueError as e:
            # An exception was raised above, 
            # meaning this is a new category.

            # Get the category name
            new_conversion_category = conversion_data.strip(':\n')

            # Update the conversion_category
            conversion_category = new_conversion_category
            
            # store the seed_ids as the new source seed_ids in almanac
            almanac[conversion_category] = seed_ids
    et = time.monotonic()
    
    print(min(seed_ids),et - st)

