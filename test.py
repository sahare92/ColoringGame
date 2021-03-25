import unittest

import gameboard


class TestGameboard(unittest.TestCase):

    def setUp(self):
        self._game_colors = ["r", "g", "b", "y"]
        self._colors_color = [1, 2, 4, 3]

    def test_is_board_finished_true(self):
        board_size = 18

        gb = gameboard.GameBoard(18, self._game_colors, self._colors_color)

        # create a mock board with only red elements
        mock_board = []
        for i in range(board_size):
            row = []
            for j in range(board_size):
                row.append("r")

            mock_board.append(row)

        gb._set_board(mock_board)

        self.assertTrue(gb.is_game_finished())

    def test_is_board_finished_false(self):
        board_size = 18

        gb = gameboard.GameBoard(18, self._game_colors, self._colors_color)

        # create a mock board with only red elements
        mock_board = []
        for i in range(board_size):
            row = []
            for j in range(board_size):
                row.append("r")

            mock_board.append(row)

        # set one different element
        mock_board[0][0] = "y"

        gb._set_board(mock_board)

        self.assertFalse(gb.is_game_finished())


if __name__ == "__main__":
    unittest.main()
