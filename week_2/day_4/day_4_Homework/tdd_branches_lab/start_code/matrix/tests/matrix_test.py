import unittest

from src.matrix import Matrix

class MatrixTest(unittest.TestCase):
    def test_extract_row_from_one_number_matrix(self):
        matrix = Matrix("1")
        self.assertEqual(matrix.row(1), [1])

    # # Test_can_extract_a_givenrow
    def test_extract_a_row(self):
        matrix = Matrix("1 2 3\n4 5 6")
        expected_outcome = [1, 2, 3]
        actual_outcome = matrix.row(1)
        self.assertEqual(expected_outcome, actual_outcome)

    # # Test can extract a given row where numbers have different number of digits
    # # Example matrix:
    def test_extract_with_different_number(self):
        matrix = Matrix("1 2\n10 20")
        expected_outcome = [1, 2]
        actual_outcome = matrix.row(1)
        self.assertEqual(expected_outcome, actual_outcome)

    def test_extract_with_different_number2(self):
        matrix = Matrix("1 2\n10 20")
        expected_outcome = [10, 20]
        actual_outcome = matrix.row(2)
        self.assertEqual(expected_outcome, actual_outcome)
    
    # #
    # # 1 2
    # 10 20

    # Test can extract row from non-square matrix
    def test_extract_non_square(self):
        matrix = Matrix("1 2 3\n4 5 6\n7 8 9\n10 11 12\n13 14 15")
        expected_outcome = [1, 2, 3]
        actual_outcome = matrix.row(1)
        self.assertEqual(expected_outcome, actual_outcome)



    def test_extract_non_square2(self):
        matrix = Matrix("1 2 3\n4 5 6\n7 8 9\n10 11 12\n13 14 15")
        expected_outcome = [4, 5, 6]
        actual_outcome = matrix.row(2)
        self.assertEqual(expected_outcome, actual_outcome)
    # Example matrix:
    #
    # 1 2 3
    # 4 5 6
    # 7 8 9
    # 8 7 6

    # Test can extract a column
    def test_extract_a_column(self):
        matrix = Matrix("1 2 3\n4 5 6\n7 8 9\n10 11 12\n13 14 15")
        expected_outcome = [1, 4, 7, 10, 13]
        actual_outcome = matrix.column(1)
        self.assertEqual(expected_outcome, actual_outcome)


    # Test can extract column from a one number matrix
    def test_extract_column_from_a_one_number(self):
        matrix = Matrix("1")
        expected_outcome = [1]
        actual_outcome = matrix.column(1)
        self.assertEqual(expected_outcome, actual_outcome)


    def test_extract_column_from_a_one_number2(self):
        matrix = Matrix("1\n2\n3")
        expected_outcome = [1,2,3]
        actual_outcome = matrix.column(1)
        self.assertEqual(expected_outcome, actual_outcome)
    # Test can extract a column from non-square matrix

    def test_extract_a_column_from_non_square_matrix(self):
        matrix = Matrix("1 2 3 4\n5 6 7 8\n9 10 11 12\n13 14 15 16")
        expected_outcome = [1, 5, 9, 13]
        actual_outcome = matrix.column(1)
        self.assertEqual(expected_outcome, actual_outcome)

    def test_extract_a_column_from_non_square_matrix2(self):
        matrix = Matrix("1 2 3 4\n5 6 7 8\n9 10 11 12\n13 14 15 16")
        expected_outcome = [3, 7, 11, 15]
        actual_outcome = matrix.column(3)
        self.assertEqual(expected_outcome, actual_outcome)

    def test_extract_a_column_from_non_square_matrix3(self):
        matrix = Matrix("1 2 3 4\n5 6 7 8\n9 10 11 12\n13 14 15 16")
        expected_outcome = [4, 8, 12, 16]
        actual_outcome = matrix.column(4)
        self.assertEqual(expected_outcome, actual_outcome)
    # Example matrix:
    #
    # 1 2 3 4
    # 5 6 8 8
    # 9 8 7 6

    # Test can extract column when numbers have different number of digits
    # Example matrix:
    def test_can_extracr_column_when_have_different_number(self):
        matrix = Matrix("89 1903 3\n18 3 1\n 9 4 800")
        expected_outcome = [89, 18, 9]
        actual_outcome = matrix.column(1)
        self.assertEqual(expected_outcome, actual_outcome)

    def test_can_extracr_column_when_have_different_number2(self):
        matrix = Matrix("89 1903 3\n18 3 1\n 9 4 800")
        expected_outcome = [1903, 3, 4]
        actual_outcome = matrix.column(2)
        self.assertEqual(expected_outcome, actual_outcome)

    def test_can_extracr_column_when_have_different_number3(self):
        matrix = Matrix("89 1903 3\n18 3 1\n 9 4 800")
        expected_outcome = [3, 1, 800]
        actual_outcome = matrix.column(3)
        self.assertEqual(expected_outcome, actual_outcome)
    # 89 1903 3
    # 18 3 1
    # 9 4 800



