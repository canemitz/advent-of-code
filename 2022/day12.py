import networkx as nx
import numpy as np

def part1(puzzle_input):
    print('Q: What is the fewest steps required to move from your current position to the location that should get the best signal?')
    global start
    global end

    origin = f'{start[0]}_{start[1]}'
    destination = f'{end[0]}_{end[1]}'

    map_graph = get_map_graph(puzzle_input)
    ans = nx.shortest_path_length(map_graph, source=origin, target=destination)

    print(f'A: {ans}')


def get_map_graph(puzzle_input):
    """Return directed graph with edges between nodes that can be moved between."""
    map_shape = (len(puzzle_input), len(puzzle_input[0]))

    map_graph = nx.DiGraph()
    edges = []
    for i in range(map_shape[0]):
        for j in range(map_shape[1]):
            coord = (i, j)
            node_name = f'{i}_{j}'
            node_val = puzzle_input[i][j]

            for neighbor_coord in get_four_neighbor_coords(map_shape, coord):
                k, l = neighbor_coord
                neighbor_val = puzzle_input[k][l]
                if node_val - neighbor_val >= -1:
                    neighbor_name = f'{k}_{l}'
                    edges.append((node_name, neighbor_name))

    map_graph.add_edges_from(edges)
    return map_graph


def get_four_neighbor_coords(arr_shape, coord):
    """Return list of coords of non-diagonal neighbors that exist."""
    (y0, x0) = coord
    (y_max, x_max) = arr_shape

    neighbor_coords = []

    for y in [y0-1, y0+1]:
        neighbor_coord = (y, x0)
        if (-1 < y < y_max):
            neighbor_coords.append(neighbor_coord)

    for x in [x0-1, x0+1]:
        neighbor_coord = (y0, x)
        if (-1 < x < x_max):
            neighbor_coords.append(neighbor_coord)

    return neighbor_coords


def part2(puzzle_input):
    print('Q:')



    print(f'A: {ans}')


def parse_input(input_file_obj):
    """Convert input from letters to numbers and return as list of lists. Store global start and end coords."""
    global start
    global end

    puzzle_input_letters = [ list(line) for line in input_file_obj.read().strip().split('\n') ]

    puzzle_input = []
    for i in range(len(puzzle_input_letters)):
        row = []
        for j in range(len(puzzle_input_letters[0])):
            letter = puzzle_input_letters[i][j]

            if letter.isupper():
                if letter == 'S':
                    start = (i, j)
                    letter = 'a'
                elif letter == 'E':
                    end = (i, j)
                    letter = 'z'

            row.append(ord(letter) - 96)
        puzzle_input.append(row)

    return puzzle_input