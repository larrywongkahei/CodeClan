class Matrix:
    def __init__(self, matrix_string):
        self.matrix_list = matrix_string.split("\n")

    def row(self, index):
        return [int(num) for num in self.matrix_list[index-1].split()]
                    

    def column(self, index):
        return [int(num.split()[index-1]) for num in self.matrix_list]
