#!/usr/bin/env python3

import sys
import time
from curses import wrapper

def parse_input_coords():
    line_list = list()
    min_x = min_y = sys.maxsize
    max_x = max_y = 0
    for line in sys.stdin:
        rock_line = list()
        split_line = line.split(" -> ")
        for coord_str in split_line:
            coord = coord_str.split(',')
            coord[0] = int(coord[0])
            coord[1] = int(coord[1])
            min_x = coord[0] if coord[0] < min_x else min_x
            max_x = coord[0] if coord[0] > max_x else max_x
            min_y = coord[1] if coord[1] < min_y else min_y
            max_y = coord[1] if coord[1] > max_y else max_y
            rock_line.append((int(coord[0]), int(coord[1])))
        line_list.append(rock_line)
    cave_bounds = ((min_x, 0), (max_x, max_y))
    global X_OFFSET
    X_OFFSET = cave_bounds[0][0]
    return line_list, cave_bounds

def print_cave(cave):
    output_string = ''
    x_range = []
    for i in range(X_OFFSET, len(cave[0])+X_OFFSET):
        x_range.append(str(i))
    for i in range(0, 3*len(cave[0]) + 2): output_string += '='
    output_string += '\n'
    x_label = list(zip(*x_range[::-1]))
    for line in x_label:
        output_string += '   '
        for i in reversed(line):
            output_string += i + '  '
        output_string += '\n'

    current_row = 0
    for i in range(0, 3*len(cave[0]) + 2): output_string += '-'
    output_string += '\n'

    output_string += '  '
    for i in range(0, len(cave[0])):
        output_string += "{:02d} ".format(i)
    output_string += '\n'
    for col in cave:
        output_string += "{:02d} ".format(current_row)
        current_row+=1
        for i in col:
            output_string += i + '  '
        output_string += '\n'
    for i in range(0, 3*len(cave[0]) + 2): output_string += '='
    output_string += '\n'

    return output_string

def draw_cave(stdscr, output_string, ending_sand=None):
    stdscr.erase()
    stdscr.addstr(0, 0, output_string)
    stdscr.refresh()
    time.sleep(0.025)


def initialize_rock(cave, start, end):
    cave[start[1]][start[0]] = '#'
    if end:
        if start[0] == end[0]:
            step = 1 if end[1] >= start[1] else -1
            for i in range(start[1], end[1], step):
                cave[i][start[0]] = '#'
        elif start[1] == end[1]:
            step = 1 if end[0] >= start[0] else -1
            for i in range(start[0], end[0], step):
                cave[start[1]][i] = '#'
    return cave

def initialize_cave(rock_lines, cave_bounds):
    cave = []
    x_range = range(cave_bounds[0][0], cave_bounds[1][0]+1)
    y_range = range(cave_bounds[0][1], cave_bounds[1][1]+1)
    for y in y_range:
        col = []
        for x in x_range:
            col.append('.')
        cave.append(col)
    for line in rock_lines:
        for index, coord in enumerate(line):
            x = coord[0] - X_OFFSET
            y = coord[1]
            if index+1 >= len(line):
                next_coord = None
            else:
                next_x = line[index+1][0] - X_OFFSET
                next_y = line[index+1][1]
                next_coord = (next_x, next_y)

            initialize_rock(cave, (x, y), next_coord)
            cave[0][500-X_OFFSET] = '+'
    return cave

def drop_sand(cave, x, y):
    cave[y][x] = 'o'
    wrapper(draw_cave, print_cave(cave))
    cave[y][x] = '.'
    if cave[y+1][x] == '.':
        drop_sand(cave, x, y+1)
    elif cave[y+1][x-1] == '.':
        drop_sand(cave, x-1, y+1)
    elif cave[y+1][x+1] == '.':
        drop_sand(cave, x+1, y+1)
    else:
        cave[y][x] = 'o'
    print_cave(cave)
    return cave

def add_sand(cave):
    try:
        cave = drop_sand(cave, 500-X_OFFSET, 0)
    except IndexError:
        raise
    # print_cave(cave)
    return

def main():
    rock_lines, cave_bounds = parse_input_coords()
    cave = initialize_cave(rock_lines, cave_bounds)
    full = False
    sand_count = 0
    while not full:
        try:
            add_sand(cave)
        except IndexError:
            full = True
            break
        sand_count += 1
    wrapper(draw_cave, print_cave(cave), sand_count)
    print(print_cave(cave))
    print("Grains of Sand:", sand_count)
    return 0

if __name__ == "__main__":
    main()