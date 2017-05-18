#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randint


swap = False    # Does the player swap ot stick.
games = 1000    # Games to play. Higher number = better accuracy.
wins = 0        # Start with zero wins.

for i in range(games):
    prizeBox = randint(1, 3)    # Put the prize in a random box.
    playerBox = randint(1, 3)   # Player selects a box.
    emptyBox = randint(1, 3)    # Show an empty box that can't be the players.
    while emptyBox in [prizeBox, playerBox]:
        emptyBox = randint(1, 3)

    if swap:    # If the player is swapping find the other box ie. not players & not empty.
        for h in range(1,4):
            if h not in [playerBox, emptyBox]:
                playerBox = h
                break

    if playerBox == prizeBox:   # If the players box contains the prize add a win.
        wins += 1

print "{0} wins out of {1} games".format(wins, games)
