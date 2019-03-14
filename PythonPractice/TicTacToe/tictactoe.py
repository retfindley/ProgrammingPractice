class SpaceTakenError(Exception):
    pass

class BoardTooSmallError(Exception):
    pass

class TicTacToe:

    def __init__(self):
        self.board = []
        self.initialize_board()
        self.playerO = 'O'
        self.playerX = 'X'
        self.player = self.playerX

    def initialize_board(self):
        """
        Creates an empty board to be played on
        """
        # get board size from user
        good_input = False
        size = None
        while not good_input:
            try:
                size = int(raw_input("What size board to do you want to play on?\n"))
                if size < 3:
                    raise BoardTooSmallError
            except BoardTooSmallError:
                print "Your board must be at least a 3x3 to play."
            except ValueError:
                print "Your board size must be an integer."
            else:
                good_input = True
        # initialize board to empty strings
        self.board = [[None for row in range(0, size)] for col in range(0, size)]
        self.size = len(self.board)
        self.num_turns = size*size
        self.draw_board()

    def draw_board(self):
        """
        Draws current state of the board
        """
        for row in self.board:
            print "---" * self.size
            for col in row:
                if col:
                    print "|%s" % col,
                else:
                    print "| ",
            print "|"
        print "---" * self.size

    def play(self):
        """
        If there are turns left, allows a play
        Makes sure the user input for row and column is valid (positive integer, untake space, in bounds)
        Sets the space according to the player's turn
        Switches player before exiting
        Output:
            True if there are remaining turns
            False if there are no remaining turns
        """
        if self.num_turns > 0:
            good_input = False
            row = None
            col = None
            # communicate who should play next
            print "-----------------------------"
            print "PLAYER %s's turn" % self.player
            # get validated user input
            while not good_input:
                try:
                    row = int(raw_input("What row?\n"))-1
                    col = int(raw_input("What column?\n"))-1
                    if row < 0 or col < 0:
                        raise ValueError
                    if self.board[row][col]:
                        raise SpaceTakenError
                    if row > self.size or col > self.size:
                        raise IndexError
                except ValueError:
                    print "Make sure the row and column are positive integers."
                except SpaceTakenError:
                    print "That space is already taken. Try again."
                except IndexError:
                    print "That space is out of bounds. Try again."
                else:
                    good_input = True
            # set space with user's value (X or O) depending on whose turn it is
            # update next player
            if self.player == self.playerX:
                self.board[row][col] = self.playerX
                self.player = self.playerO
            else:
                self.board[row][col] = self.playerO
                self.player = self.playerX
            self.num_turns -= 1
            return True
        else:
            return False

    def check_winner(self):
        """
        Checks winning conditions:
            -win along a diagonal (left to right or right to left)
            -win along row
            -win along column
        Returns:
            -winning letter
        """
        winner = None
        # check top left corner to bottom right corner diagonal win
        for i in range(self.size):
            first_element_in_left_diag = self.board[0][0]
            if not first_element_in_left_diag or self.board[i][i] != first_element_in_left_diag:
                break
        else:
            return first_element_in_left_diag
        # check top right corner to bottom left corner diagonal win
        for i in range(self.size):
            first_element_in_right_diag = self.board[0][self.size-1]
            if not first_element_in_right_diag or self.board[i][self.size-1-i] != first_element_in_right_diag:
                break
        else:
            return first_element_in_right_diag
        # check row and column wins
        for i in range(self.size):
            first_element_in_row = self.board[i][0]
            first_element_in_col = self.board[0][i]
            # rows
            for j in range(1, self.size):
                if not first_element_in_row or self.board[i][j] != first_element_in_row:
                    break
            else:
                return first_element_in_row
            # cols
            for j in range(1, self.size):
                if not first_element_in_row or self.board[j][i] != first_element_in_col:
                    break
            else:
                return first_element_in_col
        return None

if __name__ == "__main__":
    T = TicTacToe()
    winner = False
    while not winner and T.play():
        T.draw_board()
        winner = T.check_winner()
        if winner:
            print "The winner is player %s!" % winner
    else:
        if not winner:
            print "Game was a tie."
