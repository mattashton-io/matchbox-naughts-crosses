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
        pass

    def update_move(self, gs):
        self.gs = gs
        return 0

    def get_move(self, gs, move_num, allowed_moves, ai_obj):
        return ai_obj.get_move(gs, move_num, allowed_moves)