#!/usr/bin/env python3.10

import sys

"""
A = Rock     = X
B = Paper    = Y
C = Scissors = Z
"""

def parse_input():
    input = []
    for line in sys.stdin:
            input.append(line.strip())
    return input

def calculate_score(player1, player2):
    outcome = 0
    match player2:
        case 'X': # Rock
            outcome += 1
            match player1:
                case 'A': # Rock
                    outcome += 3 # Draw
                case 'B': # Paper
                    outcome += 0 # Loss
                case 'C': # Scissors
                    outcome += 6
        case 'Y': # Paper
            outcome += 2
            match player1:
                case 'A': # Rock
                    outcome += 6
                case 'B': # Paper
                    outcome += 3
                case 'C': # Scissors
                    outcome += 0
        case 'Z': # Scissors
            outcome += 3
            match player1:
                case 'A': # Rock
                    outcome += 0
                case 'B': # Paper
                    outcome += 6
                case 'C': # Scissors
                    outcome += 3
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