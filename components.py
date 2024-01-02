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
    columns = 9

    def __init__(self):
        # Instance variable to store the state matrix of the board
        self.state = None
        # Initialize the state matrix with zeros
        self.createState()

    def createState(self):
        # Initialize the state matrix with zeros for each cell (row x column)
        self.state = [[0] * self.columns for _ in range(self.rows)]

    def printState(self):
        # Print the matrix with row numbers
        for i, row in enumerate(self.state):
            # Print row number
            print(f"{i + 1}", end=" ")
            
            # Check if it is the first or last row
            if i == 0 or i == self.rows - 1:
                # Print the elements of the row without a newline at the end
                print(" ".join(map(str, row)), end="")
            else:
                # Print the elements of the row with a newline at the end
                print(" ".join(map(str, row)))

            # Print "BLUE" after the first row
            if i == 0:
                print("  BLUE")

        # Print "RED" after the last row
        print("  RED")

        # Print column letters aligned with columns
        column_letters = [chr(ord('A') + i) for i in range(self.columns)]
        column_labels = " ".join(column_letters)
        print("  " + column_labels)

    def __str__(self):
        return f"Board: {self.rows} rows, {self.columns} columns\nState:\n{self.printState()}"

# Example usage:
if __name__ == "__main__":
    game_board = Board()
    print("Board State:")
    game_board.printState()

