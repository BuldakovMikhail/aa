import numpy as np
import itertools as it

from random import random

MIN_PHEROMONE = 0.01

test = [
    [0, 6, 1, 9, 9],
    [1, 0, 6, 2, 7],
    [1, 4, 0, 6, 5],
    [8, 5, 5, 0, 8],
    [5, 1, 4, 8, 0],
]


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


def find_ways(pheromones, visibility, visited, places, ant, alpha, beta):
    pk = [0] * places

    for place in range(places):
        if place not in visited[ant]:
            ant_place = visited[ant][-1]
            pk[place] = pow(pheromones[ant_place][place], alpha) * pow(
                visibility[ant_place][place], beta
            )
        else:
            pk[place] = 0

    sum_pk = sum(pk)

    for place in range(places):
        pk[place] /= sum_pk

    return pk


def choose_place(pk):
    posibility = random()
    choice = 0
    chosen_place = 0
    while (choice < posibility) and (chosen_place < len(pk)):
        choice += pk[chosen_place]
        chosen_place += 1

    return chosen_place


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


print(brut(test, 0))

print(ants(test, 0.5, 0.5, 2, 100, 0))
