"""
Examples

This script is used for testing the different features of the TicTacToe script.

Note
----
    All test cases are commented out so the user doesn't run several test cases all at once accidentally.
"""

# TODO try the test cases and come up with more

from tictactoe import Tictactoe


def main() -> None:
    """Entry point for code to be run."""
    print("Testing:")
    # ttt = Tictactoe()
    # ttt.game()

    # ttt2 = Tictactoe(width_of_board=4, in_a_row_to_win=2)
    # ttt2.game()

    # ttt3 = Tictactoe(width_of_board=2, in_a_row_to_win=3)
    # ttt3.game()

    # Testing exception handling
    # ttt4 = Tictactoe(width_of_board=1)
    # ttt4.game()

    # ttt5 = Tictactoe(in_a_row_to_win=0)
    # ttt5.game()

    # ttt6 = Tictactoe(width_of_board=5, in_a_row_to_win="test")
    # ttt6.game()


if __name__ == "__main__":
    main()
