class Piece:
    MAX_POWER = 14

    def __init__(self, team, power):
        self._team = team
        self._power = power

    @property
    def team(self):
        return self._team

    @team.setter
    def team(self, value):
        if self.isValidTeam(value):
            self._team = value
        else:
            raise ValueError("Invalid team. Must be 'RED' or 'BLUE'.")

    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, value):
        if self.isValidPower(value):
            self._power = value
        else:
            raise ValueError(f"Invalid power. Must be between 0 and {self.MAX_POWER}.")

    def isValidTeam(self, team):
        return team.upper() in ["RED", "BLUE"]

    def isValidPower(self, power):
        return 0 <= power <= self.MAX_POWER

    def __str__(self):
        return f"Team: {self.team}, Power: {self.power}"


class Board:
    rows = 8
    columns = 8

    def __init__(self):
        self.state = None
        self.createState()

    def createState(self):
        # Initialize the state matrix with zeros
        self.state = [[0] * self.columns for _ in range(self.rows)]

    def printState(self):
        # Print the matrix with row labels
        for i, row in enumerate(self.state):
            row_label = chr(ord('A') + i)  # Convert row index to letter ('A' for 0, 'B' for 1, etc.)
            print(f"{row_label} {' '.join(map(str, row))}")

        # Print column numbers aligned with columns
        column_numbers = list(map(str, range(1, self.columns + 1)))
        column_labels = " ".join(column_numbers)
        print("  " + column_labels)

    def __str__(self):
        return f"Board: {self.rows} rows, {self.columns} columns\nState:\n{self.printState()}"

# Example usage:
if __name__ == "__main__":
    # Creating an instance of the Board class
    game_board = Board()

    # Printing the state of the board
    print("Board State:")
    game_board.printState()


