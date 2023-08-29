import random, pyfiglet, os

#----------------Title------------------#
def title():
    os.system("cls")
    print(pyfiglet.figlet_format("TicTacToe"))
#---------------------------------------#


#----------------Board------------------#
def print_board(board):
  for row in board:
    print("|".join(row))
    print("-" * 5)
#---------------------------------------#


#------------Win Condition--------------#
def check_win(board, player):
  # Check rows
  for row in board:
    if all(cell == player for cell in row):
      return True

  # Check columns
  for col in range(3):
    if all(board[row][col] == player for row in range(3)):
      return True

  # Check diagonals
  if board[0][0] == board[1][1] == board[2][2] == player:
    return True
  if board[0][2] == board[1][1] == board[2][0] == player:
    return True

  return False
#---------------------------------------#


#---------------Bot Move-----------------#
def computer_move(board):
  while True:
    row = random.randint(0, 2)
    col = random.randint(0, 2)
    if board[row][col] == "-":
      board[row][col] = "O"
      break
#---------------------------------------#

#------------Board intialize------------#
board = [["-" for _ in range(3)] for _ in range(3)]
#---------------------------------------#

#--------------Game Loop-----------------#
while True:
  #Create a clean free tictactoe ascii
  title()
  # Player's move
  print_board(board)
  while True:
    row = int(input("Enter the row (0-2): "))
    col = int(input("Enter the column (0-2): "))
    if board[row][col] == "-":
      board[row][col] = "X"
      break
    else:
      print("Invalid move. Try again.")

  # Check if the player has won
  if check_win(board, "X"):
    print_board(board)
    print("Congratulations! You won!")
    break

  # Check if it's a tie
  if all(cell != "-" for row in board for cell in row):
    print_board(board)
    print("It's a tie!")
    break

  # Computer's move
  computer_move(board)

  # Check if the computer has won
  if check_win(board, "O"):
    print_board(board)
    print("You lost! The computer won.")
    break
#---------------------------------------#