from IPython.display import clear_output
import random

def display_board(board):
    clear_output()  # Remember, this only works in jupyter!

    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def player_input():
    player_one_marker = ''
    while player_one_marker != 'X' and player_one_marker != 'O':
        player_one_marker = input('Please choose X or O').upper()
    if player_one_marker == 'O':
        return ('O', 'X')
    else:
        return ('X', 'O')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for position in range(1, 10):
        if space_check(board, position):
            return False
    return True

def player_choice(board):
    crr = 0
    while crr not in [1,2,3,4,5,6,7,8,9] or not space_check(board, crr):
        crr = int(input('Choose your nest position between 1 to 9: '))
    return crr

def replay():
    return input('Do you want to replay this game? Please enter yes or no').lower().startswith('y')

if __name__ == '__main__':
    print('Welcome to the tick tack toe game!')
    keep_gaming = True
    while keep_gaming:
        board = [' '] * 10
        player1_marker, player2_marker = player_input()
        each_turn = choose_first()
        print(each_turn + ' is going to go first.')
        ready_to_play = input('Are you ready to play? Please enter yes or no: ')
        if ready_to_play.lower()[0] == 'n':
            game_on = False
        else:
            game_on = True
        while game_on:
            if each_turn == 'Player 1':
                display_board(board)
                position = player_choice(board)
                place_marker(board, player1_marker, position)
                if win_check(board, player1_marker):
                    display_board(board)
                    print('Congrats, you won the  game')
                    game_on = False
                else:
                    if full_board_check(board):
                        display_board(board)
                        print('The game is draw!')
                        break
                    else:
                        each_turn = 'Player 2'
            else:
                display_board(board)
                position = player_choice(board)
                place_marker(board, player2_marker, position)
                if win_check(board, player2_marker):
                    display_board(board)
                    print('Player 2 has won!')
                    game_on = False
                else:
                    if full_board_check(board):
                        display_board(board)
                        print('The game is now draw!')
                        break
                    else:
                        each_turn = 'Player 1'
        if not replay():
            break
