# of games trained
# game state probability 
# check win percentage

#req move
# get turn
#get game state, if game state == symmetry ...
# if game state does not equal symmetry ...

#keep track of all moves in game state
from ai import ai
from data_mgmt import data_mgmt

class trainer:
    """Punishment and Reward System for Game"""
    def __init__(self, difficulty):
        #moves made
        self.ai_moves_1 = []
        self.ai_moves_0 = []
        self.gs = []
        self.difficulty = difficulty
        self.dm = data_mgmt()
        self.ai = ai(difficulty)
        return None
    
    def normalize (self, prob):
        val = 0

        for p in range(len(prob)): 
            val += prob[p][1] #accumulate total value %

        for p in range(len(prob)):
            prob[p][1] = round(prob[p][1]/val, 3) #normalize so no probs are over 1.000

        val = 0
        for p in range(len(prob)):
            val += prob[p][1]
        prob[-1][1] += 1 - val #add remaining prob due to rounding to last entry in prob list

        if prob[-1][1] < 0:
            prob[-1][1] = 0
            prob = self.normalize(prob) #recursion, function calling itself. Re-normalize in case prob is less than 0

        return prob

    def update_file(self, player): #can add "win" as param if we decide to implement DRAW logic
        #grab game state from self.gs
        for i in range(len(self.gs)):
            cf = self.dm.read_from_file(str(self.difficulty) + "_move_" + str(i) + ".txt")
            # print(self.gs[i])
            # print("filedump: ", cf)
            state, prob = self.ai.parse_line(cf[self.gs[i]]) 

            #update probabilities in prob section
            if self.first_to_move == 0: #inspecting moves made by player 0
                if i%2 == 0: #even moves made by player 0; are we on an even move?
                    move = self.ai_moves_0[i//2] #allows us to update in pairs (W-Ls or L-Ws)
                else: #even moves made by player 1
                    move = self.ai_moves_1[i//2]
            else: #inspecting moves made by player 1
                if i%2 == 0: #even moves made by player 1
                    move = self.ai_moves_1[i//2]
                else: #even moves made by player 0
                    move = self.ai_moves_0[i//2]

            index = 10 #10 is out of bounds
            # print("update_file move: ", move)
            for j in range(len(prob)):
                if prob[j][0] == move:
                    index = j #which line we're on inside the prob array
                    break

            if self.first_to_move == player: #did the winner go first; am I updating easy_move_0 or not
                #self.ai.moves_x -> increase probability of those moves
                if i%2 == 0: 
                    prob[index][1] *= 1.05
                    prob = self.normalize(prob)
                else:
                    prob[index][1] *= 0.95
                    prob = self.normalize(prob)
            else:
                if i%2 == 0: 
                    prob[index][1] *= 0.95
                    prob = self.normalize(prob)
                else:
                    prob[index][1] *= 1.05
                    prob = self.normalize(prob)
            # print("gs_prob_line: ", self.dm.generate_line(state, prob))
            self.dm.update_file(str(self.difficulty) + "_move_" + str(i) + ".txt", self.dm.generate_line(state, prob), self.gs[i])

    def get_move(self, gs, move_num, allowed_moves, ai_obj, player):
        board_move, file_move, file_gs = ai_obj.trainer_get_move(gs, move_num, allowed_moves)
        if player == 1:
            self.ai_moves_1.append(file_move)
            print("ai_moves_1: ", self.ai_moves_1)
            if move_num == 0:
                self.first_to_move = 1
        else:
            self.ai_moves_0.append(file_move)
            print("ai_moves_0: ", self.ai_moves_0)
            if move_num == 0:
                self.first_to_move = 0
        self.gs.append(file_gs)
        print("gs: ", self.gs)
        print("board_move: ", board_move)
        return board_move
    #store gamestate to ensure we are changing correct item in move.txt file
    #move number = move_num* file
    
    

    #editing the file
    #editing correct gamestate in file

    # use file_move to change probabilities based on wins and losses


    #send info back to trainer when game is complete (win, loss, or draw)
