import random

class AI(object):

    def __init__(self, board):
        self.board = board
        self.board_width = len(self.board)
        self.board_height = len(self.board[0])
        self.interpretedBoard = self.interpretData()
        self.player_puck_x = -1
        self.player_puck_y = -1
        self.AIScore = [0 for i in range(self.board_width)]
        self.r = random.randint()

    def updateBoard(self, board, player_puck_x, player_puck_y):
        self.board = board
        self.interpretedBoard = self.interpretData()
        self.player_puck_x = player_puck_x
        self.player_puck_y = player_puck_y
        self.AIScore = [0 for i in range(self.board_width)]

    def interpetData(self):
        new_board = [[[0 for i in range(self.board_height)] for j in range(self.board_width)]]
        for i in range(self.board_height):
            for j in range(self.board_width):
                if(self.board[i][j] == " "):
                    new_board[i][j] == 0
                elif(self.board[i][j] == "R"):
                    new_board[i][j] == 1
                else:
                    new_board[i][j] = 2
    
    def placeAtTop(self):
        for i in range(self.board_height + 1):


    def checkIfPlaceable(self):
        for i in range(self.board_width):
            try:


    def getAttackScore(self):
        for()