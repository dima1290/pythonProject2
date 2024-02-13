# Создайте программу для работы с матрицей, представленной в виде списка списков. Реализуйте следующие функции:
#
# Создание матрицы:
#
# Пользователь вводит количество строк и столбцов матрицы.
# Программа создает матрицу, заполняя ее случайными значениями.
# Вывод матрицы:
#
# Программа выводит матрицу в удобочитаемом виде, отформатированном в виде таблицы.
# Транспонирование матрицы:
#
# Программа транспонирует матрицу (меняет строки и столбцы местами) и выводит результат.
# Сумма элементов в каждой строке:
#
# Программа выводит сумму элементов в каждой строке матрицы.
# Умножение матрицы на число:
#
# Пользователь вводит число.
# Программа умножает каждый элемент матрицы на введенное число и выводит результат.

from prettytable import PrettyTable
import random
trans = []
i1 = int(input("Введите количество строк: "))
j1 = int(input("Введите количество столбцов: "))

def create_table(i, j):
    list_1 = []
    for i in range(i1):
        list_2 = []
        for j in range(j1):
            list_2.append(random.randint(0, 99))
        list_1.append(list_2)
    return list_1

def print_table(list):
    my_table = PrettyTable()
    for l1 in list:
        my_table.add_row(l1)
    print(my_table)

def transposed_table(list):
    rows = len(list)
    cols = len(list[0])

    transposed_table = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed_table[j][i] = list[i][j]
    return  transposed_table

def multiplication_table(list):
    mult = int(input("На какое число умножать?: "))
    rows = len(list)
    cols = len(list[0])

    for i in range(rows):
        for j in range(cols):
            list[i][j] = list[i][j] * mult
    return list

def addition_table(list):
    out = []
    for i in list:
        added = 0
        for j in i:
            added += j
        i.append(added)
        out.append(i)
    return out



list_1 = create_table(i=i1, j=j1)

while True:
    print(f" 1.Вывод таблицы \n 2.Транспонирование матрицы \n 3.Умножение матрицы на число \n 4.Сложение элементов строк:")
    fun = input("Выберите один из вариантов: ")


    if fun == "1":
        print_table(list_1)
    if fun == "2":
        list_1 = transposed_table(list_1)
        print_table(list_1)
    if fun == "3":
        list_1 = multiplication_table(list_1)
        print_table(list_1)
    if fun == "4":
        list_1 = addition_table(list_1)
        print_table(list_1)
