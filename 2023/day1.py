import re
import regex


def part1(calibration_document):
    print('Q: Consider your entire calibration document. What is the sum of all of the calibration values?')

    calibration_values = []
    for line in calibration_document:
        digits = re.findall(r'\d', line)
        if digits:
            calibration_value = int(digits[0] + digits[-1])
            calibration_values.append(calibration_value)

    ans = sum(calibration_values)

    print(f'A: {ans}')


def part2(calibration_document):
    print('Q: It looks like some of the digits are actually spelled out with letters. What is the real sum of all of the calibration values?')

    digit_lookup = {
        'one'  : '1',
        'two'  : '2',
        'three': '3',
        'four' : '4',
        'five' : '5',
        'six'  : '6',
        'seven': '7',
        'eight': '8',
        'nine' : '9',
        '1'    : '1',
        '2'    : '2',
        '3'    : '3',
        '4'    : '4',
        '5'    : '5',
        '6'    : '6',
        '7'    : '7',
        '8'    : '8',
        '9'    : '9'
    }

    calibration_values = []
    for line in calibration_document:
        # Using re, would need to use lookarounds (which I'm not very adept at)...something like the following, but not quite
        # digits = [ match.group() for match in re.finditer(r'\b(?:one|two|three|four|five|six|seven|eight|nine|\d+)\b', line )]

        # So instead, use the non-core regex module which finds overlapping matches
        digits = regex.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line, overlapped=True)

        if digits:
            digit_a = digit_lookup.get(digits[0])
            digit_b = digit_lookup.get(digits[-1])

            calibration_value = int(digit_a + digit_b)
            calibration_values.append(calibration_value)

    ans = sum(calibration_values)

    print(f'A: {ans}')


def part2_alt1(calibration_document):
    print('Q: It looks like some of the digits are actually spelled out with letters. What is the real sum of all of the calibration values?')

    digit_lookup = {
        'one'  : '1',
        'two'  : '2',
        'three': '3',
        'four' : '4',
        'five' : '5',
        'six'  : '6',
        'seven': '7',
        'eight': '8',
        'nine' : '9'
    }
    digit_lookup_r = { key[::-1]: digit_lookup[key] for key in digit_lookup.keys() }

    digit_word_pattern = r'|'.join(list( digit_lookup.keys() ))
    digit_word_pattern_r = digit_word_pattern[::-1]

    calibration_document_parsed = []
    for line in calibration_document:
        # Split line into chunks of digits and characters
        line_chunks = re.split(r'(\d+)', line)

        line_parsed = ''
        for chunk in line_chunks:
            # add the chunk of digits to line_parsed
            if chunk.isdigit():
                line_parsed += chunk
            # add the first and last digit words in the chunk to line_parsed
            else:
                first_match = re.search(digit_word_pattern, chunk)
                if first_match:
                    line_parsed += digit_lookup.get(first_match[0])

                chunk_r = chunk[::-1]
                last_match = re.search(digit_word_pattern_r, chunk_r)
                if last_match:
                    line_parsed += digit_lookup_r.get(last_match[0])

        calibration_document_parsed.append(line_parsed)

    print('Relevant words in calibration document converted to digits; passing to part1...\n')
    part1(calibration_document_parsed)