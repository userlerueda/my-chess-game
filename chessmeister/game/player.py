#!/usr/bin/env python

import pieces


class Player():
    def __init__(self, player_type, color):
        """Player class."""
        self.color = color
        self.player_type = player_type
        self.king = pieces.King("d5")

    def __str__(self):
        return ("Player Type: {}, Color: {}"
                .format(self.player_type, self.color))
