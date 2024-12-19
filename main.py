import pandas as pd
import openpyxl
from Task1 import Task1
from Task2 import Task2
from Task3 import Task3


def read_matrix_from_excel(file_path):
    try:
        # Чтение данных из Excel-файла
        adjacency_matrix = pd.read_excel(file_path, header=None)

        # Проверка на квадратность матрицы
        if adjacency_matrix.shape[0] != adjacency_matrix.shape[1]:
            raise ValueError("Матрица смежности должна быть квадратной.")

        return adjacency_matrix

    except ValueError as ve:
        print(f"Ошибка: {ve}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


def main():
# #Task1
#     file_path_for_first_task = "matrix1.xlsx"
#     file_path_for_Vlad = "C:\\Users\\булат\\Downloads\\Лист Microsoft Excel.xlsx"
#     first_matrix = read_matrix_from_excel(file_path_for_Vlad)
#
#
#     first_task = Task1()
#     #Изначальная матрица смежности
#     if first_matrix is not None:
#         print("Изначальная матрица смежности:")
#         print(first_matrix)
#
#     #Расстояние между вершинами x1 и y1
#     x1 = int(input("Введите первую вершину: "))
#     y1 = int(input("Введите вторую вершину: "))
#     first_task.find_length_between_virtex(first_matrix, x1, y1)
#
#     # Количество маршрутов между x2 и y2 расстоянием l2
#     x2 = int(input("Введите первую вершину: "))
#     y2 = int(input("Введите вторую вершину: "))
#     l2 = int(input("Введите длину маршрутов: "))
#     first_task.find_roads_count_between_virtex(first_matrix, l2, x2, y2)

# #Task2
    file_path_for_second_task = "matrix2.xlsx"
    second_matrix = read_matrix_from_excel(file_path_for_second_task)

    second_task = Task2()

    if second_matrix is not None:
        print("Изначальная матрица смежности:")
        print(second_matrix)
    articulation_points = second_task.find_articulation_points(second_matrix.values)
    bridges = second_task.find_bridges(second_matrix)
    print("Точки сочленения:", articulation_points)
    print("Мосты:", bridges)

#Task3
    # file_path_for_third_task = "matrix3.xlsx"
    # third_matrix = read_matrix_from_excel(file_path_for_third_task)
    #
    # third_task = Task3()
    #
    # if third_matrix is not None:
    #     print("Изначальная матрица смежности:")
    #     print(third_matrix)
    # centers = third_task.find_graph_center(third_matrix)
    # print("Центры:", centers)


main()
