import re


def decode_matrix(matrix): # difficulty-level: hard
    """Takes multi-line string that starts with 'num_rows num_cols', then
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


matrix_data = [input()]
num_rows, _ = matrix_data[0].split()

for _ in range(int(num_rows)):
    matrix_data.append(input())

print(decode_matrix('\n'.join(matrix_data)))
