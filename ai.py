from data_mgmt import data_mgmt
class ai:
    
    def __init__(self, difficulty):        
        self.difficulty = difficulty
        self.dm = data_mgmt()

    def parse_line(self, line):
        temp_gs = []
        prob = [[]]
        print(prob)
        i = 0
        while i < (len(line)):
            done = False
            if not i == 0 and i < 46:
                if (i-1)%5 == 1:
                    temp_gs.append(str(line[i]))
            elif  i > 46: #probability section of moves
                temp_prob = [0, ""]
                for j in range (i, i+11): #prob/probability HERE will have to chunk out/ loop through until we get to next parentheses (chop off commas and spaces) 
                    # print("j - 47: ", j - 47)
                    if done:
                        # print("done")
                        break
                    if (j - 47)%12 == 1: #position 1 = allowed moved 
                        temp_prob[0] = int(line[j]) 
                        # print("temp_prob[0]: ", temp_prob[0])
                    elif (j - 47)%12 == 4:
                        for k in range(5):
                            temp_prob[1] += line[j + k]   
                        # print("temp_prob[1]: ", temp_prob[1])
                        done = True
                        try: 
                            temp_prob[1] = float(temp_prob[1]) 
                            print((j - 47)//12)
                            if (j - 47 //12) < 0:
                                prob[(j-47)//12][0] = temp_prob[0]
                            else:
                                prob.append(temp_prob)
                            # print(prob)
                                print(prob[(j - 47)//12])
                        except Exception as e: 
                            print(e)
            if i + 11 < len(line):
                i = i + 11
            else:
                break
            i += 1
        return temp_gs

        
    #loop through each game state, calculate equivalents
    #rotate, if match found - then we can record move
    def compare_states(self, gs_current, gs_file):
        for state in range(len(gs_file)):
            symmetries = self.dm.get_symmetry(gs_file[state])
            ##extract the allowed moves
            for i in range(len(symmetries)):
                if symmetries[i] == gs_current:
                    return state, i
                
        #if we did not find a move that matches symmetric game-states, add game-state  to move list
        return -1, -1


    def get_move(self, gs, move_num):
        self.gs = gs
        self.move_num = move_num
        gs_list = []
        self.filename = str(self.difficulty) + "_move_" + str(self.move_num) + ".txt"
        file_lines = self.dm.read_from_file(self.filename)
        for i in range(len(file_lines)):
            temp = self.parse_line(file_lines[i])
            gs_list.append(temp)
        return 0 #returning 0 in the console as a placeholder 
    
    
