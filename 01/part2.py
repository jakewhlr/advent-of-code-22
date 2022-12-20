#!/usr/bin/env python3

import sys

def parse_input():
    input = []
    current_list = []
    for line in sys.stdin:
        if line != '\n':
            current_list.append(int(line.strip()))
        else:
            input.append(current_list)
            current_list = []
    input.append(current_list)
    return input

def determine_top_three(elf_list):
    first = 0
    second = 0
    third = 0

    for elf in elf_list:
        total = 0
        for meal in elf:
            total += meal
        if total >= first:
            third = second
            second = first
            first = total
        elif total >= second:
            third = second
            second = total
        elif total >= third:
            third = total
            
    return first, second, third

def main():
    first, second, third = determine_top_three(parse_input())
    print(f"The top 3 elves are carrying {first+second+third} calories.")
    return 0

if __name__ == "__main__":
    main()