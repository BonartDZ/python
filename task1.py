class Matrix:

    def __init__(self, matrix, matrix1):
        self.matrix = matrix
        self.matrix1 = matrix1

    def __add__(self):
        matrix_result = [[0,0,0],[0,0,0]]

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix1[i])):
                matrix_result[i][j] = self.matrix[i][j] + self.matrix1[i][j]

        return '\n'.join('\t'.join(map(str, row)) for row in matrix_result)

    def __str__(self):
       return '\n'.join('\t'.join(map(str, row)) for row in self.matrix)

my_mtrx1 = Matrix([[1, 2, 3],[1, 2, 3]] , [[1, 1, 1],[1, 1, 1]])

print(my_mtrx1.__add__())

