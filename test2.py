import os
import random
def display_board(board):
   os.system('clear')
   for i in range (1,2):
       for j in range(1,4):
           if i == 1 and j == 1:
               print('   |   |')
               print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
               print('   |   |')
               print('-----------')
           elif i == 1 and j == 2:
               print('   |   |')
               print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
               print('   |   |')
               print('-----------')
           else:
                print('   |   |')
                print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
                print('   |   |')  
           j+=1
       i+=1       
                   
def player_input():
    marker=''
    while not (marker=="X" or marker == "O"):
        marker = input("Player1: Do you want to be 'X' or 'O':").upper()
    if marker == 'X':
        return('X','O')
    else:
        return('O','X')        


def place_marker(board,marker,position):
    board[position]=marker

def win_check(board,marker):
    return ((board[1]==board[2]==board[3] == marker) or 
        (board[4]==board[5]==board[6] == marker) or 
        (board[7]==board[8]==board[9] == marker) or
        (board[1]==board[4]==board[7] == marker) or
        (board[3]==board[6]==board[9] == marker) or
        (board[2]==board[5]==board[8] == marker) or
        (board[1]==board[5]==board[9] == marker) or
        (board[7]==board[5]==board[3] == marker))
             
def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'player1'
    else:
        return 'player2'
def space_check(board,position):
    return board[position] == ' '
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
    return position
def reply():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

while True:
    theboard = [' ']*10
    player1_marker,player2_marker = player_input()
    turn = choose_first()
    print(' Congratulations '+  turn + ' you will be going first ')
    play_game = input('Are you ready to play ? Enter yes or no:')
    if play_game[0].lower() == 'y':
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn == 'player1':
            display_board(theboard)
            position = player_choice(theboard)
            place_marker(theboard,player1_marker,position)
            if win_check(theboard,player1_marker):
                display_board(theboard)
                print('Congratulations! you won the game')
                game_on = False
            else:
                if full_board_check(theboard):
                    display_board(theboard)
                    print("the match is drawn") 
                else:
                    turn = 'player2'    
        if turn == 'player2':
            display_board(theboard)
            position = player_choice(theboard)
            place_marker(theboard,player2_marker,position)
            if win_check(theboard,player2_marker):
                display_board(theboard)
                print('Player2 you won the game')
                game_on = False
            else:
                if full_board_check(theboard):
                    display_board(theboard)
                    print("the match is drawn")
                else:
                    turn = 'player1'
    if not reply():
        break
                                                