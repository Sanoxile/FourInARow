class PuckPlacement(object):

    def __init__(self, reds_turn, puck_x, board):
        self.reds_turn = reds_turn
        self.puck_x = puck_x
        self.puck_y = -1
        self.board = board
    
    def checkIfPlacementValid(self):
        valid = False
        try:
            self.puck_y = 0
            while True:
                if not (self.board[self.puck_x][self.puck_y] == "R") and not (self.board[self.puck_x][self.puck_y] == "Y"):
                    break
                self.puck_y += 1
            valid = True
        except:
            print("Invalid input. ", end="")
        return valid
        
    def placePuck(self):
        if self.reds_turn:
            self.board[self.puck_x][self.puck_y] = "R"
        else:
            self.board[self.puck_x][self.puck_y] = "Y"
        return self.puck_y