import data_mgmt
class ai:
    def __init__(self, difficulty):
        self.difficulty = difficulty


    def get_move(self, gs, move_num, reader):
        self.gs = gs
        self.move_num = move_num
        self.filename = str(self.difficulty) + "_move_" + str(self.move_num) + ".txt"
        file_lines = reader.read_from_file(self.filename)
        return file_lines
    