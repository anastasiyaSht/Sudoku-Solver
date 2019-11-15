import unittest

from app import print_board, find_empty, validate, solve


class TestSudoku(unittest.TestCase):

    def test_find_empty(self):
        board = [
            [6, 0, 5],
            [0, 0, 0],
            [0, 1, 8],
        ]
        self.assertEqual(find_empty(board), (0, 1))

    def test_validate(self):
        board = [
            [6, 0, 5],
            [0, 0, 0],
            [0, 1, 8],
        ]
        self.assertFalse(validate(board, 6, (0, 1)))

    def test_solve(self):
        board = [
            [6, 0, 5, 2, 0, 0, 7, 0, 8],
            [0, 0, 0, 0, 0, 8, 0, 9, 0],
            [0, 1, 8, 0, 0, 0, 2, 0, 0],
            [0, 6, 1, 0, 0, 7, 9, 5, 0],
            [0, 0, 0, 1, 0, 5, 0, 0, 6],
            [5, 3, 0, 6, 0, 2, 0, 0, 0],
            [0, 0, 0, 5, 2, 0, 0, 7, 0],
            [0, 5, 0, 7, 0, 4, 0, 6, 2],
            [0, 7, 0, 9, 6, 3, 0, 0, 4],
        ]

        board_ready = [
            [6, 4, 5, 2, 1, 9, 7, 3, 8],
            [7, 2, 3, 4, 5, 8, 6, 9, 1],
            [9, 1, 8, 3, 7, 6, 2, 4, 5],
            [2, 6, 1, 8, 4, 7, 9, 5, 3],
            [8, 9, 7, 1, 3, 5, 4, 2, 6],
            [5, 3, 4, 6, 9, 2, 8, 1, 7],
            [4, 8, 6, 5, 2, 1, 3, 7, 9],
            [3, 5, 9, 7, 8, 4, 1, 6, 2],
            [1, 7, 2, 9, 6, 3, 5, 8, 4],
        ]
        solve(board)
        self.assertEqual(board, board_ready)


if __name__ == '__main__':
    test = TestSudoku()
    test.test_find_empty()
    test.test_validate()
