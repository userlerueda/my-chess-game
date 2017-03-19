#!/usr/bin/env python

"""
Chessmeister is a chess developed as a hobby to use python code.

Game developed by Luis Rueda <userlerueda@gmail.com>
"""

import game.player as player
import game.board as board


def draw_game(player1, player2, game_board):
    """Draw the game on the screen."""
    print("Current Game")
    print(game_board)


def main():
    """Main program."""
    # ask human color
    game_board = board.Board()
    human_color = "white"
    computer_color = "black"
    human = player.Player("human", human_color)
    computer = player.Player("computer", computer_color)
    winner = False
    while not winner:
        draw_game(human, computer, game_board)
        move = raw_input("Please input your move: ")
        game_board.set_element(move, "HOR")

    # initialize_player("computer", human_color)
    # player["color"] = "white"
    # if player["color"] == "white":
    #     computer["color"] = "black"
    # else:
    #     computer["color"] = "white"
    # player["pieces"] = {}
    # for piece in player["pieces"]:
    #     player["pieces"][piece] = pieces.King(player)
    # computer["pieces"]["king"] =
    # computer_king = pieces.King(computer)


if __name__ == "__main__":
    main()
