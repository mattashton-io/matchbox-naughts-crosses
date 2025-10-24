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


board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
game_pieces =
menu = {} #choose friend or AI
stats = {}
settings = {}
difficulty = ["easy", "medium", "impossible"]
start_game = {}
gui = {}
game_state = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
valid_moves = []
is_valid_move = False

player = 1



# load gui
# generate empty game-state
#loop through game state
def allowed_moves():
    for i in range[9]:
        if game_state[i] == "-":
            valid_moves.append([i])


def get_move():
#check against valid moves
    time.sleep(3)
    while not is_valid_move:
        print("your turn")
        temp_move = input("make a move: ")
        for i in range(len(valid_moves)):
            if temp_move == valid_moves[i]:
                is_valid_move = True
                return temp_move
            else:
                print("invalid move. Try again.")
        #if statement to check who's turn it is
    return -1

#dif invalid, display error message
#else, make the move
#update game state
#update gui

#check for win
def check_for_win():
    moves = []
    #check which player whose turn it is
    if player == 1:
        for p in len(game_state):
            if game_state[p] == "X":
            #list their moves only
                moves.append(p)
    elif player == 0:
        for p in len(game_state):
            if game_state[p] == "O":
            #list their moves only
                moves.append(p)
    else:
        return -1

    for i in len(game_state):
        if i//3 == 0:
            return 0
        elif 
        
#update turn_tracker
def change_turn():
    if player == 1:
        player = 0
    else:
        player = 1

def init_game():
    return 1

def update_game_state():
    return 1

#clear board

#PLay state
def play():
    init_game()
    while True:
        #check which moves are valid
        allowed_moves()
        
        #get move from AI
        get_move()
        
        update_game_state()

        #check for win
        check_for_win()

        #update the player 
        change_turn()
    