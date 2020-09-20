import os
import argparse
import game
import moves

parser = argparse.ArgumentParser()
parser.add_argument('-n', action='store', dest='n', default=3, type=int)
parser.add_argument('-k', action='store', dest='k', default=3, type=int)
parser.add_argument('-mode', action='store', dest='gamemode', default='player') #player or playervscomp or compvsplayer or comp

args = parser.parse_args()

n, k, gamemode = args.n, args.k, args.gamemode

if (k > n) or (gamemode not in ['player', 'playervscomp', 'compvsplayer', 'comp']):
    print('It is impossible to play a game')
    exit(0)

titato = game.tictactoe(n, k)

state_of_wining = (False, '.')

while True:
    titato.print_game()
    x, y = 0, 0
    if (titato.cur_player == 0):
        if (gamemode == 'player' or gamemode == 'playervscomp'):
            x, y = moves.player_move(titato)
            x -= 1
            y -= 1
        else:
            x, y = moves.comp_move(titato)
    else:
        if (gamemode == 'player' or gamemode == 'compvsplayer'):
            x, y = moves.player_move(titato)
            x -= 1
            y -= 1
        else:
            x, y = moves.comp_move(titato)

    state_of_wining = titato.make_move(x, y)
    titato.print_game()
    if (state_of_wining[0]):
        break

if (state_of_wining[1] != '.'):
    print("Congartulations to the", state_of_wining[1], "player, he won!")
else:
    print("It seems like nobody won. Good game!")


