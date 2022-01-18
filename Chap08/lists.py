#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    game = [ 'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock' ]
    print_list(game)
    game.append('Lizard')

    print(type(set(game)))
    print(game)
    print(set(game))
    game.extend([8, 'Geeks', 'Always'])
    print(game)
    dataScientist = set(['Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS'])
    print(set(['Linux', 'R', 'SQL Server', 'Git', 'Tableau', 'SAS']))
    print (dataScientist)


    print(set(['Linux', 'R', 'SQL Server', 'Git', 'Tableau', 'SAS']))

def print_list(o):
    for i in o: print(i, end='  ', flush=True)
    print()

if __name__ == '__main__': main()
