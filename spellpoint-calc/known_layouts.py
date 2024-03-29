# A dictionary of dictionaries.
# Each sub dicts holds the class' spell slots on the format
# cl: [1st lvl slots, 2nd lvl slots, ..., 9th lvl slots]
# if the class specifies 0 slots, 0 should be specified
# - slots SHOULD be omitted

types = {
    'wiz': {
         1: [1],
         2: [2],
         3: [2, 1],
         4: [3, 2],
         5: [3, 2, 1],
         6: [3, 3, 2],
         7: [4, 3, 2, 1],
         8: [4, 3, 3, 2],
         9: [4, 4, 3, 2, 1],
        10: [4, 4, 3, 3, 2],
        11: [4, 4, 4, 3, 2, 1],
        12: [4, 4, 4, 3, 3, 2],
        13: [4, 4, 4, 4, 3, 2, 1],
        14: [4, 4, 4, 4, 3, 3, 2],
        15: [4, 4, 4, 4, 4, 3, 2, 1],
        16: [4, 4, 4, 4, 4, 3, 3, 2],
        17: [4, 4, 4, 4, 4, 4, 3, 2, 1],
        18: [4, 4, 4, 4, 4, 4, 3, 3, 2],
        19: [4, 4, 4, 4, 4, 4, 4, 3, 3],
        20: [4, 4, 4, 4, 4, 4, 4, 4, 4]
    }  
}