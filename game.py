import os
import copy

class tictactoe:
    a = []
    n, k = 3, 3
    player_sym = ['o', 'x']
    cur_player = 0
    rem_moves = 0

    def __init__(self, n=3, k=3):
        self.n, self.k = n, k
        self.a = [['.' for _ in range(n)] for _ in range(n)]
        self.rem_moves = n * n
    def __hash__(self):
        ans = 0
        for i in range(self.n):
            for j in range(self.n):
                ans = ans * 3 + (0 if self.a[i][j] == '.' else (1 if self.a[i][j] == 'o' else 2))
        return ans

    def check_win(self):
        for i in range(self.n):
            for j in range(self.n):
                if (self.a[i][j] == '.'):
                    continue
                flag_hor, flag_ver, flag_diag_right, flag_diag_left = True, True, True, True
                for x in range(self.k):
                    if (i + x >= self.n):
                        flag_ver = False
                        flag_diag_right = False
                        flag_diag_left = False
                    if (j + x >= self.n):
                        flag_hor = False
                        flag_diag_right = False
                    if (j - x < 0):
                        flag_diag_left = False
 
                    if (i + x < self.n):
                        flag_ver = flag_ver and (self.a[i + x][j] == self.a[i][j])
 
                    if (i + x < self.n and j + x < self.n):
                        flag_diag_right = flag_diag_right and (self.a[i + x][j + x] == self.a[i][j])
 
                    if (j + x < self.n):
                        flag_hor = flag_hor and (self.a[i][j + x] == self.a[i][j])
 
                    if (i + x < self.n and j - x >= 0):
                        flag_diag_left = flag_diag_left and (self.a[i + x][j - x] == self.a[i][j])
 
                    if (not flag_hor and not flag_ver and not flag_diag_right and not flag_diag_left):
                        break
                if (flag_hor or flag_ver or flag_diag_right or flag_diag_left):
                    return self.a[i][j]
        return '.'

    def is_state_win(self):
        return self.check_win() == self.player_sym[self.cur_player]
    def is_state_lose(self):
        return self.check_win() == self.player_sym[self.cur_player ^ 1]
    def is_state_draw(self):
        return not self.is_state_win() and not self.is_state_lose() and self.rem_moves == 0

    def print_game(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in self.a:
            for cell in row:
                print(cell, end='')
            print()

    def safe_print_game(self):
        print('safe:')
        for row in self.a:
            for cell in row:
                print(cell, end='')
            print()

    def check_input(self, s):
        if (len(s) != 2):
            return False
        if (not s[0].isdigit() or not s[1].isdigit()):
            return False
        x, y = map(int, s)
        if (x <= 0 or y <= 0 or x > self.n or y > self.n or self.a[x-1][y-1] != '.'):
            return False
        return True

    def make_move(self, x, y):
        self.a[x][y] = self.player_sym[self.cur_player]
        self.cur_player ^= 1
        self.rem_moves -= 1
        if (self.check_win() != '.'):
            return (True, self.check_win())
        if (self.rem_moves == 0):
            return (True, '.')
        return (False, '.')

    def generate_possible_moves(self):
        c = self.player_sym[self.cur_player]

        moves = []
 
        for i in range(self.n):
            for j in range(self.n):
                if self.a[i][j] == '.':
                    moves.append((c, i, j))
        states = []
        for move in moves:
            tadd = copy.deepcopy(self)
            tadd.a[move[1]][move[2]] = move[0]
            tadd.cur_player ^= 1
            tadd.rem_moves -= 1
            states.append(tadd)
        return states


