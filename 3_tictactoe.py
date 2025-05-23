# Tic-Tac-Toe Board Printer
# Print a 3x3 Tic-Tac-Toe board with numbers or player symbols.

import os
import time

# Our game board. We're using index 0 as a placeholder, so positions 1-9 are what we care about.
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '] 
player = 1 

# Game state constants
Win = 1
Draw = -1
Running = 0
Stop = 1

Game = Running 
Mark = 'X' # Player 1 starts with 'X'

# This function just draws the board.
def DrawBoard():
    print(" %c | %c | %c " % (board[1],board[2],board[3]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[4],board[5],board[6]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[7],board[8],board[9]))
    print("   |   |   ")

# Checks if the spot a player picked is empty.
def CheckPosition(x):
    if(board[x] == ' '):
        return True
    else:
        return False

# Checks if anyone has won or if it's a draw.
def CheckWin():
    global Game
    # Checking rows
    if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):
        Game = Win
    elif(board[4] == board[5] and board[5] == board[6] and board[4] != ' '):
        Game = Win
    elif(board[7] == board[8] and board[8] == board[9] and board[7] != ' '):
        Game = Win
    # Checking columns
    elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):
        Game = Win
    elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):
        Game = Win
    elif(board[3] == board[6] and board[6] == board[9] and board[3] != ' '):
        Game=Win
    # Checking diagonals
    elif(board[1] == board[5] and board[5] == board[9] and board[5] != ' '):
        Game = Win
    elif(board[3] == board[5] and board[5] == board[7] and board[5] != ' '):
        Game=Win
    # Check for a draw
    elif(board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ' and board[9]!=' '):
        Game=Draw
    else:
        Game=Running 

print("Tic-Tac-Toe Game Designed By Sourabh Somani")
print("Player 1 [X] --- Player 2 [O]\n")
print()
print()
print("Please Wait...")
time.sleep(3) 

# The main game loop. Runs until someone wins or it's a draw.
while(Game == Running):
    os.system('cls') 
    DrawBoard() 

    # Figures out whose turn it is.
    if(player % 2 != 0):
        print("Player 1's chance")
        Mark = 'X'
    else:
        print("Player 2's chance")
        Mark = 'O'
    
    
    choice = int(input("Enter the position between [1-9] where you want to mark:"))

    # If the spot is open, make the move.
    if(CheckPosition(choice)):
        board[choice] = Mark
        player+=1 
        CheckWin() 

os.system('cls')
DrawBoard() 

# Announce the results!
if(Game==Draw):
    print("Game Draw")
elif(Game==Win):
    player-=1 # Go back to the winning player.
    if(player%2!=0):
        print("Player 1 Won")
    else:
        print("Player 2 Won")