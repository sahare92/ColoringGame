import sys

from gameboard import GameBoard

NUM_OF_ROWS_COLUMNS = 18
GAME_COLORS = ["r", "g", "b", "y"]
COLORS_COLOR = [1, 2, 4, 3]
ALLOWED_STEPS = 21


# starts a coloring game
def main():

    # create a game board - with randomized colors (rgby)
    gb = GameBoard(NUM_OF_ROWS_COLUMNS, GAME_COLORS, COLORS_COLOR)

    steps_played = 0

    print("Welcome to the Coloring Game!")
    print(f"Please enter one of the possible colors to play this game: {GAME_COLORS}")
    gb.print_board()

    # start listening on inputs from the user (the actual game)
    print(f"Available game colors: {GAME_COLORS}")
    print(f"Please select a color:")
    for line in sys.stdin:

        # game over if played too many steps
        if steps_played == ALLOWED_STEPS:
            print(f'Game over! Unfortunately you ran out of steps. (Allowed steps: {ALLOWED_STEPS})')
            break

        steps_played += 1

        # remove the newline char from the input line
        line = line[:-1]

        # when quit/q - exit game
        if line in ["quit", "q"]:
            print("Exiting game!")
            return

        # when input is a color - paint the board accordingly
        if line in GAME_COLORS:

            # color with the selected color
            gb.color(line)

        if gb.is_game_finished():
            print("Congratulations! you finished the game")
            break

        # TODO: add an option to retry

        print("Current game board:")
        gb.print_board()

        print(f"Please select the next color: (Remaining steps: {ALLOWED_STEPS - steps_played})")

    print("Goodbye! Hope to see you back soon!")


if __name__ == "__main__":
    main()
