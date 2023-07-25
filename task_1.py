# Напишите функцию для транспонирования матрицы
from pprint import pprint

def m_transp(matrix):
    for i in range(len(matrix)):
        for j in range(i, len(matrix[i])):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        return

def printable(matrix):
    for i in matrix:
        print(i)
    print('-'*10)

m = [[1,2,3], [4,5,6], [7,8,9]]
printable(m)
m_transp(m)
printable(m)
