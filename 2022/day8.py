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
    print('Q: Consider each tree on your map. What is the highest scenic score possible for any tree?')

    tree_grid = puzzle_input

    max_y = (len(tree_grid)    - 1) / 2
    max_x = (len(tree_grid[0]) - 1) / 2
    scenic_score_theoretical_max = int(max_y**2 * max_x**2)

    ans = 1
    for i in range(len(tree_grid)):
        row = tree_grid[i]
        for j in range(len(row)):
            ans = max(ans, get_scenic_score(tree_grid, i, j))

        if ans == scenic_score_theoretical_max:
            break

    print(f'A: {ans}')


def get_scenic_score(tree_grid, i, j):
    """Return scenic score for tree at (i,j), which is the produce of the viewing distances in each direction.

    Note: the viewing distance is the distance at which a tree equals or exceeds the tree at (i,j);
          this means that there could be trees in some direction that block ones farther out, but don't block your view,
          so you might not be able to see all the trees in your viewing distance.""
    """
    tree_height = tree_grid[i][j]

    viewing_distance = {
        'left' : 0,
        'right': 0,
        'up'   : 0,
        'down' : 0
    }

    trees_left  = tree_grid[i][:j]
    trees_right = tree_grid[i][j+1:]
    if not trees_left or not trees_right:
        return 0

    for tree in trees_left[::-1]:
        viewing_distance['left'] += 1
        if tree >= tree_height:
            break

    for tree in trees_right:
        viewing_distance['right'] += 1
        if tree >= tree_height:
            break

    trees_up   = []
    trees_down = []
    for row_idx in range(len(tree_grid)):
        row = tree_grid[row_idx]
        if row_idx < i:
            trees_up.append(row[j])
        elif row_idx > i:
            trees_down.append(row[j])

    if not trees_up or not trees_down:
        return 0

    for tree in trees_up[::-1]:
        viewing_distance['up'] += 1
        if tree >= tree_height:
            break

    for tree in trees_down:
        viewing_distance['down'] += 1
        if tree >= tree_height:
            break

    scenic_score = 1
    for direction in viewing_distance:
        scenic_score *= viewing_distance[direction]

    return scenic_score