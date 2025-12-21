from data_mgmt import data_mgmt
import random

class ai:
    
    def __init__(self, difficulty):        
        self.difficulty = difficulty
        self.dm = data_mgmt()

    def parse_line(self, line):
        temp_gs = []
        prob = []
        gs = []
        i = 0
        while i < (len(line)):
            done = False
            if not i == 0 and i < 46:
                if (i-1)%5 == 1:
                    temp_gs.append(str(line[i]))
            elif  i > 46: #probability section of moves
                gs = temp_gs
                temp_prob = [0, ""]
                for j in range (i, i+11): #prob/probability HERE will have to chunk out/ loop through until we get to next parentheses (chop off commas and spaces) 
                    if done:
                        break
                    if (j - 47)%12 == 1: #position 1 = allowed moved 
                        temp_prob[0] = int(line[j]) 
                    elif (j - 47)%12 == 4:
                        for k in range(5):
                            temp_prob[1] += line[j + k]   
                        done = True
                        try: 
                            temp_prob[1] = float(temp_prob[1]) 
                            prob.append(temp_prob)
                        except Exception as e: 
                            print(e)
            if i + 23 >= len(line): # 23 is to provide a buffer. The buffer is 2* a chunk (12) - 1; so 24 - 1 = 23
                break
            elif i > 46 and (i + 11) < len(line): #46 takes us to the probability portion of the move
                i += 11 # 11 means capturing probabilities from "(" to ")" in chunks of 12; we still iterate through each chunk
            i += 1 # iterating through the game states/ allowed moves
        return gs, prob 

    def generate_line(self, first_line):
        #ad logic to creat each gs-prob line in file from ["gs[0]",....,"gs[8]" + "prob[0]"" +...+ "prob[n]""]
        gs_line = "["
        for gs in range(len(self.gs)):
            if gs != 8:
                gs_line += "\"" + self.gs[gs]  + "\"" + ", "
            else:
                gs_line += "\"" + self.gs[gs] + "\""
        gs_line += "] "  

        prob_line = "["
        default_val = str(round(1/len(self.allowed_moves), 3))
        while len(default_val) < 5:
            default_val += "0" 

        for prob in range(len(self.allowed_moves)):
            #calculate probably 
            # replicate (allowed_moves[prob], default_val), 
            if prob != len(self.allowed_moves) - 1:
                prob_line += "(" + str(self.allowed_moves[prob]) + ", " + default_val + "), " 
            else:
                prob_line += "(" + str(self.allowed_moves[prob]) + ", " + default_val + ")"      
        prob_line += "]"    
        gs_prob_line = gs_line + prob_line
        if not first_line:
            self.dm.write_to_file(self.filename, gs_prob_line)
        else:
            self.dm.write_first_line(self.filename, gs_prob_line)
    
    
    #loop through each game state, calculate equivalents
    #rotate, if match found - then we can record move
    def compare_states(self, gs_current, gs_file):
        for state in range(len(gs_file)):
            # print(gs_file[state])
            symmetries = self.dm.get_symmetry(gs_file[state])
            #iterate through symmetries
            for rotation in range(len(symmetries)):
                if symmetries[rotation] == gs_current:
                    return state, rotation
                
        #if we did not find a move that matches symmetric game-states, add game-state and probabilities to move list
        self.generate_line(False)
        return -1, -1

    def pick_a_move(self, rotation, prob_list):
        rand = random.randint(0, 999)
        # print("random int = ", rand)
        cumulative_int = 0
        for p in prob_list:
            # print("p-value = ", p)
            current_int = int(p[1] * 1000)
            cumulative_int += current_int
            if cumulative_int < rand:
                cumulative_int += current_int
                # print("cumulative int value = ", cumulative_int)
            else:
                rotated_position = p[0] 
                # print("init rotated position = ", rotated_position)
                for i in range(rotation):
                    rotated_position = (3*(2-rotated_position%3) + rotated_position//3) #ccw rotation
                    if i == 3: #vertical flip after first 4 rotations
                        print("diagonal rotation initialized")
                        rotated_position = (3*(2-rotated_position//3) + rotated_position%3)
                print("p[0] = ", p[0], "\n new rotated position: ", rotated_position)
                return rotated_position #computer picks move



    def get_move(self, gs, move_num, allowed_moves):
        self.gs = gs
        self.move_num = move_num
        self.allowed_moves = allowed_moves
        gs_list = []
        prob_list = []
        self.filename = str(self.difficulty) + "_move_" + str(self.move_num) + ".txt"
        file_lines = self.dm.read_from_file(self.filename)
        if file_lines is None:
            self.generate_line(True)
            file_lines = self.dm.read_from_file(self.filename)

        for i in range(len(file_lines)):
            temp_gs, temp_prob = self.parse_line(file_lines[i])
            gs_list.append(temp_gs)
            prob_list.append(temp_prob)
            # print(gs_list[i])
            # print(prob_list[i])
        state, rotation = self.compare_states(gs, gs_list)
        if state == -1:
            state, rotation = self.compare_states(gs, gs_list)
        # print("prob_list: \n", prob_list[state])
        # print(state, rotation)

        move = self.pick_a_move(rotation, prob_list[state])

        return move  
    
    
