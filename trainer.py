# of games trained
# game state probability 
# check win percentage

#req move
# get turn
#get game state, if game state == symmetry ...
# if game state does not equal symmetry ...

#keep track of all moves in game state
from ai import ai

class trainer:
    """Punishment and Reward System for Game"""
    def __init__(self):
        self.ai_moves_1 = []
        self.ai_moves_2 = []
        return None

    def update_move(self, gs):
        self.gs = gs
        return 0

    def get_move(self, gs, move_num, allowed_moves, ai_obj, player):
        board_move, file_move = ai_obj.trainer_get_move(gs, move_num, allowed_moves)
        if player == 1:
            self.ai_moves_1.append(file_move)
            print("ai_moves_1: ", self.ai_moves_1)
        else:
            self.ai_moves_2.append(file_move)
            print("ai_moves_2: ", self.ai_moves_2)
        return board_move

    
    