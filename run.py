import random

ships_sunk = {"computer": 0, "player":0}

name = input("What is your name ")
print("Welcome to Battleship " + name + "!")
input("Start Game Y/N ")

class GameBoard():
    """
    Main board class.
    """   
    def __init__(self, board):
        self.board = board


    def get_letters_to_numbers():
        letters_to_numbers = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7}
        return letters_to_numbers
    

    def print_board(self):
        print(" A B C D E F G H")
        print(" ---------------")
        row_number = 1
        for row in self.board:
            print("||||||" )
            row_number += 1




def shoot():
    pass


def hit_or_miss():
    pass


def player_ship_sunk():
    pass


def computer_ship_sunk():
    pass


def gameover():
    pass
