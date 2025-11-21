from data_mgmt import data_mgmt
class ai:
    
    def __init__(self, difficulty):        
        self.difficulty = difficulty
        self.dm = data_mgmt()

    def parse_line(self, line):
        temp_gs = []
        prob = [[] for _ in range(2)]
        for i in range(len(line)):
            if not i == 0 and i < 46:
                if (i-1)%5 == 1:
                    temp_gs.append(str(line[i]))
            elif  i > 46:
                if (i-1)%5 == 1:
                    pass    #prob/probability HERE will have to chunk out/ loop through until we get to next parentheses (chop off commas and spaces)           
        return temp_gs
        
        
        #extract the allowed moves as well
        #rotate, if match found - then we can record move


    def get_move(self, gs, move_num):
        self.gs = gs
        self.move_num = move_num
        self.filename = str(self.difficulty) + "_move_" + str(self.move_num) + ".txt"
        file_lines = self.dm.read_from_file(self.filename)
        for i in range(len(file_lines)):
            temp = self.parse_line(file_lines[i])
            print(temp)
        return 0 
    
