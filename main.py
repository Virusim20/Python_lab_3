import math
import os


def main():
  print("Практична робота №3 Маріанна Забрянська 312ст")
  task1()
  input()
  os.system('cls' if os.name == 'nt' else 'clear')
  print("Завдання 2\n")
  task2('/home/runner/Lab3/matrix.txt')


def Swap(X, Y):
  """Міняє вміст змінних X і Y."""
  X, Y = Y, X
  return X, Y


def task1():
  # Задання початкових значень для змінних A, B, C, D
  A = float(input("Введіть число A: "))
  B = float(input("Введіть число B: "))
  C = float(input("Введіть число C: "))
  D = float(input("Введіть число D: "))

  # Поміняти вміст пар змінних
  A, B = Swap(A, B)  # Поміняти A і B
  C, D = Swap(C, D)  # Поміняти C і D
  B, C = Swap(B, C)  # Поміняти B і C

  # Вивести нові значення змінних
  print("Нові значення A, B, C, D:", A, B, C, D)


def read_matrix_from_file(file_path):
  """Зчитати матрицю з текстового файлу."""
  with open(file_path, 'r') as file:
    matrix = [[int(num) for num in line.split()] for line in file]
  return matrix


def find_column_with_min_sum(matrix):
  """Знайти стовпець з найменшою сумою елементів."""
  min_sum_column = min(range(len(matrix[0])),
                       key=lambda col: sum(row[col] for row in matrix))
  return min_sum_column


def print_min_sum_column_info(min_sum_column, min_sum_value):
  """Вивести інформацію про стовпець з найменшою сумою."""
  print(f"Номер стовпця з найменшою сумою: {min_sum_column + 1}")
  print(f"Значення найменшої суми: {min_sum_value}")


def sort_matrix_by_columns_desc(matrix):
  """Відсортувати матрицю по стовпцях у порядку спадання."""
  sorted_matrix = [sorted(column, reverse=True) for column in zip(*matrix)]
  return list(map(list, zip(*sorted_matrix)))


def task2(file_path):
  # Зчитати матрицю з файлу
  matrix = read_matrix_from_file(file_path)

  # Знайти стовпець з найменшою сумою
  min_sum_column = find_column_with_min_sum(matrix)
  min_sum_value = sum(row[min_sum_column] for row in matrix)

  # Вивести інформацію про стовпець з найменшою сумою
  print_min_sum_column_info(min_sum_column, min_sum_value)

  # Відсортувати матрицю по стовпцях у порядку спадання
  sorted_matrix = sort_matrix_by_columns_desc(matrix)

  # Вивести відсортовану матрицю
  print("Відсортована матриця:")
  for row in sorted_matrix:
    print(row)


main()
