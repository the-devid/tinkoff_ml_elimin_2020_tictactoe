import random
import copy
import time

LOSE = 0
WIN = 1
DRAW = 2
UNKNOWN = 3

class GameAnalyzer:
    
    MAX_TIME = 10.0
    REC_COUNT = 5
    start_time = 0

    is_win = {}
    next_move = {}
    visited = set()

    def __init__(self, custom_rec_count=REC_COUNT):
        self.REC_COUNT = custom_rec_count
    rem_count = 0
    
    def proc(self, state):   #  SSYLKI I CONSTANTY IZOBRELI ESCHE V C++ POCHEMU IH NET V PITONE
        if state in self.is_win and self.is_win[state] != UNKNOWN:
            return (self.is_win[state], self.next_move[state])
        if state.is_state_win():
            self.is_win[state] = WIN
            self.next_move[state] = None
            return (self.is_win[state], self.next_move[state])
        if state.is_state_lose():
            self.is_win[state] = LOSE
            self.next_move[state] = None
            return (self.is_win[state], self.next_move[state])
        if state.is_state_draw():
            self.is_win[state] = DRAW
            self.next_move[state] = None
            return (self.is_win[state], self.next_move[state])

        if self.rem_count >= self.REC_COUNT or time.time() - self.start_time > self.MAX_TIME:
            return (UNKNOWN, None)
        possible_moves = state.generate_possible_moves()
        random.shuffle(possible_moves)
        lose_moves = []
        win_moves = []
        draw_moves = []
        unknown_moves = []
        for cur_move in possible_moves:
            if time.time() - self.start_time > self.MAX_TIME and not (state in self.is_win and self.is_win[state] != UNKNOWN):
                unknown_moves.append(cur_move)
            else:
                self.rem_count += 1 - int(state in self.visited)
                analyzed = self.proc(cur_move)
                self.rem_count -= 1 - int(state in self.visited)
                if analyzed[0] == WIN:
                    win_moves.append(cur_move)
                elif analyzed[0] == DRAW:
                    draw_moves.append(cur_move)
                elif analyzed[0] == UNKNOWN:
                    unknown_moves.append(cur_move)
                else:
                    lose_moves.append(cur_move)
        self.visited.add(state)

        ##  troubles start here
        if len(lose_moves) != 0:
            self.is_win[state] = WIN
            self.next_move[state] = lose_moves[0]
            return (self.is_win[state], self.next_move[state])
        elif len(draw_moves) != 0 and len(unknown_moves) == 0:
            self.is_win[state] = DRAW
            self.next_move[state] = draw_moves[0]
            return (self.is_win[state], self.next_move[state])
        elif len(lose_moves) == 0 and len(draw_moves) == 0 and len(unknown_moves) == 0:
            self.is_win[state] = LOSE
            self.next_move[state] = win_moves[0]
            return (self.is_win[state], self.next_move[state])
        else:
            self.is_win[state] = UNKNOWN
            sum_size = len(draw_moves) + len(unknown_moves)
            i = random.randint(0, sum_size - 1)
            self.next_move[state] = draw_moves[i] if i < len(draw_moves) else unknown_moves[i - len(draw_moves)]
            return (self.is_win[state], self.next_move[state])
    def process(self, state):
        self.start_time = time.time()
        ret = self.proc(state)
        self.rem_count = 0
        time.sleep(0.2)
        return ret
            



