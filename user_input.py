class UserInput:

    def __init__(self) -> None:
        pass

    def getUserInput(self, board_width):
        try:
            user_input = int(input((f"Enter to drop a puck in column 1-{board_width}: ")))
        except:
            user_input = -1
        while user_input <= 0 or user_input > board_width:
            try:
                user_input = int(input(f"Invalid input. Enter to drop a puck in column 1-{board_width}: "))
            except:
                pass
        return user_input - 1

