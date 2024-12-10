class CheckFourInRow(object):

    def __init__(self, reds_turn, puck_x, puck_y, board_width, board_height, board):
        self.reds_turn = reds_turn
        self.puck_x = puck_x
        self.puck_y = puck_y
        self.board_width = board_width
        self.board_height = board_height
        self.board = board

    def checkHorizontal(self):  # Checks for four in a row horizontally
        amountInARow = 1
        for i in range(self.puck_x - 1 , self.puck_x - 4, -1): # Check from the left
            if i < 0:
                break
            if self.board[i][self.puck_y] == "R" and self.reds_turn:
                amountInARow += 1
            elif self.board[i][self.puck_y] == "Y" and not self.reds_turn:
                amountInARow += 1
            else:
                break

        for i in range(self.puck_x + 1, self.puck_x + 4, 1): # Check from the right
            if i >= self.board_width or amountInARow == 4:
                break
            if self.board[i][self.puck_y] == "R" and self.reds_turn:
                amountInARow += 1
            elif self.board[i][self.puck_y] == "Y" and not self.reds_turn:
                amountInARow += 1
            else:
                break
        return amountInARow


    def checkVertical(self):
        amountInARow = 1
        for i in range(self.puck_y - 1, self.puck_y - 4, -1):   # Check below 
            if i < 0:
                break
            if self.board[self.puck_x][i] == "R" and self.reds_turn:
                amountInARow += 1
            elif self.board[self.puck_x][i] == "Y" and not self.reds_turn:
                amountInARow += 1
            else:
                break
        return amountInARow
    
    def checkPosDiagonal(self):
        amountInARow = 1
        for delta in range(-1, -4, -1):
            xCoord = self.puck_x + delta
            yCoord = self.puck_y + delta
            if xCoord < 0 or yCoord < 0:
                break
            if self.board[xCoord][yCoord] == "R" and self.reds_turn:
                amountInARow += 1
            elif self.board[xCoord][yCoord] == "Y" and not self.reds_turn:
                amountInARow += 1
            else:
                break

        for delta in range(1, 4, 1):
            xCoord = self.puck_x + delta
            yCoord = self.puck_y + delta
            if xCoord >= self.board_width or yCoord >= self.board_height or amountInARow == 4:
                break
            if self.board[xCoord][yCoord] == "R" and self.reds_turn:
                amountInARow += 1
            elif self.board[xCoord][yCoord] == "Y" and not self.reds_turn:
                amountInARow += 1
            else:
                break
        return amountInARow
    
    def checkNegDiagonal(self):
        amountInARow = 1
        for delta in range(1, 4, 1):
            xCoord = self.puck_x - delta
            yCoord = self.puck_y + delta
            if xCoord < 0 or yCoord >= self.board_height:
                break
            if self.board[xCoord][yCoord] == "R" and self.reds_turn:
                amountInARow += 1
            elif self.board[xCoord][yCoord] == "Y" and not self.reds_turn:
                amountInARow += 1
            else:
                break

        for delta in range(1, 4, 1):
            xCoord = self.puck_x + delta
            yCoord = self.puck_y - delta
            if xCoord >= self.board_width or yCoord < 0 or amountInARow == 4:
                break
            if self.board[xCoord][yCoord] == "R" and self.reds_turn:
                amountInARow += 1
            elif self.board[xCoord][yCoord] == "Y" and not self.reds_turn:
                amountInARow += 1
            else:
                break
        return amountInARow