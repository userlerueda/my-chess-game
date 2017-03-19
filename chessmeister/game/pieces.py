#!/usr/bin/env python


class King():
    def __init__(self, position):
        """Create a King object."""
        self.position = position

    def move(self, new_position):
        """Move King to desired position."""
        self.position = new_position

    def __str__(self):
        """Return details for King."""
        return ("Player: {}, Position {}".format(self.player, self.position))


class Queen():
    def __init__(self):
        self.algo = 0


class Rook():
    def __init__(self):
        self.algo = 0


class Bishop():
    def __init__(self):
        self.algo = 0


class Pawn():
    def __init__(self):
        self.algo = 0


def main():
    black_king = King("black")
    white_king = King("white")
    print(black_king)
    black_king.move("e1")
    print(black_king)


if __name__ == '__main__':
    main()
