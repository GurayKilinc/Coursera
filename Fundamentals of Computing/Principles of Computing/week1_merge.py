"""
Merge function for 2048 game.
"""
def slide_left(line):
    """
    To make all non-zero integers to be at the left of the list
    """
    length = len(line)
    count = 0
    output = [0] * length
    for i in range(length):
        if line[i] != 0:
            output[i - count] = line[i]
        else:
            count += 1
    return output

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    output = slide_left(line)
    for i in range(len(line) - 1):
        if output[i] != 0 and output[i] == output[i + 1]:
            output[i] *= 2
            output[i + 1] = 0
    output = slide_left(output)
    return output

# print(merge([8, 16, 16, 8]))