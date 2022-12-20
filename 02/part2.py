#!/usr/bin/env python3.10

import sys

"""
A = Rock     = X = 1 
B = Paper    = Y = 2
C = Scissors = Z = 3 
"""

def parse_input():
    input = []
    for line in sys.stdin:
            input.append(line.strip())
    return input

def calculate_score(player1, player2):
    outcome = 0
    match player2:
        case 'X': # to lose
            outcome += 0
            match player1:
                case 'A': # Rock 
                    outcome += 3 # Scissors
                case 'B': # Paper
                    outcome += 1 # Rock
                case 'C': # Scissors
                    outcome += 2
        case 'Y': # to draw
            outcome += 3
            match player1:
                case 'A': # Rock
                    outcome += 1
                case 'B': # Paper
                    outcome += 2
                case 'C': # Scissors
                    outcome += 3
        case 'Z': # to win
            outcome += 6
            match player1:
                case 'A': # Rock
                    outcome += 2
                case 'B': # Paper
                    outcome += 3
                case 'C': # Scissors
                    outcome += 1
    return outcome

def main():
    strategy = parse_input()
    total_score = 0
    for match in strategy:
        score = calculate_score(match.split(' ')[0], match.split(' ')[1])
        print(match, score)
        total_score += score

    print(f"Total Score is {total_score}")
    return 0

if __name__ == "__main__":
    main()