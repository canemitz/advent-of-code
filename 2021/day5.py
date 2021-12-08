import numpy as np


def part1(input_data):
    print('Q: Consider only horizontal and vertical lines. At how many points do at least two lines overlap?')

    line_segments = get_line_segments(input_data)
    line_segments_straight = get_straight_line_segments(line_segments)

    diagram = get_initial_diagram(line_segments_straight)
    diagram_marked = mark_straight_lines_on_diagram(diagram, line_segments_straight)

    ans = get_num_points_with_x_lines(diagram_marked, x_lines=2)

    print(f'A: \n{ans}')


def get_line_segments(input_data):
    """Return list of dictionaries of coordinates for each segment.
    Reorder direction so segments go from lesser to greater values.
    Example:
        input_data = '5,9 -> 0,9'
        line_segments = [{'x1': 0, 'y1': 9, 'x2': 5, 'y2': 9}]
    """
    line_segments_list = ''.join(input_data.readlines()).split('\n')
    line_segments_list = [x.split(' -> ') for x in line_segments_list]

    line_segments = []
    for segment in line_segments_list:
        (x_a, y_a) = segment[0].split(',')
        (x_b, y_b) = segment[1].split(',')
        segment_dict = {
            'x1': min(int(x_a), int(x_b)),
            'x2': max(int(x_a), int(x_b)),
            'y1': min(int(y_a), int(y_b)),
            'y2': max(int(y_a), int(y_b))
        }
        line_segments.append(segment_dict)

    return line_segments


def get_initial_diagram(line_segments):
    """Return numpy array of dots large enough for all the line segments."""
    x_max = 0
    y_max = 0

    for segment in line_segments:
        x_max = max(x_max, segment['x1'], segment['x2'])
        y_max = max(y_max, segment['y1'], segment['y2'])

    initial_diagram = np.zeros([x_max+1, y_max+1], dtype=int)
    return initial_diagram


def get_straight_line_segments(line_segments):
    """Return only line segments where x1=x2 or y1=y2"""
    line_segments_straight = []

    for segment in line_segments:
        if segment['x1'] == segment['x2'] or segment['y1'] == segment['y2']:
            line_segments_straight.append(segment)

    return line_segments_straight


def mark_straight_lines_on_diagram(diagram, line_segments):
    """Increment elements on diagram where line segments exist."""
    diagram_marked = np.array(diagram)

    for segment in line_segments:
        x_range = [x for x in range(segment['x1'], segment['x2']+1)]
        y_range = [y for y in range(segment['y1'], segment['y2']+1)]

        for x in x_range:
            for y in y_range:
                diagram_marked[x, y] += 1

    return diagram_marked


def get_num_points_with_x_lines(diagram, x_lines):
    """Return number of elements in diagram whose value is at least x_lines."""
    (rows, cols) = np.where(diagram >= x_lines)

    num_points = 0
    for coord in zip(rows, cols):
        num_points += 1

    return num_points


def part2(input_data):
    print('Q:')
    print(f'A: {ans}')