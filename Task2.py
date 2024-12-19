from collections import deque
import pandas as pd

class Task2:
    def find_articulation_points(self, matrix):
        #массив для точек сочленения
        articulation_points = []
        n = len(matrix)


        #Обход матрицы в ширину
        #Здесь мы находим число доступных вершин из стартовой,чтобы в дальнейшем проверить, увеличилось ли число компонент
        def findAvailableVertexes(adj_matrix, delete_vertex):
            """
                Проверяет, остается ли граф связным после удаления заданноq вершиныуу
            """
            visited = [False] * n
            start_vertex = 1 if delete_vertex == 0 else 0
            visited[start_vertex] = True

            queue = deque([start_vertex])#очередь для обхода графа
            #цикл продолжается пока очередь непустая
            while queue:
                currentV = queue.popleft()

                visited[currentV] = True

                for v in range(len(adj_matrix)):
                    #если текущая вершина (i) не удаленная(имитируем удаление вершины) и если текущая вершина (i) не посещена и
                    # между взятой вершиной (currentV) и текущей вершиной (i) есть ребро
                    if v != delete_vertex and not visited[v] and adj_matrix[currentV][v] != 0:
                        queue.append(v)

            counter = 0
            for i in visited:
                if(i):
                    counter += 1
            return counter


        for i in range(n):

            avaliable_vertexes = findAvailableVertexes(matrix, i)

            # Проверяем,увеличилось ли число компонент, те были ли посещены все вершины (кроме удаленной)
            if avaliable_vertexes != n - 1:  # n - 1, так как удалили одну вершину
                articulation_points.append(i)

        return articulation_points

    def find_bridges(self, matrix):
        bridges = []  # Список для хранения мостов
        n = len(matrix)  # Количество вершин в графе

        # Получение списка всех рёбер
        edges = []
        for i in range(n):
            for j in range(i + 1, n):  # Перебираем только верхний треугольник матрицы
                if matrix[i][j] == 1:
                    edges.append((i, j))

        def is_connected(adj_matrix, delete_edge):
            """
            Проверяет, остается ли граф связным после удаления заданного ребра.
            """
            visited = [False] * n
            # Если начальная вершина совпадает с удаляемым ребром, выбираем другую
            start_vertex = 1 if delete_edge[0] == 0 else 0

            # Очередь для обхода в ширину
            queue = deque([start_vertex])
            visited[start_vertex] = True

            while queue:
                current_vertex = queue.popleft()
                for v in range(n):
                    # Пропускаем удаляемое ребро
                    if ((current_vertex == delete_edge[0] and v == delete_edge[1]) or
                            (current_vertex == delete_edge[1] and v == delete_edge[0])):
                        continue
                    if not visited[v] and adj_matrix[current_vertex][v] == 1:
                        visited[v] = True
                        queue.append(v)

            # Если есть хотя бы одна непосещённая вершина, граф несвязный
            return all(visited)

        # Проверка каждого ребра
        for delete_edge in edges:
            if not is_connected(matrix, delete_edge):
                bridges.append(delete_edge)

        return bridges

