
#check symmetry for rotations and reflections
# 4 rotations + vertical reflection + 4 rotations
#i = index; j = rotations
# %3 = x-value; i//3 = y-value
# i = 3*(i//3) + (i%3)
# step 0: diagonal  flip x and y; turn i into x = i//3, y = i%3
# step 1: vertical flip -(i%3 - 1) + 1 -> 2 - i%3
# step 2: 3(y) + x -> how to go back to [i] integers from x,y values
#to rotate board 90-degress counter-clockwise j = 3*(i//3) + (i%3)
#new integer value (after rotation) = 3(2-j%3) + j//3

class data_mgmt:
    def get_symmetry(game_state):
        symmetry = [["-" for k in range(8)] for l in range(len(game_state))] #8 game state rows, each game state row will be populated with "-" across 9 positions
        symmetry[0] = game_state.copy() #locks in current game state to top row 
        for i in range(7): #
            temp = game_state.copy()
            if i == 4: #vertical flip after first 4 rotations
                for j in range(len(game_state)):
                    temp[3*(2-j//3) + j%3] = symmetry[i][j]
            for j in range(len(game_state)):
                    temp[3*(2-j%3) + j//3] = symmetry[i][j]
            symmetry[i+1] = temp
        return symmetry