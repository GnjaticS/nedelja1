def solution(sequence):

    index = 0

    is_sequence = True


    while index + 1 < len(sequence) and sequence[index + 1] - sequence[index] != 1:
        sequence.remove(sequence[index + 1])
        if index + 1 < len(sequence) and sequence[index + 1] - sequence[index] > 1:
            sequence.remove(sequence[index + 1])
            index += 1
    index += 1


    if index + 1 >= len(sequence):
        is_sequence = False
    elif index + 1 >= len(sequence) and sequence[index + 1] - sequence[index] != 1:
        is_sequence = True


    elif index + 1 >= len(sequence) and sequence[index + 1] - sequence[index] != 1:
        sequence.remove(sequence[index + 1])
        is_sequence = False
        index += 1


    return is_sequence

sequence = [1, 3, 2]
print(solution(sequence))