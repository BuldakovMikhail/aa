def brut(matrix, start_city):
    size = len(matrix)
    nodes = list(range(0, size))
    nodes.pop(start_city)

    min_dist = float("inf")
    best_way = []

    for comb in it.permutations(nodes):
        comb = [start_city] + list(comb)
        cur_dist = 0
        for i in range(len(comb) - 1):
            cur_dist += matrix[comb[i]][comb[i + 1]]

        if cur_dist < min_dist:
            min_dist = cur_dist
            best_way = comb

    return min_dist, best_way
