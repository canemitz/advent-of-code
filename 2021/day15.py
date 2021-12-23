import math
import numpy as np
import datetime


def part1(input_data):
    print('Q: What is the lowest total risk of any path from the top left to the bottom right?')
    global map_arr

    get_map_arr(input_data)

    (n_rows, n_cols) = map_arr.shape
    origin = (0, 0)
    destination = (n_rows-1, n_cols-1)
    (distances_to_coords, prev_coords) = dijkstra(origin, destination)

    lowest_total_risk = distances_to_coords[destination]

    print(f'A: {lowest_total_risk}')


def get_map_arr(input_data):
    global map_arr
    global map_flattened

    map_arr = np.array(
        [ [int(x) for x in line.strip()] for line in input_data.readlines() ]
    )

    map_flattened = get_map_flattened(map_arr)


def get_map_flattened(map_arr):
    map_flattened = []
    for y, row in enumerate(map_arr):
        for x in range(len(row)):
            coord = (y, x)
            map_flattened.append(coord)

    return map_flattened


def dijkstra(origin, destination):
    # distances = {}
    global map_arr
    global map_flattened

    # distances from origin to vertex (key)
    dist = {}
    # points to previous-hop nodes on the shortest path from source to the given vertex
    prev = {}

    # Populate dist and prev
    for v in map_flattened:
        dist[v] = float('inf')
        prev[v] = None
    dist[origin] = 0
    dist = sort_dict(dist)

    # Q is a set that (initially) holds each vertex
    Q = set(map_flattened)

    # Skip sorting dist the first time (might save some time?)
    sort_dist = False
    # init vars to print progress
    max_Q = len(Q)
    max_Q_over_20 = int(max_Q / 20)

    # While there are vertices left in Q
    while Q:

        # Print progress every 5% fewer vertices in Q
        len_Q = len(Q)
        if not len_Q % max_Q_over_20:
            print(f'{datetime.datetime.now()}: Looping while Q, {100 - int(100 * len_Q / max_Q)}% done ({len_Q} vertices remaining)')

        u = get_vertex_in_Q_with_smallest_dist(Q, dist, sort_dist)
        sort_dist = True

        if u == destination:
            break

        Q.remove(u)

        neighbors_of_u = get_four_neighbor_coords(map_arr, u)
        for v in neighbors_of_u:
            if v in Q:
                # Check potential new path: dist[u] plus distance from u to v (current node to neighbor)
                alt_length = dist[u] + get_length(u, v)

                if alt_length < dist[v]:
                    dist[v] = alt_length
                    prev[v] = u

    return dist, prev


def get_vertex_in_Q_with_smallest_dist(Q, dist, sort_dist):
    dist_in_Q = {}

    # Get the dist dictionary for only the vertices in the set Q
    for v in dist:
        if v in Q:
            dist_in_Q[v] = dist[v]

    # Sort dist_in_Q by value
    dist_in_Q_sorted = sort_dict(dist_in_Q) if sort_dist else dist_in_Q

    u = None
    for v in dist_in_Q_sorted:
        u = v
        break

    return u


def sort_dict(dictionary):
    # Get an iterable of tuples, where tuple[0] is the key, and tuple[1] is the value
    list_of_tuples = dictionary.items()

    # Sort the list of tuples by the dictionary value
    sorted_tuples = sorted(list_of_tuples, key=lambda entry: entry[1])

    # Stuff the sorted list of tuples back into a dictionary
    sorted_dict = {key: val for key, val in sorted_tuples}

    return sorted_dict


def get_length(u, v):
    """Return distance (risk score) going from coord u to v."""
    global map_arr

    (y_max, x_max) = map_arr.shape
    (y_u, x_u) = u
    (y_v, x_v) = v

    length = float('inf')
    if ( (y_u > y_max) or (x_u > x_max) or (y_v > y_max) or (x_v > x_max) ):
        length = float(inf)
    else:
        if (y_u == y_v) and (abs(x_u - x_v) == 1):
            length = map_arr[(y_v, x_v)]
        elif (x_u == x_v) and (abs(y_u - y_v) == 1):
            length = map_arr[(y_v, x_v)]

    return length


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

