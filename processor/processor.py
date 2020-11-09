from matrix import Matrix


class MatrixTester:

    def __init__(self):
        self.mode = 'main'

    @staticmethod
    def printer(result):
        if result is None:
            print('The operation cannot be performed.')
        else:
            print('The result is:')
            for i in range(len(result)):
                print(*result[i])

    @staticmethod
    def get_matrix(message='matrix'):
        x, y = [int(i) for i in input(f"Enter size of {message}: ").split()]
        print(f'Enter {message}:')
        return Matrix.create_matrix(x, y)

    def menus(self):

        if self.mode == 'main':
            print()
            print('1. Add matrices')
            print("2. Multiply matrix by a constant")
            print('3. Multiply matrices')
            print('4. Transpose matrix')
            print('0. Exit')
        elif self.mode == 'transpose':
            print()
            print('1. Main diagonal')
            print('2. Side diagonal')
            print('3. Vertical line')
            print('4. Horizontal line')
        self.choice()

    def choice(self):
        import sys

        choice = input('Your choice: ')
        if self.mode == 'main':
            if choice == '1':
                self.add_message()
            elif choice == '2':
                self.scalar_message()
            elif choice == '3':
                self.multiply_message()
            elif choice == '4':
                self.transpose()
            elif choice == '0':
                sys.exit()
            else:
                pass
        elif self.mode == 'transpose':
            self.transpose(choice)

    def add_message(self):
        m1 = self.get_matrix('first matrix')
        m2 = self.get_matrix('second matrix')
        result = m1.add_matrix(m2)
        self.printer(result)

    def scalar_message(self):
        m = self.get_matrix('matrix')
        result = m.multiply_constant()
        self.printer(result)

    def multiply_message(self):
        m1 = self.get_matrix('first matrix')
        m2 = self.get_matrix('second matrix')
        result = m1.multiply_matrix(m2)
        self.printer(result)

    def transpose(self, choice=None):

        if self.mode != 'transpose':
            self.mode = 'transpose'
            self.menus()
        if self.mode == 'transpose':

            m1 = self.get_matrix('matrix')
            self.printer(m1.transpose_matrix(choice))

    def start(self):

        while True:
            self.menus()
            self.mode = 'main'

def main():
    power = MatrixTester()
    power.start()


if __name__ == '__main__':
    main()
