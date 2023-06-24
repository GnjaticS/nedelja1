def solution(sequence):


    is_sequence = True

    index = 0

    sequence2 = list(set(sequence))

    if len(sequence) - len(sequence2) > 0:
        is_sequence = False
        return is_sequence

    sequence2.sort()

    while True:
        if index + 1 < len(sequence2) and sequence2[index + 1] - sequence2[index] != 1:
            sequence2.remove(sequence2[index + 1])
            index += 1
        if index + 1 < len(sequence2) and sequence2[index + 1] - sequence2[index] > 1:
            sequence2.remove(sequence[index + 1])

            is_sequence = False
            break
        if index + 1 >= len(sequence2):
            is_sequence = False
            break
        index += 1
    if index + 1 >= len(sequence2):
        is_sequence = True
        index = 0

    while True:
        if index + 1 < len(sequence2) and sequence2[index + 1] - sequence2[index] != 1:
            sequence2.remove(sequence2[index + 1])
            index += 1
        if index + 1 < len(sequence2) and sequence2[index + 1] - sequence2[index] > 1:
            sequence2.remove(sequence[index + 1])

            is_sequence = False
            break
        if index + 1 >= len(sequence2):
            is_sequence = True
            break
        index += 1

    return is_sequence


#sequence = [0, -2, 5, 6]
#print(solution(sequence))
print(__name__)
import grammar