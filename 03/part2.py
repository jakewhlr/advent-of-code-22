#!/usr/bin/env python3

import sys


def parse_input():
    input = []
    for line in sys.stdin:
            input.append(line.strip())
    groups = [input[i:i+3] for i in range(0, len(input), 3)]
    return groups

def find_priority(item):
    if item.islower():
        return ord(item) - 96
    elif item.isupper():
        return ord(item) - 38

def find_shared(rucksack_group):
    sack_a = rucksack_group[0]
    sack_b = rucksack_group[1]
    sack_c = rucksack_group[2]
    for item in sack_a:
        if sack_b.find(item) >= 0:
            if sack_c.find(item) >= 0:
                priority = find_priority(item)
                return priority

def main():
    input = parse_input()
    total_priority = 0
    for group in input:
        total_priority += find_shared(group)
    print(f"Total Priority: {total_priority}")
    return 0

if __name__ == "__main__":
    main()