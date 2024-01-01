class Piece:
    # Class variable representing the maximum allowed power for any piece
    MAX_POWER = 14

    def __init__(self, team, power):
        # Instance variables to store the team and power of the piece
        self._team = team
        self._power = power

    @property
    def team(self):
        # Getter method for the 'team' attribute
        return self._team

    @team.setter
    def team(self, value):
        # Setter method for the 'team' attribute, checks if the provided value is valid
        if self.isValidTeam(value):
            self._team = value
        else:
            raise ValueError("Invalid team. Must be 'RED' or 'BLUE'.")

    @property
    def power(self):
        # Getter method for the 'power' attribute
        return self._power

    @power.setter
    def power(self, value):
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
        return f"Team: {self.team}, Power: {self.power}"



class Board:
    # Class variables representing the default number of rows and columns on the board
    rows = 8
    columns = 8

    def __init__(self):
        # Instance variable to store the state matrix of the board
        self.state = None
        # Initialize the state matrix with zeros
        self.createState()

    def createState(self):
        # Initialize the state matrix with zeros for each cell (row x column)
        self.state = [[0] * self.columns for _ in range(self.rows)]

    def printState(self):
        # Print the matrix with row labels
        for i, row in enumerate(self.state):
            # Convert row index to letter ('A' for 0, 'B' for 1, etc.)
            row_label = chr(ord('A') + i)
            # Print the row label and the elements of the row separated by space
            print(f"{row_label} {' '.join(map(str, row))}")

        # Print column numbers aligned with columns
        column_numbers = list(map(str, range(1, self.columns + 1)))
        column_labels = " ".join(column_numbers)
        # Print column numbers with a space at the beginning for alignment
        print("  " + column_labels)

    def __str__(self):
        # String representation of the Board object, including the number of rows, columns, and the board state
        return f"Board: {self.rows} rows, {self.columns} columns\nState:\n{self.printState()}"

# Example usage:
if __name__ == "__main__":
    # Creating an instance of the Board class
    game_board = Board()

    # Printing the state of the board
    print("Board State:")
    game_board.printState()

