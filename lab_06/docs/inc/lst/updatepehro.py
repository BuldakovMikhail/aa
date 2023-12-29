MIN_PHEROMONE = 0.01


def update_pheromones(matrix, places, visited, pheromones, q, k_evaporation):
    ants = places

    for i in range(places):
        for j in range(places):
            delta = 0
            for ant in range(ants):
                length = get_length(matrix, visited[ant])
                delta += q / length

            pheromones[i][j] *= 1 - k_evaporation
            pheromones[i][j] += delta
            if pheromones[i][j] < MIN_PHEROMONE:
                pheromones[i][j] = MIN_PHEROMONE

    return pheromones
