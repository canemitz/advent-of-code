import math
import numpy as np
import datetime
import networkx as nx

def part1(input_data):
    print('Q: What is the lowest total risk of any path from the top left to the bottom right?')

    map_arr       = get_map_arr(input_data)
    map_flattened = get_map_flattened(map_arr)
    map_graph     = get_map_graph(map_arr, map_flattened)

    (n_rows, n_cols) = map_arr.shape
    origin = (0, 0)
    destination = (n_rows-1, n_cols-1)

    lowest_total_risk = nx.shortest_path_length(map_graph, source=origin, target=destination, weight='risk_level')

    print(f'A: {lowest_total_risk}')


def get_map_arr(input_data):
    map_arr = np.array(
        [ [int(x) for x in line.strip()] for line in input_data.readlines() ]
    )

    return map_arr


def get_map_flattened(map_arr):
    map_flattened = []
    for y, row in enumerate(map_arr):
        for x in range(len(row)):
            coord = (y, x)
            map_flattened.append(coord)

    return map_flattened


def get_map_graph(map_arr, map_flattened):
    map_graph = nx.DiGraph()

    map_graph.add_nodes_from(map_flattened)

    edges = []
    for node in map_flattened:
        node_risk_level = map_arr[node]
        node_neighbors = get_four_neighbor_coords(map_arr, node)

        for neighbor in node_neighbors:
            neighbor_risk_level = map_arr[neighbor]
            edge = (node, neighbor, {'risk_level': neighbor_risk_level})
            edges.append(edge)

    map_graph.add_edges_from(edges)

    return map_graph


def get_four_neighbor_coords(arr, coord):
    """Return list of coords of non-diagonal neighbors that exist."""
    (y0, x0) = coord
    (y_max, x_max) = arr.shape

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


def part2(input_data):
    print('Q: Using the full map, what is the lowest total risk of any path from the top left to the bottom right?')

    global map_arr
    global map_arr_expanded

    get_map_arr(input_data)
    get_map_arr_expanded(10)

    (n_rows, n_cols) = map_arr.shape
    origin = (0, 0)
    destination = (n_rows-1, n_cols-1)
    (distances_to_coords, prev_coords) = dijkstra(origin, destination)

    lowest_total_risk = distances_to_coords[destination]

    print(f'A: {lowest_total_risk}')


def get_map_arr_expanded(size):
    global map_arr
    global map_arr_expanded
    global map_flattened

    map_tiles = [map_arr]

    # Get incremented mini maps needed
    for x in range(1, (2*size)-1):
        next_map_tile = get_incremented_map_arr(map_tiles[x-1])
        map_tiles.append(next_map_tile)

    # Make map_tiles repeat as needed for easy slicing
    map_tiles *= size*size

    # Get the columns of the expanded map
    expanded_map_cols = []
    i_0 = 0
    i_1 = size
    for x in range(size):
        col = np.concatenate(map_tiles[i_0:i_1])
        expanded_map_cols.append(col)
        i_0 += 1
        i_1 += 1

    # Create the expanded map from the columns
    map_arr_expanded = np.concatenate(expanded_map_cols, axis=1)

    # Assign to map_arr so I don't have to change the other functions that use that global
    map_arr = map_arr_expanded

    map_flattened = get_map_flattened(map_arr)


def get_incremented_map_arr(map_tile):
    # Add 1 to each element in the map_tile
    incremented_map_arr = map_tile + 1

    # Check for any values greater than 9, and set them to 1
    for coord in zip(*np.where(incremented_map_arr == 10)):
        incremented_map_arr[coord] = 1

    return incremented_map_arr


def part2(input_data):
    print('Q: Using the full map, what is the lowest total risk of any path from the top left to the bottom right?')
    print(f'A: {ans}')