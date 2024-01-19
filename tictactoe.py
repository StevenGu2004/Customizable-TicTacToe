""" 
Customizable TicTacToe

This script can be used to generate a game of TicTacToe played via command line user inputs, 
where the player can flexibly declare the size of the board and the amount of equivalent marks needed
in a row, column or diagonal in succession for a player to win.

Example
-------
    see: examples.py

"""


class Tictactoe:
    """Create a game of Command line TicTacToe."""

    def __init__(self,
                 width_of_board=3,
                 in_a_row_to_win=3):
        """
        Initialize a game of TicTacToe.

        Optional Parameters
        -------------------
        width_of_board : Maximum amount of marks that can be placed along a side of the square board
        in_a_row_to_win : Number of equivalent marks needed in succession whether in a row, column, 
                          or diagonal needed for a player to win
        """

        # Exceptions
        if not isinstance(width_of_board, int) or width_of_board <= 1:
            raise ValueError(
                "The width of board must be an integer greater than 1.")

        if not isinstance(in_a_row_to_win, int) or in_a_row_to_win <= 1:
            raise ValueError(
                "The amount of marks needed to win (in succession) must be an integer greater than 1.")

        self.n = width_of_board
        self.game_over = False
        self.board = {(i, j): " " for i in range(self.n)
                      for j in range(self.n)}
        self.history = [self.board.copy()]
        self.x_turn = True
        self.k = in_a_row_to_win

    def generate_line(self) -> str:
        """ 
        Generate a line that divides each row of the game board.

        Return
        ------
        Line of dashes that nicely divide rows of game board
        """
        return '-' * (4 * self.n - 1)

    def get_player_this_turn(self) -> str:
        """ 
        Get the player for the current turn of game.

        Return
        ------
        Alias of the current player's mark
        """
        return "X" if self.x_turn else "O"

    def display_board(self,
                      board: dict[tuple[int], str]) -> None:
        """ 
        Display the board state as strings.

        Parameter
        ---------
        board : Game state of marks and their respective positions on the board
        """
        # Columns label
        print("  ", end="")
        for i in range(self.n):
            print(" " + str(i) + "  ", end="")
        print("")
        # Display the board
        for i in range(self.n):
            # Rows label
            print(str(i) + " ", end="")
            for j in range(self.n):
                print(board[(i, j)] if i == self.n - 1 and j == self.n - 1
                      else " " + board[((i, j))] + " | " if j == 0
                      else board[((i, j))] + " | " if j != self.n - 1
                      else board[((i, j))] + "\n" + "  " + self.generate_line() + "\n", end="")
        print("\n")

    def check_win(self) -> bool:
        """ 
        Check if a player has won.

        Return
        ------
        Boolean of whether or not a winner has been decided.
        """
        won = False
        player_this_turn = self.get_player_this_turn()
        for i in range(self.n):
            for k in range(self.n - self.k + 1):
                row_k = [self.board[(i, index)]
                         for index in range(k, k + self.k)]
                column_k = [self.board[(index, i)]
                            for index in range(k, k + self.k)]
                if all(val == player_this_turn for val in row_k) or all(val == player_this_turn for val in column_k):
                    # if all(val == player_this_turn for val in row_k):
                    #     print("row")
                    #     print(row_k)
                    # if all(val == player_this_turn for val in column_k):
                    #     print("column")
                    #     print(column_k)
                    won = True
        # y = -x direction
        for i in range(self.n - self.k, 0, -1):
            diag_lower = [self.board[(i + j, j)] for j in range(self.n - i)]
            diag_upper = [self.board[(j, i + j)] for j in range(self.n - i)]
            # Count entire diagonal
            if all(val == player_this_turn for val in diag_lower) or all(val == player_this_turn for val in diag_upper):
                won = True
                # if all(val == player_this_turn for val in diag_lower):
                #     print("entire lower diagnoal from y = -x")
                #     print(diag_lower)
                # if all(val == player_this_turn for val in diag_upper):
                #     print("entire upper diagnoal from y = -x")
                #     print(diag_upper)
            if len(diag_lower) > self.k:
                for i in range(len(diag_lower) - self.k + 1):
                    if all(diag_lower[j] == player_this_turn for j in range(i, self.k + i)):
                        won = True
                        # print("partial lower diagnoal from y = -x")
                        # print(diag_lower[i:self.k + i])
            if len(diag_upper) > self.k:
                for i in range(len(diag_upper) - self.k + 1):
                    if all(diag_upper[j] == player_this_turn for j in range(i, self.k + i)):
                        won = True
                        # print("partial upper diagnoal from y = -x")
                        # print(diag_upper[i:self.k + i])

        # y = x direction
        for i in range(self.n - self.k, 0, -1):
            diag_upper = [self.board[(self.n - i - 1 - j, j)]
                          for j in range(self.n - i)]
            diag_lower = [self.board[(self.n - j - 1, i + j)]
                          for j in range(self.n - i)]
            # Count entire diagonal
            if all(val == player_this_turn for val in diag_lower) or all(val == player_this_turn for val in diag_upper):
                won = True
                # if all(val == player_this_turn for val in diag_lower):
                #     print("entire lower diagnoal from y = x")
                #     print(diag_lower)
                # if all(val == player_this_turn for val in diag_upper):
                #     print("entire upper diagnoal from y = x")
                #     print(diag_upper)
            if len(diag_lower) > self.k:
                for i in range(len(diag_lower) - self.k + 1):
                    if all(diag_lower[j] == player_this_turn for j in range(i, self.k + i)):
                        won = True
                        # print("partial lower diagnoal from y = x")
                        # print(diag_lower[i:self.k + i])
            if len(diag_upper) > self.k:
                for i in range(len(diag_upper) - self.k + 1):
                    if all(diag_upper[j] == player_this_turn for j in range(i, self.k + i)):
                        won = True
                        # print("partial upper diagnoal from y = x")
                        # print(diag_upper[i:self.k + i])

        # y = -x direction
        diag1 = [self.board[(i, i)] for i in range(self.n)]
        if len(diag1) > self.k:
            for i in range(len(diag1) - self.k + 1):
                if all(diag1[j] == player_this_turn for j in range(i, self.k + i)):
                    won = True
                    # print("partial proper diag from y = -x")
                    # print(diag1[i:self.k + i])

        # y = x direction
        diag2 = [self.board[(self.n-1-i, i)] for i in range(self.n)]
        if len(diag2) > self.k:
            for i in range(len(diag2) - self.k + 1):
                if all(diag2[j] == player_this_turn for j in range(i, self.k + i)):
                    won = True
                    # print("partial proper diag from y = x")
                    # print(diag2[i:self.k + i])

        if all(val == player_this_turn for val in diag1) or all(val == player_this_turn for val in diag2):
            won = True
            # if all(val == player_this_turn for val in diag1):
            #     print(diag1)
            # if all(val == player_this_turn for val in diag2):
            #     print(diag2)
        return won

    def check_draw(self) -> bool:
        """
        Check whether the game is a draw. 

        Return
        ------
        Boolean of whether or not the game is a draw 
        """
        draw = True
        for i in range(self.n):
            for j in range(self.n):
                if self.board[(i, j)] == " ":
                    draw = False
        return draw

    def show_history(self) -> None:
        """Display all moves made throughout the game via print statements."""
        if self.game_over:
            print("\n")
            for i, board in enumerate(self.history):
                if i != 0:
                    print(f"On turn {i} the board looked like: \n")
                    self.display_board(board)
            player_this_turn = self.get_player_this_turn()
            game_length = str(len(self.history) - 1)
            if not self.check_draw():
                print(
                    "The game ended in " + game_length +
                    " turns, with " + player_this_turn + " being the winner.")
            else:
                print(
                    "The game ended in " + game_length +
                    " turns, with no winners.")
        else:
            print("You can only see the history after a game.")

    def game(self) -> None:
        """Start a game of TicTacToe."""
        print("\nTo place your mark, enter the position like the following: (int)row_number (int)column_number"
              "\nFor example, on a board of size 3, a valid input could look like '1 2'")
        current_move = None
        while not self.game_over:
            print("\n It's X's turn \n" if self.x_turn else "It's O's turn \n")
            player_this_turn = self.get_player_this_turn()
            if current_move == None:
                self.display_board(self.board)
            valid_input_type = False
            print("Where should " + player_this_turn + " go: ", end="")
            while not valid_input_type:
                try:
                    current_move = tuple(
                        map(int, input().split()))

                    while not (current_move in self.board and self.board[current_move] == " "):
                        current_move = tuple(
                            map(int, input("Please enter a valid input: ").split()))
                except ValueError:
                    print("Please enter a valid input: ", end="")
                else:
                    valid_input_type = True

            self.board[current_move] = player_this_turn
            self.history.append(self.board.copy())
            self.display_board(self.board)

            if self.check_win():
                self.game_over = True
                print(player_this_turn + " won!")
                # Change to the turn of the winner.
                self.x_turn = False if self.x_turn else True
            else:
                if self.check_draw():
                    self.game_over = True
                    print("It's a draw.")
            self.x_turn = False if self.x_turn else True

        if "yes" == input("The game has ended. "
                          "Enter 'yes' if you would like to view the history of the board, "
                          "enter anything else if otherwise: "):
            self.show_history()
