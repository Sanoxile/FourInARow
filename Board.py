
class Board(object):    # Creates a class that represents the board

    def __init__(self, board_width, board_heght):   # Initializes the board with values
        self.board_width = board_width
        self.board_height = board_heght
        self.board = [[" " for i in range(board_heght)] for j in range(board_width)]    # Creates a 2D array that represents the board
    
    def setRedPuck(self, width, height):    # Sets a specific spot on the board to a red puck
        self.board[width][height] = "R"

    def setYellowPuck(self, width, height): # Sets a specific spot on the board to a yellow puck
        self.board[width][height] = "Y"
    
    def printBoard(self):   # Prints and displays the connect four board
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n") # Makes sure that the game ends up at the bottom of the screen
        print("CONNECT FOUR")   # Prints the title of the game
        for i in range(self.board_height - 1, -1, -1):  # "i" represents the height of the board
            print("-" * 4 * self.board_width + "-") # Prints a divider between rows for the board
            for j in range(self.board_width):   # "j" represents width
                print("| " + self.board[j][i], end=" ") # Prints a divider with two spaces as well as a character
            print("|")  # Prints a final divider at the end of the columns
        print("-" * 4 * self.board_width + "-") # Prints a final divider at the end of the rows
