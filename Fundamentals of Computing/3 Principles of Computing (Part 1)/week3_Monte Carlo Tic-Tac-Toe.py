"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 1         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player
# print(provided.EMPTY) = 1
# print(provided.PLAYERX) = 2
# print(provided.PLAYERO) = 3
# print(provided.DRAW) = 4

def random_draw(board, player, empty_cells_list):
    '''
    Help with the mc_trail function
    '''
    selected_cell = random.choice(empty_cells_list)
    board.move(selected_cell[0], selected_cell[1], player)
    player = provided.switch_player(player)
    empty_cells_list.remove(selected_cell)

def mc_trial(board, player):
    '''
    Modify the board input
    '''
    empty_cells = board.get_empty_squares()
    # check win
    winner = board.check_win()
    while winner == None:
        random_draw(board, player, empty_cells)
        winner = board.check_win()
        
def mc_update_scores(scores, board, player):
    '''
    Update the scores grid 
    '''
    winner = board.check_win()
  
    for col in range(board.get_dim()):
        for row in range(board.get_dim()):
            if winner == provided.DRAW:
                scores[row][col] += 0
            
            elif winner == player and board.square(row,col) == player:
                scores[row][col] += SCORE_CURRENT
            elif winner == player and board.square(row, col) != player and board.square(row, col) != provided.EMPTY:
                scores[row][col] -= SCORE_OTHER
            elif winner != player and board.square(row,col) == player:
                scores[row][col] -= SCORE_CURRENT
            elif winner != player and board.square(row, col) != player and board.square(row, col) != provided.EMPTY:
                scores[row][col] += SCORE_OTHER
            elif board.square(row, col) == provided.EMPTY:
                scores[row][col] -= 0.0        
        

def get_best_move(board, scores):
    '''
    Get best move
    '''
    max_score = -1000
    
    for col in range(board.get_dim()):
            for row in range(board.get_dim()):
                if scores[row][col] >  max_score and board.square(row, col) == provided.EMPTY:
                    
                    max_score = scores[row][col]
                    
    # find empty squares with max score                
    empty_squares = board.get_empty_squares()
    candidate_move_list = []
    for square in empty_squares:
        if scores[square[0]][square[1]] == max_score:
            candidate_move_list.append(square)

    row, col = candidate_move_list[random.randrange(0,len(candidate_move_list))] 
    return row, col

def mc_move(board, player, trials):
    '''
    Move
    '''
    score_board = [ [0 for dummy_col in range(board.get_dim())] for dummy_row in range(board.get_dim())]
    for dummy_i in range(trials):
        trial_board = board.clone()
        mc_trial(trial_board, player)
        mc_update_scores(score_board, trial_board, player)
   
    row, col = get_best_move(board, score_board)
    
    return row, col


# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

# provided.play_game(mc_move, NTRIALS, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)