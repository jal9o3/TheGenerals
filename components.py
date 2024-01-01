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
    rows = 8
    columns = 8

    def __init__(self):
        self.state = None
        self.createState()

    def createState(self):
        self.state = [[0] * self.columns for _ in range(self.rows)]

    def printState(self):
        # Print the matrix with row numbers
        for i, row in enumerate(self.state):
            # Print row number
            print(f"{i + 1}", end=" ")
            # Print the elements of the row separated by space
            print(" ".join(map(str, row)))
        
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

