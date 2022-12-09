def part1(puzzle_input):
    print('Q: Determine whether this peculiar patch of tall trees would be a good location for a tree house.')
    print('   How many trees are visible from outside the grid [when looking directly along a row or column]?')

    trees_visible = get_coords_of_visible_trees(puzzle_input)

    ans = len(trees_visible)

    print(f'A: {ans}')


def get_coords_of_visible_trees(tree_grid):
    """Return set of tuples of coords of trees that are visible."""
    trees_visible = set()

    for i in range(len(tree_grid)):
        row = tree_grid[i]
        for j in range(len(row)):
            if tree_is_visible(tree_grid, i, j):
                trees_visible.add((i, j))

    return trees_visible


def tree_is_visible(tree_grid, i, j):
    """Return true if all trees in one direction are shorter than the tree at i, j."""
    tree_height = tree_grid[i][j]

    trees_left = tree_grid[i][:j]
    if not trees_left or max(trees_left) < tree_height:
        return True

    trees_right = tree_grid[i][j+1:]
    if not trees_right or max(trees_right) < tree_height:
        return True

    trees_up   = []
    trees_down = []
    for row_idx in range(len(tree_grid)):
        row = tree_grid[row_idx]
        if row_idx < i:
            trees_up.append(row[j])
        elif row_idx > i:
            trees_down.append(row[j])

    if not trees_up or max(trees_up) < tree_height:
        return True
    elif not trees_down or max(trees_down) < tree_height:
        return True
    else:
        return False


def part2(puzzle_input):
    print('Q:')



    print(f'A: {ans}')