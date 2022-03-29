import math

import parser
import known_layouts as layouts


def main():
    args = parser.parse_cli()

    if args.subcommand == 'total':
        slots = set_up(args.level, args.caster, args.slots, args.custom_slot)
        bonus = calc_bonus(args.spell_level, args.modifier)
        print(f'Total Spell points: {slots + bonus}\nFrom slots: {slots}, from bonus: {bonus}')

    elif args.subcommand == 'slots':
        slots = set_up(args.level, args.caster, args.slots, args.custom_slot)
        print(f'Spell points from slots: {slots}')

    elif args.subcommand == 'stat':
        bonus = calc_bonus(args.spell_level, args.modifier)
        print(f'Bonus spell points: {bonus}')

    else:
        print('Unknown parser. You probably forgot the arguments')


def set_up(lvl, caster, slot_class, file):
    if slot_class is None:
        slot_dict = read_to_dict(file)

    else:
        slot_dict = layouts.types[slot_class]

    if caster.__contains__('full'):
        if lvl > 9:
            slot_arr = slot_dict[9]
        else:
            slot_arr = slot_dict[lvl]
    else:
        slot_arr = slot_dict[lvl]

    return handlers[caster](lvl, slot_arr)


def read_to_dict(file):
    slot_dict = {}
    with open(file) as file:
        for line in file:
            elements = list(map(lambda x: int(x), line.strip().split(' ')))
            slot_dict[elements[0]] = elements[1:]

    return slot_dict


def calc_bonus(max_slot_lvl, stat):
    if stat < 1:
        return 0

    total = 0

    # manually calculate bonus slots for high stat modifiers.
    for i in range(1, max_slot_lvl + 1):
        # first bonus comes at stat = 12, so we compensate
        adj_stat = stat - (i - 1)
        total += math.ceil(adj_stat / 4) * (2 * i - 1)

    return total


# Class gets up to 4th lvl spells, like paladin and ranger
def calc_minor(lvl, slot_arr):
    total = 0
    for i, slots in enumerate(slot_arr, 1):
        total += slots * ( 2 * i - 1)

    return total


# Class gets up to 6th lvl spells,
def calc_medium(lvl, slot_arr):
    total = 0
    for i, slots in enumerate(slot_arr, 1):
        if i > 1:
            if slots == 0:
                slots = 1
        total += slots * ( 2 * i - 1 )

    return total


# class gets up to 9th lvl spells
def calc_full(lvl, slot_arr):
    total = 0
    for i, slots in enumerate(slot_arr, 1):
        if i == 1:
            total += slots * 2

        else:
            total += min(slots * (2 * i - 1), 16)

        if i % 2 == 0:
            if slots > 1:
                total -= 1 

    total += max((lvl - 9) * 16, 0)

    return total


# class is a sorcerer, or gets equivalent spell
def calc_sorc(lvl, slot_arr):
    total = calc_full(lvl, slot_arr)
    total += 2 * (round(lvl/2)) - 1

    return total


handlers = {
    'quarter': calc_minor,
    'half': calc_medium,
    'full': calc_full,
    'full_spont': calc_sorc 
}


if __name__ == '__main__':
    main()