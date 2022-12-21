#!/usr/bin/env python3

import sys


def parse_input():
    input = []
    for line in sys.stdin:
        pair = []
        split = line.strip().split(',')
        for item in split:
            pair.append([int(i) for i in item.split('-')])
        input.append(pair)
    return input

def find_sublist(pair):
    start_a, end_a = pair[0]
    start_b, end_b = pair[1]
    if start_a >= start_b and end_a <= end_b:
        return True
    if start_b >= start_a and end_b <= end_a:
        return True
    return False


def main():
    input = parse_input()
    total_count = 0
    for line in input:
        if find_sublist(line): total_count += 1
    print(f"Total Count: {total_count}")
    return 0

if __name__ == "__main__":
    main()