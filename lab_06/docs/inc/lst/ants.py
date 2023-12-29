def ants(matrix, alpha, beta, k_evaporation, days, start_city):
    places = len(matrix)

    q = get_q(matrix)
    best_way = []
    min_dist = float("inf")
    pheromones = [[1 for i in range(places)] for j in range(places)]
    visibility = [
        [(1.0 / matrix[i][j] if (i != j) else 0) for j in range(len(matrix[i]))]
        for i in range(len(matrix))
    ]

    ants = places
    for day in range(days):
        route = np.arange(places)
        visited = [[start_city] for _ in range(ants)]
        for ant in range(ants):
            while len(visited[ant]) != ants:
                pk = find_ways(
                    pheromones, visibility, visited, places, ant, alpha, beta
                )
                chosen_place = choose_place(pk)
                visited[ant].append(chosen_place - 1)

            cur_length = get_length(matrix, visited[ant])

            if cur_length < min_dist:
                min_dist = cur_length
                best_way = visited[ant]

        pheromones = update_pheromones(
            matrix, places, visited, pheromones, q, k_evaporation
        )

    return min_dist, best_way
