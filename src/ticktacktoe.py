from IPython.display import clear_output
import random
import time
import string
#   two people on the same board in front of a single pc
#   use numpad to match numbers on a tic tac toe board
#   alternate between x and o
# 123
# 456
# 789
def display_board(board):
    print('\n     |     |     ')
    print('  ' + board[0] + '  |  ' +  board[1] +  '  |   ' + board[2])
    print('     |     |     ')
    print('------------------')
    print('     |     |     ')
    print('  ' + board[3] + '  |  ' + board[4] + '  |   ' + board[5])
    print('     |     |     ')
    print('------------------')
    print('     |     |     ')
    print('  ' + board[6] + '  |  ' +  board[7] +  '  |   ' + board[8])
    print('     |     |     \n')



def player_input():
    wrong_choice = True
    while wrong_choice == True:
        player1_choice = input('You are player 1, please provide your choice between O and X: ').upper()
        if player1_choice == 'O' or player1_choice == 'X':
            wrong_choice = False
        else:
            wrong_choice = True
            print('Please enter a valid choice')
    return player1_choice

def place_marker(board, marker, position):
    board[position - 1] = marker

def win_check(board, mark):
    mark_counter = 0
    notmark_counter = 0
    notmark = ''
    if mark == 'X':
        notmark = 'O'
    else:
        notmark = 'X'
    if board[0] == mark and board[1] == mark and board[2] == mark:
        mark_counter += 1
    elif board[3] == mark and board[4] == mark and board[5] == mark:
        mark_counter += 1
    elif board[6] == mark and board[7] == mark and board[8] == mark:
        mark_counter += 1
    elif board[0] == mark and board[3] == mark and board[6] == mark:
        mark_counter += 1
    elif board[1] == mark and board[4] == mark and board[7] == mark:
        mark_counter += 1
    elif board[2] == mark and board[5] == mark and board[8] == mark:
        mark_counter += 1
    elif board[0] == mark and board[4] == mark and board[8] == mark:
        mark_counter += 1
    elif board[2] == mark and board[4] == mark and board[6] == mark:
        mark_counter += 1
    else:
        pass

    if board[0] == notmark and board[1] == notmark and board[2] == notmark:
        notmark_counter += 1
    elif board[3] == notmark and board[4] == notmark and board[5] == notmark:
        notmark_counter += 1
    elif board[6] == notmark and board[7] == notmark and board[8] == notmark:
        notmark_counter += 1
    elif board[0] == notmark and board[3] == notmark and board[6] == notmark:
        notmark_counter += 1
    elif board[1] == notmark and board[4] == notmark and board[7] == notmark:
        notmark_counter += 1
    elif board[2] == notmark and board[5] == notmark and board[8] == notmark:
        notmark_counter += 1
    elif board[0] == notmark and board[4] == notmark and board[8] == notmark:
        notmark_counter += 1
    elif board[2] == notmark and board[4] == notmark and board[6] == notmark:
        notmark_counter += 1
    else:
        pass
    print(mark_counter)
    print(notmark_counter)
    if mark_counter > notmark_counter:
        return 'won'
    else:
        return 'lost'

def choose_first():
    firstone = random.randint(1,2)
    if firstone == 1:
        print('player1 goes first')
    else:
        print('player2 goes first')

def space_check(board, position):
    return board[position - 1] == ' '

def full_board_check(board):
    for space in board:
        if space == ' ' or space == '':
            break;
            return False
    return True

def player_choice(board):
    flag = False
    crr_choice = 0
    while flag == False:
        crr_choice = int(input('Choose your next position? Choose a number between 1 to 9: '))
        if space_check(board, crr_choice) == True:
            flag = False
        if crr_choice not in range(1, 10):
            print('Please make a valid choice')
            flag = False
        else:
            return crr_choice
            flag = True


def replay():
    return input('do you want to replay? yes or no').lower().startswith('y')

def ready_to_play():
    flag = False
    while flag == False:
        let_go = input('Are you ready to play the game? Answer with yes or no: ')
        if let_go == 'yes' or let_go == 'no':
            flag = True
        else:
            print('Please provide a valid choice. yes or no: ')
    if let_go == 'no':
        print('You are not ready to play this game. Please take your time and'
              'restart the game whenever you want!')
        return False
    else:
        return True
if __name__ == '__main__':
    keep_gaming = True
    while keep_gaming == True:
        board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        inner_gaming = True
        print('Welcome to the tick tack toe game!\n')
        #   player 1 chooses x or o
        player_one_choice = player_input()
        #   ask if the player is ready to play. quit the game if not ready
        ready = ready_to_play()
        if (ready == False):
            keep_gaming = False
            inner_gaming = False
            break
        #   take user choice and store it
        #display_board(board)
        choose_first()
        while inner_gaming == True:
            display_board(board)
            current_choice = int(player_choice(board))
            player_two_choice = ''
            if player_one_choice == 'O':
                player_two_choice = 'X'
            else:
                player_two_choice = 'O'
            #   display the emtpy board
            full_board = full_board_check(board)
            place_marker(board, player_one_choice, current_choice)
            display_board(board)
            if full_board == False:
                inner_gaming = False
            win_state = win_check(board, player_one_choice)
            if win_state == 'won':
                print("congrats")
                inner_gaming = False
                break
            elif win_state == 'lost' and full_board == False:
                print("sadge")
                inner_gaming = False
            #player 2
            player_two_index = int(player_choice(board))
            full_board = full_board_check(board)
            place_marker(board, player_two_choice, player_two_index)
            display_board(board)
            win_state = win_check(board, player_one_choice)
            if win_state == 'won':
                print("congrats")
                inner_gaming = False
                break
            elif win_state == 'lost' and full_board == False:
                print("sadge")
                inner_gaming = False
        if not replay():
            keep_gaming = False
            break