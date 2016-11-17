import re, regex

def detect_html_tags(html_input):  # difficulty-level: easy
    """Takes html string and returns a sorted list of tags that occur in it."""

    tags = re.findall(r'< *(\w+)', html_input)
    tags = list(set(tags))

    return ';'.join(sorted(tags))

def is_valid_postal_re_module(postal):  # difficulty-level: hard
    """Takes string of a postal code and returns True if valid, False if not"""

    base_regex = re.compile(r'^[1-9][0-9]{5}$')
    alter_regex = re.compile(r'([0-9])[0-9](?=\1)')
    alter_matches = []

    # work-around for case of overlapping matches not available in re module
    for i in range(5):
        alter_matches += [bool(alter_regex.match(postal[i:]))]

    return sum(alter_matches) < 2 and bool(base_regex.search(postal))

def is_valid_postal_regex_module(postal):  # simpler with regex instead of re
    """Takes string of a postal code and returns True if valid, False if not"""

    base_regex = regex.compile(r'^[1-9][0-9]{5}$')
    alter_regex = regex.compile(r'([0-9])([0-9])(?=\1)')

    return (len(alter_regex.findall(postal, overlapped=True)) < 2
            and bool(base_regex.search(postal)))

def is_valid_credit_card_num(cc_num): # difficulty-level: medium
    """Takes string of a credit card number and determines it's validity."""

    cc_num = re.sub(r'^(\d{4})-(\d{4})-(\d{4})-(\d{4})$',
                    r'\1\2\3\4', cc_num)  # strip valid dashes

    if re.search(r'(?=[4-6])^(?:([0-9])(?!\1{3})){16}$', cc_num):
        return 'Valid'
    else:
        return 'Invalid'

def decode_matrix(matrix): # difficulty-level: hard
    """
    Takes multi-line string that starts with 'num_rows num_cols', then
    continues on the next line with a matrix of those dimensions with each
    value being a single character. Returns decoded message of characters
    read from the top to bottom of each column, going from left to right.
    Non-alphanumeric values between words are replaced with a single space.
    """

    matrix = matrix.split('\n')
    num_rows, num_cols = matrix[0].split()
    num_rows, num_cols = int(num_rows), int(num_cols)

    msg = []
    for col in range(num_cols):
        for row in range(1, num_rows+1):
            msg.append(matrix[row][col])

    return re.sub(r'\b[^A-Za-z0-9]+\b', r' ',''.join(msg))

