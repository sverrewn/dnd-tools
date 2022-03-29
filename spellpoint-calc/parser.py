import argparse

def parse_cli():
    parser = argparse.ArgumentParser(prog='spell_point_calc.py')

    subparsers = parser.add_subparsers(dest='subcommand', help='Available sub commands')

    parser_slots = subparsers.add_parser('slots', help='Calculates spell points from slots')
    parser_stat = subparsers.add_parser('stat', help='Calculates bonus spell points from stats.')
    parser_tot = subparsers.add_parser('total', help='Calculates total spell points')


    parser_slots.add_argument('-l', '--level', action='store', required=True, type=int,
                            help='Character level'
                        )

    parser_slots.add_argument('-c', '--caster', action='store', required=True,
                        choices=['quarter', 'half', 'full', 'full_spont'],
                        help='Choose what kind of caster you are.\
                              quarter goes up to spell level 4, \
                              half goes up to spell level 6, \
                              full goes up to spell level 9, \
                              full_spont is a spontaenous caster with spells up to level 9.'
                    )

    group = parser_slots.add_mutually_exclusive_group(required=True)
    
    group.add_argument('-s', '--slots', action='store',
                       choices=['wiz', 'urpriest'],
                       help='Choose spell slot layout from known sources'
                    )

    group.add_argument('-cs', '--custom_slot', action='store',
                        help='The path to the file containing the desired custom slot layout.\
                              The file must contain the slot layout for a level 9 character \
                              if it is a full (spontaneous) caster above level 9.\
                              the format is \'char_lvl slot1 slot2 slot3\' and so on. An arbitrary \
                              amount of lines are supported.\
                              for a 5th lvl wizard this would be 5 3 2 1'
                    )


    parser_stat.add_argument('-sl', '--spell_level', action='store', required=True, type=int,
                            help='Highest level spell slot available'
                        )

    parser_stat.add_argument('-m', '--modifier', action='store', required=True, type=int,
                             help='Ability modifier of casting stat'
                        )


    parser_tot.add_argument('-l', '--level', action='store', required=True, type=int,
                            help='Character level'
                        )

    parser_tot.add_argument('-sl', '--spell_level', action='store', required=True, type=int,
                            help='Highest level spell slot available'
                        )

    parser_tot.add_argument('-m', '--modifier', action='store', required=True, type=int,
                             help='Ability modifier of casting stat'
                        )

    parser_tot.add_argument('-c', '--caster', action='store', required=True,
                        choices=['quarter', 'half', 'full', 'full_spont'],
                        help='Choose what kind of caster you are.\
                              quarter goes up to spell level 4, \
                              half goes up to spell level 6, \
                              full goes up to spell level 9, \
                              full_spont is a spontaenous caster with spells up to level 9.'
                    )

    group = parser_tot.add_mutually_exclusive_group(required=True)
    
    group.add_argument('-s',
                       '--slots',
                       action='store',
                       choices=['wiz', 'urpriest'],
                       help='Choose spell slot layout from known sources'
                    )

    group.add_argument('-cs', '--custom_slot', action='store',
                        help='The path to the file containing the desired custom slot layout.\
                              The file must contain the slot layout for a level 9 character \
                              if it is a full (spontaneous) caster above level 9.\
                              the format is \'char_lvl slot1 slot2 slot3\' and so on. An arbitrary \
                              amount of lines are supported.\
                              for a 5th lvl wizard this would be 5 3 2 1'
                    )

    return parser.parse_args()