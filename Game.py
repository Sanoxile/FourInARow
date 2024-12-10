import Board
import UserInput
import PuckPlacement
import CheckFourInRow

class Game(object):

    def __init__(self):
        pass

    def startGame(self):
        self.reds_turn = True
        self.pucksPlaced = 0
        board_width = 7
        board_height = 5

        self.board = Board.Board(board_width, board_height)
        user_input = UserInput.UserInput()

        while True:
            self.board.printBoard()
            while True:
                puck_x = user_input.getUserInput(board_width)
                puck_placer = PuckPlacement.PuckPlacement(self.reds_turn, puck_x, self.board.board)
                placementValid = puck_placer.checkIfPlacementValid()
                if placementValid:
                    puck_y = puck_placer.placePuck()
                    break
            self.pucksPlaced += 1
            checker = CheckFourInRow.CheckFourInRow(self.reds_turn, puck_x, puck_y, board_width, board_height, self.board.board)
            amountInRow = checker.checkHorizontal()
            if amountInRow == 4:
                break
            amountInRow = checker.checkVertical()
            if amountInRow == 4:
                break
            amountInRow = checker.checkPosDiagonal()
            if amountInRow == 4:
                break
            amountInRow = checker.checkNegDiagonal()
            if amountInRow == 4:
                break
            self.reds_turn = not self.reds_turn
    
    def endGame(self):
        self.board.printBoard()
        if self.pucksPlaced == self.board.board_height * self.board.board_width:
            print("Its a draw ;-;")
        elif self.reds_turn:
            print("Red wins!!!")
        else:
            print("Yellow wins!!!")