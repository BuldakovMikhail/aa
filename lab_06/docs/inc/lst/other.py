def choose_place(pk):
    posibility = random()
    choice = 0
    chosen_place = 0
    while (choice < posibility) and (chosen_place < len(pk)):
        choice += pk[chosen_place]
        chosen_place += 1

    return chosen_place


def get_q(matrix):
    q = 0
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i != j:
                q += matrix[i][j]
                count += 1
    return q / count


def get_length(matrix, route):
    length = 0

    for way_len in range(1, len(route)):
        length += matrix[route[way_len - 1]][route[way_len]]

    return length
