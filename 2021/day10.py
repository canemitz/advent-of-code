import re

chunk_type = {
    '(': 'paren',
    ')': 'paren',
    '[': 'square',
    ']': 'square',
    '{': 'curly',
    '}': 'curly',
    '<': 'angle',
    '>': 'angle'
}

illegal_char_scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}


def part1(nav_subsystem):
    print('Q: Find the first illegal character in each corrupted line of the navigation subsystem.')
    print('   What is the total syntax error score for those errors?')

    first_illegal_chars = []
    for line in nav_subsystem.readlines():
        first_illegal_char = get_first_illegal_char(line)
        if first_illegal_char:
            first_illegal_chars.append(first_illegal_char)

    total_syntax_error_score = sum([illegal_char_scores[x] for x in first_illegal_chars])

    print(f'A: {total_syntax_error_score}')


def remove_chunks(line):
    """Recurse through a line, removing atomic chunks.
    Returns corrupted or incomplete line, or empty string.
    """
    atomic_chunk_regex = r'\(\)|\[\]|{}|<>'

    # Remove chunks until line does not change
    line_reduced = line
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
    print('Q:')
    print(f'A: {ans}')