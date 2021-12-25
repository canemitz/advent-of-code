import networkx as nx


def part1(input_data):
    print('Q: How many paths through this cave system are there that visit small caves at most once?')
    cave_graph = get_cave_graph(input_data)

    unique_paths = []
    for path in nx.all_simple_paths(cave_graph, source='start', target='end'):
        new_path = []

        # Remove the suffix from large cave nodes to avoid duplicate paths
        for node in path:
            node_basename = node.split('_')[0]
            new_path.append(node_basename)
        if new_path not in unique_paths:
            unique_paths.append(new_path)

    ans = len(unique_paths)
    print(f'A: {ans}')


def get_cave_graph(input_data):
    cave_graph = nx.Graph()

    # Duplicate large caves so that simple paths can go through the "same" node
    # ...increment and rerun until number of paths doesn't increase
    num_duplicate_large_caves = 4

    edges = []
    for line in input_data.readlines():
        [a, b] = line.strip().split('-')
        a_arr = [a]
        b_arr = [b]

        if a.isupper():
            a_arr += [f'{a}_{x}' for x in range(num_duplicate_large_caves)]
        if b.isupper():
            b_arr += [f'{b}_{x}' for x in range(num_duplicate_large_caves)]

        for x in a_arr:
            for y in b_arr:
                edge = (x, y)
                edges.append(edge)
                cave_graph.add_nodes_from(edge)

    cave_graph.add_edges_from(edges)

    return cave_graph


def part2(input_data):
    print('Q:')
    print(f'A: {ans}')