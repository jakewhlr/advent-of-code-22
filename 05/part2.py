#!/usr/bin/env python3

import sys
import re

def parse_input():
    procedure = []
    stacks = []
    for line in sys.stdin:
        line = line.strip('\n')
        if line.startswith(" 1"):
            continue
        if not line:
            continue
        if line.startswith("move"):
            procedure.append([int(i) for i in re.search("move (\d+) from (\d+) to (\d+)", line).groups()])
        else:
            current_row = []
            current_col = ""
            for index, char in enumerate(line):
                if((index + 1) % 4 == 0):
                    if current_col == "   ":
                        current_col = None
                    else:
                        current_col = current_col[1]
                    current_row.append(current_col)
                    current_col = ""
                    continue
                current_col += char
            if current_col.startswith('['):
                current_row.append(current_col[1])
            else:
                current_row.append(None)
            stacks.append(current_row)
 
    return stacks, procedure

def initialize_stacks(stacks_list):
    stacks = [[] for i in stacks_list[0]]
    stacks_list.reverse()
    for line in stacks_list:
        for i in range(0, len(line)):
            if line[i]:
                stacks[i].append(line[i])
    return stacks

def move_crates(stacks, qty, src, dest):
    crates = [stacks[src-1].pop() for j in range(0, qty)]
    crates.reverse()
    for crate in crates:
        stacks[dest-1].append(crate) 
    return stacks

def main():
    stacks_list, procedure = parse_input()
    stacks = initialize_stacks(stacks_list)
    for step in procedure:
        stacks = move_crates(stacks, step[0], step[1], step[2])
    output_str = ""
    for stack in stacks:
        output_str += stack.pop()
    print(f"The top of the stacks will be {output_str}")
    return 0

if __name__ == "__main__":
    main()