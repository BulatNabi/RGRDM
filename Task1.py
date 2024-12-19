class Task1:
    def find_length_between_virtex(self, matrix_1, x, y):
        if (x == y):
            print(f"Алгоритм закончен. Расстояние между вершинами {x} и {y} равно 0")
            return
        length = 1
        result_matrix = matrix_1
        while (result_matrix[x][y] == 0):
            length += 1
            result_matrix = result_matrix.dot(matrix_1)
            print(f"Степень матрицы {length}")
            print(result_matrix)
            print("-----------------------------------")
        print(f"Алгоритм закончен. Расстояние между вершинами {x} и {y} равно {length}")
        return

    def find_roads_count_between_virtex(self, matrix_1, length, x, y):
        if (x == y):
            print(f"Алгоритм закончен. Расстояние между вершинами {x} и {y} равно {matrix_1[x][y]}")
            return
        count = 1
        result_matrix = matrix_1
        while (count != length):
            count += 1
            result_matrix = result_matrix.dot(matrix_1)
            print(f"Степень матрицы {count}")
            print(result_matrix)
            print("-----------------------------------")
        print(f"Алгоритм закончен. Количество путей между вершинами {x} и {y} равно {result_matrix[x][y]}")
        return