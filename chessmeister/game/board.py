import pprint

def letter_to_number(letter):
    if letter == "a" or letter == "A":
        return 1
    if letter == "b" or letter == "B":
        return 2
    if letter == "c" or letter == "C":
        return 3
    if letter == "d" or letter == "D":
        return 4
    if letter == "e" or letter == "E":
        return 5
    if letter == "f" or letter == "F":
        return 6
    if letter == "g" or letter == "G":
        return 7
    if letter == "h" or letter == "H":
        return 8


def valid_position(position):
    if len(position) != 2:
        print("Position is in the form of e1 or D4")
        return False
    column = letter_to_number(position[0])
    if column < 1 or column > 8:
        print("Invalid Letter must be [a-z][A-Z]")
        return False
    row = int(position[1])
    if row < 1 or row > 8:
        print("Invalid Number must be [1-8]")
        return False
    return True


class Board():
    def __init__(self):
        self.board = [["", "", "", "", "", "", "", ""],
                      ["", "", "", "", "", "", "", ""],
                      ["", "", "", "", "", "", "", ""],
                      ["", "", "", "", "", "", "", ""],
                      ["", "", "", "", "", "", "", ""],
                      ["", "", "", "", "", "", "", ""],
                      ["", "", "", "", "", "", "", ""],
                      ["", "", "", "", "", "", "", ""]]

    def get_element(self, position):
        if valid_position(position):
            column = letter_to_number(position[0]) - 1
            row = int(position[1]) - 1
            return self.board[column][row]

    def set_element(self, position, ficha):
        if valid_position(position):
            column = letter_to_number(position[0]) - 1
            row = int(position[1]) - 1
            self.board[column][row] = ficha

    def __str__(self):
        nice_board = pprint.pformat(self.board)
        return nice_board
