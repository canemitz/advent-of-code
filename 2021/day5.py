import numpy as np


def part1(input_data):
    print('Q: Consider only horizontal and vertical lines. At how many points do at least two lines overlap?')

    line_segments = get_line_segments(input_data)

    diagram = get_initial_diagram(line_segments)
    diagram_marked = mark_straight_lines_on_diagram(diagram, line_segments)

    ans = get_num_points_with_x_lines(diagram_marked, x_lines=2)

    print(f'A: \n{ans}')


def get_line_segments(input_data):
    """Return list of dictionaries of coordinates for each segment.
    Example:
        input_data = '0,9 -> 5,9'
        line_segments = [{'x1': 0, 'y1': 9, 'x2': 5, 'y2': 9}]
    """
    line_segments_list = ''.join(input_data.readlines()).split('\n')
    line_segments_list = [x.split(' -> ') for x in line_segments_list]

    line_segments = []
    for segment in line_segments_list:
        (x_1, y_1) = segment[0].split(',')
        (x_2, y_2) = segment[1].split(',')
        segment_dict = {
            'x1': int(x_1),
            'x2': int(x_2),
            'y1': int(y_1),
            'y2': int(y_2)
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


def get_filtered_line_segments(line_segments, line_filter):
    """Filter out line segments where x1=x2 or y1=y2
    Return those if line_filter is straight, else return the other segments
    """
    line_segments_filtered = []

    for segment in line_segments:
        if (segment['x1'] == segment['x2'] or segment['y1'] == segment['y2']):
            if line_filter == 'straight':
                line_segments_filtered.append(segment)
        elif line_filter == 'diagonal':
            line_segments_filtered.append(segment)

    return line_segments_filtered


def mark_straight_lines_on_diagram(diagram, line_segments):
    """Increment elements on diagram where straight line segments exist."""
    diagram_marked = np.array(diagram)
    line_segments_straight = get_filtered_line_segments(line_segments, 'straight')

    for segment in line_segments_straight:
        x1 = segment['x1']
        x2 = segment['x2']
        y1 = segment['y1']
        y2 = segment['y2']

        x_increment = 1 if x1 < x2 else -1
        y_increment = 1 if y1 < y2 else -1

        for x in range(x1, x2+x_increment, x_increment):
            for y in range(y1, y2+y_increment, y_increment):
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
    print('Q: Consider all of the lines. At how many points do at least two lines overlap?')

    line_segments = get_line_segments(input_data)

    diagram = get_initial_diagram(line_segments)
    diagram_marked = mark_straight_lines_on_diagram(diagram, line_segments)
    diagram_marked = mark_diagonal_lines_on_diagram(diagram_marked, line_segments)

    ans = get_num_points_with_x_lines(diagram_marked, x_lines=2)
    print(f'A: {ans}')


def mark_diagonal_lines_on_diagram(diagram, line_segments):
    """Increment elements on diagram where diagonal line segments exist."""
    diagram_marked = np.array(diagram)

    line_segments_diagonal = get_filtered_line_segments(line_segments, 'diagonal')

    for segment in line_segments_diagonal:
        x1 = segment['x1']
        x2 = segment['x2']
        y1 = segment['y1']
        y2 = segment['y2']

        x_increment = 1 if x1 < x2 else -1
        y_increment = 1 if y1 < y2 else -1

        for x, y in zip(range(x1, x2+x_increment, x_increment), range(y1, y2+y_increment, y_increment)):
            diagram_marked[x, y] += 1

    return diagram_marked