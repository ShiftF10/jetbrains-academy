class Matrix:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.m = [[0] * y for _ in range(x)]

    # Allows the use of the rest of the operations through the .command outside of this file
    @staticmethod
    def create_matrix(x, y):
        matrix = Matrix(x, y)  # Key line.
        matrix.m = [[Matrix.convert(float(i)) for i in input().split()] for _ in range(x)]
        return matrix

    @staticmethod
    def convert(number):
        return int(number) if float(number).is_integer() else float(number)

    def add_matrix(self, mat):

        if mat.x == self.x and mat.y == self.y:
            result = Matrix(self.x, self.y)
            result.m = [[self.m[i][j] + mat.m[i][j] for j in range(self.y)] for i in range(self.x)]
            return result
        else:
            return None

    def multiply_constant(self):

        scalar = self.convert(input('Enter constant: '))
        return [[self.m[i][j] * scalar for j in range(self.y)] for i in range(self.x)]

    def multiply_matrix(self, matrix):

        if self.y == matrix.x:
            result = matrix(self.x, matrix.y)
            for i in range(self.x):
                for j in range(matrix.y):
                    result.m[i][j] = [self.m[i][k] * matrix[k][j] for k in range(matrix.x)]
            return result
        else:
            return None

    def transpose_matrix(self, choice):

        if choice == '1':
            return [[self.m[j][i] for j in range(self.y)] for i in range(self.x)]
        elif choice == '2':
            return [[self.m[-j - 1][-i - 1] for j in range(self.y)] for i in range(self.x)]
        elif choice == '3':
            return [[self.m[i][-j - 1] for j in range(self.y)] for i in range(self.x)]
        elif choice == '4':
            return [[self.m[-i - 1][j] for j in range(self.y)] for i in range(self.x)]
