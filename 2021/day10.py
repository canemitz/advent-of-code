import re


def part1(nav_subsystem):
    print('Q: Find the first illegal character in each corrupted line of the navigation subsystem.')
    print('   What is the total syntax error score for those errors?')

    first_illegal_chars = []
    for line in nav_subsystem.readlines():
        first_illegal_char = get_first_illegal_char(line)
        if first_illegal_char:
            first_illegal_chars.append(first_illegal_char)

    illegal_char_points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    total_syntax_error_score = sum([illegal_char_points[x] for x in first_illegal_chars])

    print(f'A: {total_syntax_error_score}')


def remove_chunks(line):
    """Recurse through a line, removing atomic chunks.
    Returns corrupted or incomplete line, or empty string.
    """
    atomic_chunk_regex = r'\(\)|\[\]|{}|<>'

    # Remove chunks until line does not change
    line_reduced = line.strip()
    while re.sub(atomic_chunk_regex, '', line_reduced) != line_reduced:
        line_reduced = re.sub(atomic_chunk_regex, '', line_reduced)

    return line_reduced


def get_first_illegal_char(line):
    """Return first illegal char if line is corrupted, else return an emptry string."""

    line_reduced = remove_chunks(line)

    illegal_chars_regex = r'\)|\]|}|>'
    illegal_chars = re.findall(illegal_chars_regex, line_reduced)

    first_illegal_char = illegal_chars.pop(0) if illegal_chars else ''

    return first_illegal_char


def part2(nav_subsystem):
    print('Q: Find the completion string for each incomplete line, score the completion strings, and sort the scores.')
    print('   What is the middle score?')

    incomplete_lines = get_incomplete_lines(nav_subsystem)

    scores = []
    for line in incomplete_lines:
        completion_string = get_completion_string(line)
        completion_string_score = get_completion_string_score(completion_string)
        scores.append(completion_string_score)

    scores.sort()
    median_score = scores[int( (len(scores)-1) / 2 )]

    print(f'A: {median_score}')


def get_incomplete_lines(nav_subsystem):
    """Returns list of [reduced] incomplete lines"""
    incomplete_lines = []

    for line in nav_subsystem.readlines():
        line_reduced = remove_chunks(line)
        if not get_first_illegal_char(line_reduced):
            incomplete_lines.append(line_reduced)

    return incomplete_lines


def get_completion_string(incomplete_line):
    """Given a reduced incomplete line, return the completion string for it."""
    closing_char_lookup = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }

    completion_string = ''

    line_reversed = incomplete_line[::-1]
    for char in line_reversed:
        # if char in closing_char_lookup.keys():
        completion_string += closing_char_lookup[char]

    return completion_string


def get_completion_string_score(completion_string):
    """Get score of closing characters."""
    closing_char_points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }

    score = 0
    for char in completion_string:
        score *= 5
        score += closing_char_points[char]

    return score