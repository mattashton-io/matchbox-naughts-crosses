# Developed by Matt Ashton (Google Public Sector) and Tyler Witte, PhD (Purdue Fort Wayne).
#build a game of naughts and crosses (tic-tac-toe) with matchboxes, pebbles, and reinforcment learning (via rewards and punishments)

"""
High-level concepts
1)Game
    -Board
    -X-O piece
    -Turn Control
    -Available Moves
    -Win Condition Logic
    -Game State [x, -, 0, - , - , x, 0, x, 0]
    -Display (GUI)
2)Score/Win Condition
    Board will be a list/set of 9 items [0, 1, 2, 3, 4, 5, 6, 7, 8]
    i//3 - rows
    i%3 - cols 
    Every turn, check the state of the board to see if anyone won
3)AI


"""
import time
from data_mgmt import data_mgmt
from ai import ai

board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
game_pieces = []
menu = {} #choose friend or AI
stats = {}
settings = {}
difficulty = ["easy", "medium", "impossible"]
start_game = {}
gui = {}
game_state = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
global player 
draw = False



# load gui
# generate empty game-state
#loop through game state
def allowed_moves():
    temp_array = []
    for i in range(9):
        if game_state[i] == "-":
            temp_array.append(i)
    return temp_array        


def get_move():
#check against valid moves
    time.sleep(2)
    valid_moves = allowed_moves()
    is_valid_move = False
    while not is_valid_move:
        print("your turn")
        print("valid moves: ", valid_moves)
        temp_move = int(input("make a move: "))
        ## SAFETY CHECK NEEDED ##
        for i in range(len(valid_moves)):
            if temp_move == valid_moves[i]:
                is_valid_move = True
                return temp_move
        print("invalid move. Try again.")
        #if statement to check who's turn it is
    return -1

#dif invalid, display error message
#else, make the move
#update game state
#update gui

#check for win
def check_for_win():
    for i in range(len(game_state)):
        if i//3 == 0:
            print(game_state[i], end = " ")
        if i//3 == 1:
             print(game_state[i], end = " ")
        if i//3 == 2:
            print(game_state[i], end = " ")
        if i%3 == 2:
            print("\n")

    moves = []
    #check which player whose turn it is
    if player == 1:
        for p in range(len(game_state)):
            if game_state[p] == "X":
            #list their moves only
                moves.append(p)
    elif player == 0:
        for p in range(len(game_state)):
            if game_state[p] == "O":
            #list their moves only
                moves.append(p)
    else:
        return -1 #if for some reason there's an incorrect player ID entered, return -1
    

    win_conditions = [0, 0, 0, 0, 0, 0, 0, 0] #list/set of 3 x horizontal , 3x vert, 2x diag

    for i in range(len(moves)):
        win_conditions[moves[i]//3] += 1
        win_conditions[moves[i]%3 + 3] += 1
        if moves[i]%4 == 0:
            win_conditions[6] += 1
        if moves[i]%2 == 0 and moves[i] != 8 and moves[i] != 0:
            win_conditions[7] += 1
    
    for w in range(len(win_conditions)):
        if win_conditions[w] == 3:
            return 1
    print(win_conditions)    
    return 0


#update turn_tracker
def change_turn():
    global player
    if player == 1:
        player = 0
    else:
        player = 1

def init_game():
    global player
    player = 1
    

def update_game_state(i, c):
    game_state[i] = c 
    return 1

#clear board
            

#AI Opponent Component
#Feed AI the board state 
#Game state with -'s
#Corresponding position [0 - 8]
# Percent chance to make each move
#Return a move based on available moves
#if move is available, make move and change game state
#if it wins, increase those moves it made

#check symmetry for rotations and reflections
# 4 rotations + vertical reflection + 4 rotations
#i = index; j = rotations
# %3 = x-value; i//3 = y-value
# i = 3*(i//3) + (i%3)
# step 0: diagonal  flip x and y; turn i into x = i//3, y = i%3
# step 1: vertical flip -(i%3 - 1) + 1 -> 2 - i%3
# step 2: 3(y) + x -> how to go back to [i] integers from x,y values

#to rotate board 90-degress counter-clockwise j = 3*(i//3) + (i%3)
# def get_symmetry()
    # for i in range(len(moves)):
    #     win_conditions[moves[i]//3] += 1
    #     win_conditions[moves[i]%3 + 3] += 1


#new i (after rotation)
for i in range(8):
    temp = game_state.copy()
    for j in range(len(game_state)):
        temp[3*(2-j%3) + j//3] = game_state[j]


#PLay state
def play():
    init_game()
    while check_for_win() != 1:
        if not allowed_moves():
            draw = True
            break

        change_turn()               
        if player == 1:
            c = "X"
        else:
            c = "O"
#       update the player 

        #get move from AI
        move = get_move()
        
        update_game_state(move, c)
    print("-- GAME OVER --")
    if check_for_win() == 1:
        print("Player ", player, " won!")
    else:
        print("It's a Draw")

def print_symmetries():
    dm = data_mgmt()
    test_gs = ["-", "X", "-", "-", "O", "-", "X", "-", "-"]
    test_symmetry = dm.get_symmetry(test_gs)
    for j in range(8):
        for i in range(len(game_state)):
            if i//3 == 0:
                print(test_symmetry[j][i], end = " ")
            if i//3 == 1:
                print(test_symmetry[j][i], end = " ")
            if i//3 == 2:
                print(test_symmetry[j][i], end = " ")
            if i%3 == 2:
                print("\n")
        print("\n")
# play()
# print_symmetries()

opponent = ai("easy")

game_state_test = ["-", "-", "-", "-", "X", "-", "-", "-", "-"]
game_state = game_state_test
#printed twice? 
print(opponent.get_move(game_state_test, 1, allowed_moves())) ## ai.py get_move()

#format data structure
#request move
#give turn number
# "easy_move_1
# #open (file)
# #loop: untl end or find match
#   current game_state
#   symmetries
#   line gs == symmetries
#   determine move w/prob