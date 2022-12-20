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

def determine_max(elf_list):
    current_max = 0
    for index, elf in enumerate(elf_list):
        total = 0
        for meal in elf:
            total += meal
        if total > current_max:
            current_max = total
            elf_index = index
    return current_max, elf_index

def main():
    max_calories, elf_index = determine_max(parse_input())
    print(f"Elf #{elf_index+1} has the most calories at {max_calories}")
    return 0

if __name__ == "__main__":
    main()