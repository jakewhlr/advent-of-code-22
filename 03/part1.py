#!/usr/bin/env python3

import sys


def parse_input():
    input = []
    for line in sys.stdin:
            input.append(line.strip())
    return input

def halve_rucksack(rucksack):
    length = len(rucksack)
    if length % 2 != 0:
        raise ValueError("Rucksack contains odd number")
    else:
        comp_a = rucksack[0:int(length/2)]
        comp_b = rucksack[int(length/2):length]
    return comp_a, comp_b

def find_priority(item):
    if item.islower():
        return ord(item) - 96
    elif item.isupper():
        return ord(item) - 38

def find_shared(rucksack):
    print(f"{rucksack}, {halve_rucksack(rucksack)}")
    comp_a, comp_b = halve_rucksack(rucksack)
    for item in comp_a:
        if comp_b.find(item) >= 0:
            print(comp_b.find(item))
            print(f"{item}: {find_priority(item)}")
            priority = find_priority(item)
            return priority

def main():
    input = parse_input()
    total_priority = 0
    for line in input:
        total_priority += find_shared(line)
    print(f"Total Priority: {total_priority}")
    return 0

if __name__ == "__main__":
    main()