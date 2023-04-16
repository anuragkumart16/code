from random import randint

turn = 'X'
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-' ]

def display_board():
  print(board[0] + ' | ' + board[1] + ' | ' +board[2])
  print(board[3] + ' | ' + board[4] + ' | ' +board[5])
  print(board[6] + ' | ' + board[7] + ' | ' +board[8])


def turn_for_bot():
  random_chance_for_bot = randint(0,8)
  if board[random_chance_for_bot] == '-':
    bot_chance = random_chance_for_bot + 1
    print('Choose a location from 1-9 : '+ str(bot_chance))
    board[random_chance_for_bot] = 'X'
  else :
    turn_for_bot() 
 

def chance_of_person():
  locate = input('Choose a location from 1-9 : ')
  locate = int(locate)-1
  if board[locate] == '-':
    board[locate] = 'O'
  else :
    print('Location is already occupied.Pls try again.')
    chance_of_person()

   
  


global game_run
game_run = True
def check_winner():  
  row1 = board[0]==board[1]==board[2] != '-'
  row2 = board[3]==board[4]==board[5] != '-'
  row3 = board[6]==board[7]==board[8] != '-'
  col1 = board[0]==board[3]==board[6] != '-'
  col2 = board[1]==board[4]==board[7] != '-'
  col3 = board[2]==board[5]==board[8] != '-'
  diag1= board[0]==board[4]==board[8] != '-'
  diag2= board[2]==board[4]==board[6] != '-'
  if row1 == True:
    print(board[0]+' is winner')
  elif row2 == True:
    print(board[3]+' is winner')
  elif row3 == True:
    print(board[6]+' is winner')
  elif col1 == True:
    print(board[0]+' is winner')
  elif col2 == True :
    print(board[1]+' is winner')
  elif col3 == True :
    print(board[2]+' is winner') 
  elif diag1 == True:
    print(board[8]+' is winner')
  elif diag2 == True:
    print(board[4]+' is winner')
  elif "-" not in board :
    print('Tie')
    global game_run
  if col1 or col2 or col3 or row1 or row2  or row3 or diag1 or diag2 or '-' not in board :
    game_run = False


turn ='X'
def flip_player():
  global turn
  if turn == 'X' :
    turn = 'O'
    print()
    print(turn + "'s turn")
    chance_of_person()
    display_board()
  elif turn == 'O' :
     turn = 'X'
     print()
     print(turn + "'s turn")
     turn_for_bot()
     display_board()

display_board()
print('You are O')
while game_run :

  flip_player()
  check_winner()
