class Piece:
    # Class variable representing the maximum allowed power for any piece
    MAX_POWER = 5

    def __init__(self):
        # Instance variables to store the team and power of the piece
        self._team = ''
        self._power = -2

    def get_team(self):
        # Getter method for the 'team' attribute
        return self._team

    def set_team(self, value):
        # Setter method for the 'team' attribute, checks if the provided value is valid
        if self.isValidTeam(value):
            self._team = value.upper()
        else:
            raise ValueError("Invalid team. Must be 'RED' or 'BLUE'.")

    def get_power(self):
        # Getter method for the 'power' attribute
        return self._power

    def set_power(self, value):
        # Setter method for the 'power' attribute, checks if the provided value is within valid range
        if self.isValidPower(value):
            self._power = value
        else:
            raise ValueError(f"Invalid power. Must be between 0 and {self.MAX_POWER}.")

    def isValidTeam(self, team):
        # Checks if the provided team is valid (either 'RED' or 'BLUE')
        return team.upper() in ["RED", "BLUE"]

    def isValidPower(self, power):
        # Checks if the provided power is within the valid range (0 to MAX_POWER)
        return 0 <= power <= self.MAX_POWER

    def __str__(self):
        # String representation of the Piece object
        return f"{self.get_team()[0]}{self.get_power()}"


class Board:
    # Class variables representing the default number of rows and columns on the board
    rows = 5
    columns = 5

    def __init__(self):
        # Instance variable to store the state matrix of the board
        self.state = None
        # Initialize the state matrix with zeros
        self.createState()
        # Initialize the turn attribute to an empty string
        self.turn = ''
        # Initialize the graveyards of both teams
        self.blueGraveyard = []
        self.redGraveyard = []
        # Initialize the terminal attribute, which will store the result of the game
        self.terminal = "ONGOING"

    def createState(self):
        # Initialize the state matrix with zeros for each cell (row x column)
        self.state = [[0] * self.columns for _ in range(self.rows)]

    def blueFormation(self, formation):
        row = 0
        col = 0

        for power in formation:
            if power != -1:
                # Instantiate a new Piece object with 'blue' team and the given power
                piece = Piece()
                piece.set_team('BLUE')
                piece.set_power(power)
                # Assign the piece to the current spot in the matrix
                self.state[row][col] = piece

            # Move to the next spot in the matrix
            col += 1
            if col == self.columns:
                col = 0
                row += 1

    def redFormation(self, formation):
        row = self.rows - 1
        col = self.columns - 1

        for power in formation:
            if power != -1:
                # Instantiate a new Piece object with 'red' team and the given power
                piece = Piece()
                piece.set_team('RED')
                piece.set_power(power)
                # Assign the piece to the current spot in the matrix
                self.state[row][col] = piece

            # Move to the next spot in the matrix
            col -= 1
            if col < 0:
                col = self.columns - 1
                row -= 1
    
    def set_turn(self, turn):
        # Setter method for the 'turn' attribute, checks if the provided value is valid
        if self.isValidTurn(turn):
            self.turn = turn.upper()
        else:
            raise ValueError("Invalid turn. Must be 'BLUE' or 'RED'.")

    def get_turn(self):
        # Getter method for the 'turn' attribute
        return self.turn

    def isValidTurn(self, turn):
        # Checks if the provided turn is valid (either 'BLUE' or 'RED')
        return turn.upper() in ["BLUE", "RED"]

    def move(self, start, destination):
        # Validate the format of start and destination
        if not self.isValidPosition(start) or not self.isValidPosition(destination):
            raise ValueError("Invalid position format. Use the format <letter><digit>.")

        # Check if game has ended
        if self.terminal != "ONGOING":
            return

        # Convert the letter part of the position to column index
        start_col = ord(start[0]) - ord('A')
        destination_col = ord(destination[0]) - ord('A')

        # Convert the digit part of the position to row index
        start_row = int(start[1]) - 1
        destination_row = int(destination[1]) - 1

        self.check_move(start_row, start_col, destination_row, destination_col)

        if isinstance(self.state[start_row][start_col], Piece) and isinstance(self.state[destination_row][destination_col], Piece):
            if self.state[start_row][start_col].get_team() != self.state[destination_row][destination_col].get_team():
                # Check the power attributes and handle the challenge
                self.handle_challenge(start_row, start_col, destination_row, destination_col)
        else:
             # Perform the move by updating the state matrix
            self.state[destination_row][destination_col] = self.state[start_row][start_col]
            self.state[start_row][start_col] = 0  # Clear the starting position

        self.set_terminal()

        # Switch the turn to the other team
        self.switch_turn()

    def handle_challenge(self, start_row, start_col, destination_row, destination_col):
        # Check the power attributes of the pieces
        start_power = self.state[start_row][start_col].get_power()
        destination_power = self.state[destination_row][destination_col].get_power()

        if (start_power > destination_power) or (start_power == 1 and destination_power == Piece.MAX_POWER) \
            or (start_power == 0 and destination_power == 0):
            # Remove the piece in the destination square, placing it in the graveyard
            self.remove(destination_row, destination_col)
            # Move the piece in the starting square to the destination square
            self.state[destination_row][destination_col] = self.state[start_row][start_col]
            self.state[start_row][start_col] = 0  # Clear the starting position
        elif (start_power < destination_power) or (start_power == Piece.MAX_POWER and destination_power == 1):
            # Remove the piece in the starting square from the board
            self.remove(start_row, start_col)
        else:
            # Remove both pieces from the board in case of a tie
            self.remove(start_row, start_col)
            self.remove(destination_row, destination_col)

    def remove(self, row, col):
        # Add piece to the team's graveyard
        if self.state[row][col].get_team() == "BLUE":
            self.blueGraveyard.append(self.state[row][col].get_power())
        else:
            self.redGraveyard.append(self.state[row][col].get_power())
        # Remove the piece at the specified position from the board
        self.state[row][col] = 0

    def check_move(self, start_row, start_col, destination_row, destination_col):
        # Validate that the indices are within the board dimensions
        if not (0 <= start_row < self.rows) or not (0 <= start_col < self.columns) or \
           not (0 <= destination_row < self.rows) or not (0 <= destination_col < self.columns):
            raise ValueError("Invalid position. Position out of bounds.")

        # Validate that there is a piece at the starting position
        if not isinstance(self.state[start_row][start_col], Piece):
            raise ValueError("No piece at the starting position.")

        # Validate that the piece at the starting position belongs to the current turn
        if self.state[start_row][start_col].get_team() != self.get_turn():
            raise ValueError("Invalid move. The piece at the starting position does not belong to the current turn.")

        # Validate that the destination does not contain a piece from the same team
        if isinstance(self.state[destination_row][destination_col], Piece) and \
           self.state[destination_row][destination_col].get_team() == self.get_turn():
            raise ValueError("Invalid move. The destination contains a piece from the same team.")

        # Check if the move is one square forward, backward, left, or right
        if abs(destination_row - start_row) + abs(destination_col - start_col) != 1:
            raise ValueError("Invalid move. Only one square forward, backward, left, or right moves are allowed.")

    def set_terminal(self):
        # Check if 0 is found in blueGraveyard
        if 0 in self.blueGraveyard:
            self.terminal = "RED WIN"
        # Check if 0 is found in redGraveyard
        elif 0 in self.redGraveyard:
            self.terminal = "BLUE WIN"

    def isValidPosition(self, position):
        # Checks if the provided position has the correct format "<letter><digit>"
        if len(position) == 2 and position[0].isalpha() and position[1].isdigit():
            return True
        return False

    def switch_turn(self):
        # Switch the turn to the other team
        self.turn = 'RED' if self.turn == 'BLUE' else 'BLUE'

    def printState(self):
        # Print the graveyards of both teams
        print("Blue Graveyard: " + " ".join(map(str, self.blueGraveyard)))
        print("Red Graveyard: " + " ".join(map(str, self.redGraveyard)))
        print() # Newline for readability

        # Print the matrix with row numbers
        for i, row in enumerate(self.state):
            # Print row number
            print(f"{i + 1:2}", end=" ")

            # Check if it is the first or last row
            if i == 0 or i == self.rows - 1:
                # Print the elements of the row without a newline at the end
                print(" ".join(f"{element.__str__():3}" for element in row), end="")
            else:
                # Print the elements of the row with a newline at the end
                print(" ".join(f"{element.__str__():3}" for element in row))

            # Print "BLUE" after the first row
            if i == 0:
                print("  BLUE")

        # Print "RED" after the last row
        print("  RED")

        # Print column letters aligned with columns
        column_letters = [f"{chr(ord('A') + i):3}" for i in range(self.columns)]
        column_labels = " ".join(column_letters)
        print("   " + column_labels + "\n")

        print(f"{self.turn}" + "'s turn\n")

    def __str__(self):
        return f"Board: {self.rows} rows, {self.columns} columns\nTurn: {self.turn}\nState:\n{self.printState()}"

# Example usage:
if __name__ == "__main__":
    game_board = Board()

    game_board.blueFormation([3, 0, 4, 5, -1, -1, 2, 1, 1, -1])
    game_board.redFormation([5, 1, -1, -1, 0, 3, 1, -1, 4, 2])
    game_board.set_turn('BLUE')
    game_board.printState()
    
    # game_board.move('D2', 'C2') # attempt to challenge allied piece
    # game_board.move('C2', 'B3') # attempt to move diagonally
    game_board.move('D2', 'E2')
    game_board.printState()
    game_board.move('E4', 'E3')
    game_board.printState()
    game_board.move('E2', 'E3')
    game_board.printState()
    game_board.move('D4', 'D3')
    game_board.printState()
    game_board.move('C2', 'D2')
    game_board.printState()
    game_board.move('D3', 'D2')
    game_board.printState()
    game_board.move('D1', 'D2')
    game_board.printState()
    game_board.move('D5', 'D4')
    game_board.printState()
    game_board.move('D2', 'D3')
    game_board.printState()
    game_board.move('D4', 'D3')
    game_board.printState()
    game_board.move('C1', 'C2')
    game_board.printState()
    game_board.move('D3', 'D2')
    game_board.printState()
    game_board.move('C2', 'D2')
    game_board.printState()
    game_board.move('E3', 'D3')
    game_board.printState()
    game_board.move('D2', 'D3')
    game_board.printState()
    game_board.move('A4', 'A3')
    game_board.printState()
    game_board.move('A1', 'A2')
    game_board.printState()
    game_board.move('A3', 'A2')
    game_board.printState()
    game_board.move('A2', 'A3')
    game_board.printState()
    game_board.move('A5', 'A4')
    game_board.printState()

    # game_board.move('A3', 'A4') # capture red's flag
    # game_board.printState()

    # game_board.move('B4', 'C4') # attempt to move after end of game
    # game_board.printState()

    game_board.move('B2', 'C2')
    game_board.printState()
    game_board.move('B4', 'B3')
    game_board.printState()
    game_board.move('B1', 'B2')
    game_board.printState()
    # game_board.move('B3', 'B2') # capture blue's flag
    # game_board.printState()

    # game_board.move('C2', 'B2') # attempt to move after end of game
    # game_board.printState()