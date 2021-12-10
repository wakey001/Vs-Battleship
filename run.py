from random import randint

scores = {"computer": 0, "player": 0}


class GameBoard:
    """
    Main board class. Sets board size, the number of ships.
    The player's name and the board type (player or computer)
    Has methods for adding ships, and guesses, and printing board. 
    """ 
    def __init__(self, size, num_of_ships, name, type):
        self.size = size
        self.num_of_ships = num_of_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []
        self.board = [["." for x in range(size)] for y in range(size)]
            
    def print(self):
        for row in self.board:
            print(" ".join(row))
    
    def guess(self, x, y):
        self.guesses.append((x, y))
        self.board[x][y] = "X"

        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return "Hit"
        else:
            return "Miss"
    
    def add_ship(self, x, y, type="computer"):
        if len(self.ships) >= self.num_of_ships:
            print("Error: You cannot add anymore ships!")
        else:
            self.ships.append((x, y))
            if self.type == "player":
                self.board[x][y] = "@"
    

def random_point(size):
    """
    Helper function to return a randominteger between 0 and size
    """
    return randint(0, size-1)


def valid_coordinates(x, y, board):
    pass


def polpulate_board(board):
    pass


def make_guess(board):
    pass


def play_game(computer_board, player_board):
    pass


def new_game():
    """
    starts a new game. Sets the board size and number of ships, resets the
    scores and initialises the boards.
    """

    size = 5
    num_of_ships = 4
    scores["computer"] = 0
    scores["player"] = 0
    print("-" * 35)
    print(" Welcome to VS BATTLESHIP!")
    print(f" Board Size: {size}. numof ships: {num_ships}")
    print(" Top left corner is row: 0, col: 0")
    print("-" * 35)
    player_name = input("Please enter your name \n")
    print("-" * 35)

    computer_board = Board(size, num_of_ships, "Computer", type="computer")
    player_board = Board(size, num_of_ships, player_name, type="player")

    for _ in range(num_ships):
        polpulate_board(player_board)
        polpulate_board(computer_board)
    
    play_game(computer_board, player_board)


new_game()
