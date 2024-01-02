class Piece:
    # Class variable representing the maximum allowed power for any piece
    MAX_POWER = 14

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
    rows = 8
    columns = 9

    def __init__(self):
        # Instance variable to store the state matrix of the board
        self.state = None
        # Initialize the state matrix with zeros
        self.createState()

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

    def printState(self):
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
        print("   " + column_labels)

    def __str__(self):
        return f"Board: {self.rows} rows, {self.columns} columns\nState:\n{self.printState()}"

# Example usage:
if __name__ == "__main__":
    game_board = Board()
    print("Board State:")
    game_board.blueFormation([-1, 1, 2, -1, -1, 3, -1, 4, 5, 6])
    game_board.redFormation([-1, 1, 2, -1, -1, 3, -1, 4, 5, 6])
    game_board.printState()

