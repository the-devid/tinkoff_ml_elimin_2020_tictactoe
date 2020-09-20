import os
from time import sleep
import game
import analys

def player_move(titato):
    s = input('Input row\'s number first, then column\'s number second: ').split()
    while (not titato.check_input(s)):
        titato.print_game()
        s = input('Your last move was incorrect, make a new one. Input row\'s number first, then column\'s number second: ').split()
    x, y = map(int, s)
    return (x, y)

tttanalys = analys.GameAnalyzer()

def comp_move(titato):
    next_move = tttanalys.process(titato)
    next_move = next_move[1]
    for i in range(titato.n):
        for j in range(titato.n):
            if next_move.a[i][j] != titato.a[i][j]:
                return (i, j)

    return (-1, -1)

        
