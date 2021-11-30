from random import randint

ships_sunk = {"computer": 0, "player": 0}


class GameBoard:
    """
    Main board class.
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

