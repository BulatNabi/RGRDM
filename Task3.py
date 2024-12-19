import heapq

import numpy as np


def dijkstra(adj_matrix, start):
    n = len(adj_matrix)
    distances = [float('inf')] * n
    distances[start] = 0
    priority_queue = [(0, start)]  # (distance, vertex)

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor in range(n):
            if adj_matrix[current_vertex][neighbor] > 0:  # если есть ребро
                distance = current_distance + adj_matrix[current_vertex][neighbor]

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

    return distances

class Task3:



    def find_graph_center(self, adj_matrix):
        n = len(adj_matrix)
        min_max_distance = float('inf')
        centers = []

        for vertex in range(n):
            distances = dijkstra(adj_matrix, vertex)
            max_distance = max(distances)

            if max_distance < min_max_distance:
                min_max_distance = max_distance
                centers = [vertex]
            elif max_distance == min_max_distance:
                print(max_distance)
                centers.append(vertex)

        return centers



