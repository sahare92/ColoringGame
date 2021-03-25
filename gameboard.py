import copy
import random

from colored import fg


class GameBoard(object):
    """
    An object representing a game board.
    Consists of NxN matrix where each element represents a color
    """

    def __init__(self, board_size, game_colors, colors_color):
        self._board_size = board_size
        self._game_colors = game_colors
        self._colors_color = colors_color
        self._board = self._generate_game_board()

    def print_board(self):
        for row in self._board:
            colored_row = ""
            for element in row:

                # add matching color code to each element and append it to the colored row's string
                color = fg(self._colors_color[self._game_colors.index(element)])
                colored_row = f"{colored_row} {color} {element} "

            print(colored_row)

    def is_game_finished(self):
        top_left_color = self._board[0][0]

        # make sure all the elements are of the same color as the first one
        for i in range(self._board_size):
            for j in range(self._board_size):
                if self._board[i][j] != top_left_color:
                    return False

        return True

    """
    Perform the coloring operation for the given new_color
    """
    def color(self, new_color):

        # create a copy of the previous elements - to be used to identify where we should color
        previous_board_copy = copy.deepcopy(self._board)
        original_color = self._board[0][0]

        # create a bool matrix in the size of BOARD_SIZE*BOARD_SIZE to mark where we visited
        visited_elements = []
        for i in range(self._board_size):
            row = []
            for j in range(self._board_size):
                row.append(False)
            visited_elements.append(row)

        # color up-down-left-right boxes if the neighbour element has the same color
        #  and call recursively to color the same way for neighbour elements
        self._color_element_and_neighbours(0, 0, new_color, original_color, previous_board_copy, visited_elements)

    def _color_element_and_neighbours(self, x, y, new_color, original_color, previous_board, visited_elements):

        # check if already visited the element - return
        if visited_elements[x][y]:
            return
        visited_elements[x][y] = True

        # color the current element
        self._board[x][y] = new_color

        # color matching neighbour elements, and call this function recursively

        # color down
        if x + 1 < self._board_size and previous_board[x + 1][y] == original_color:
            self._board[x + 1][y] = new_color
            self._color_element_and_neighbours(x + 1, y, new_color, original_color, previous_board, visited_elements)

        # color right
        if y + 1 < self._board_size and previous_board[x][y + 1] == original_color:
            self._board[x][y + 1] = new_color
            self._color_element_and_neighbours(x, y + 1, new_color, original_color, previous_board, visited_elements)

        # color up
        if x - 1 >= 0 and previous_board[x - 1][y] == original_color:
            self._board[x - 1][y] = new_color
            self._color_element_and_neighbours(x - 1, y, new_color, original_color, previous_board, visited_elements)

        # color left
        if y - 1 >= 0 and previous_board[x][y - 1] == original_color:
            self._board[x][y - 1] = new_color
            self._color_element_and_neighbours(x, y - 1, new_color, original_color, previous_board, visited_elements)

    def _generate_game_board(self):

        # create an empty board
        board = []

        # create the board matrix with random colors on each element
        for i in range(self._board_size):
            row = []
            for j in range(self._board_size):
                row.append(self._generate_random_color())

            board.append(row)

        return board

    def regenerate_game_board(self):
        self._board = self._generate_game_board()

    def _generate_random_color(self):
        return random.choice(self._game_colors)

    def _set_board(self, new_board):
        self._board = new_board
