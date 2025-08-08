#Tic Tac Toe
from random import randint
import time
def clear_screen():
    import os
    import sys
    try:
        from IPython import get_ipython
        if get_ipython() is not None:
            from IPython.display import clear_output
            clear_output(wait=True)
            return
    except ImportError:
        pass
    print("\033[2J\033[H", end="")
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')
num_check = str(list(range(1,10)))
game_board = ["|","\033[34m1\033[0m","|","2","|","3","|"]
game_board2 = ["|","4","|","5","|","6","|"]
game_board3 = ["|","7","|","8","|","9","|"]
game_start = True
bot_active = False
bot_choice = "0"
def game_playerfirst():
    global bot_active
    print("_______")
    print(f"{game_board[0]}{game_board[1]}{game_board[2]}{game_board[3]}{game_board[4]}{game_board[5]}{game_board[6]}")
    print(f"{game_board2[0]}{game_board2[1]}{game_board2[2]}{game_board2[3]}{game_board2[4]}{game_board2[5]}{game_board2[6]}")
    print(f"{game_board3[0]}{game_board3[1]}{game_board3[2]}{game_board3[3]}{game_board3[4]}{game_board3[5]}{game_board3[6]}")
    print("-------")
    print("Place An X.")
    time.sleep(0.25)
    choice1 = input("")
    if(choice1 in num_check and choice1 == "1" and game_board[1] != "X" and game_board[1] != "O"):
     game_board[1] = "X"
     clear_screen()
     bot_active = True
     game_start = False
    elif(choice1 in num_check and choice1 == "2" and game_board[3] != "X" and game_board[3] != "O"):
     game_board[3] = "X"
     clear_screen()
     bot_active = True
     game_start = False
    elif(choice1 in num_check and choice1 == "3" and game_board[5] != "X" and game_board[5] != "O"):
     game_board[5] = "X"
     clear_screen()
     bot_active = True
     game_start = False
    elif(choice1 in num_check and choice1 == "4" and game_board2[1] != "X" and game_board2[1] != "O"):
     game_board2[1] = "X"
     clear_screen()
     bot_active = True
     game_start = False
    elif(choice1 in num_check and choice1 == "5" and game_board2[3] != "X" and game_board2[3] != "O"):
     game_board2[3] = "X"
     clear_screen()
     bot_active = True
     game_start = False
    elif(choice1 in num_check and choice1 == "6" and game_board2[5] != "X" and game_board2[5] != "O"):
     game_board2[5] = "X"
     clear_screen()
     bot_active = True
     game_start = False
    elif(choice1 in num_check and choice1 == "7" and game_board3[1] != "X" and game_board3[1] != "O"):
     game_board3[1] = "X"
     clear_screen()
     bot_active = True
     game_start = False
    elif(choice1 in num_check and choice1 == "8" and game_board3[3] != "X" and game_board3[3] != "O"):
     game_board3[3] = "X"
     clear_screen()
     bot_active = True
     game_start = False
    elif(choice1 in num_check and choice1 == "9" and game_board3[5] != "X" and game_board3[5] != "O"):
     game_board3[5] = "X"
     clear_screen()
     bot_active = True
     game_start = False
    else:
     print("Error! Please Select A Valid Option!")
    bot_choice = str(randint(1,10))
    while bot_active == True:
     if(bot_choice == "1" and game_board[1] != "X" and game_board[1] != "O"):
      game_board[1] = "O"
      bot_active = False;
      game_start = True
      bot_choice = "0"
     elif(bot_choice == "2" and game_board[3] != "X" and game_board[3] != "O"):
      game_board[3] = "O"
      bot_active = False;
      game_start = True
      bot_choice = "0"
     elif(bot_choice == "3" and game_board[5] != "X" and game_board[5] != "O"):
      game_board[5] = "O"
      bot_active = False;
      game_start = True
      bot_choice = "0"
     elif(bot_choice == "4" and game_board2[1] != "X" and game_board2[1] != "O"):
      game_board2[1] = "O"
      bot_active = False;
      game_start = True
      bot_choice = "0"
     elif(bot_choice == "5" and game_board2[3] != "X" and game_board2[3] != "O"):
      game_board2[3] = "O"
      bot_active = False;
      game_start = True
      bot_choice = "0"
     elif(bot_choice == "6" and game_board2[5] != "X" and game_board2[5] != "O"):
      game_board2[5] = "O"
      bot_active = False;
      game_start = True
      bot_choice = "0"
     elif(bot_choice == "7" and game_board3[1] != "X" and game_board3[1] != "O"):
      game_board3[1] = "O"
      bot_active = False;
      game_start = True
      bot_choice = "0"
     elif(bot_choice == "8" and game_board3[3] != "X" and game_board3[3] != "O"):
      game_board3[3] = "O"
      bot_active = False;
      game_start = True
      bot_choice = "0"
     elif(bot_choice == "9" and game_board3[5] != "X" and game_board3[5] != "O"):
      game_board3[5] = "O"
      bot_active = False;
      game_start = True
      bot_choice = "0"
     else:
      bot_choice = str(randint(1,9))
def menu():
  print("Start Game?")
  prompt1 = input("")
  if(prompt1 == "Start" or prompt1 == "Yes"):
   menu_active = False
  else:
    print("Error! Please Enter A Valid Response.")
    return menu()
menu()
while game_start == True:
 game_playerfirst()
 if(game_board[1] == "X" and game_board[3] == "X" and game_board[5] == "X" or game_board[1] == "X" and game_board2[3] == "X" and game_board3[5] == "X" or game_board[5] == "X" and game_board2[3] == "X" and game_board3[1] == "X" or game_board[3] == "X" and game_board2[3] == "X" and game_board3[3] == "X" or game_board[1] == "X" and game_board2[1] == "X" and game_board3[1] == "X" or game_board[5] == "X" and game_board2[5] == "X" and game_board3[5] == "X" or game_board2[1] == "X" and game_board2[3] == "X" and game_board2[5] == "X" or game_board3[1] == "X" and game_board3[3] == "X" and game_board3[5] == "X"):
      print("You Win!")
      print("_______")
      print(f"{game_board[0]}{game_board[1]}{game_board[2]}{game_board[3]}{game_board[4]}{game_board[5]}{game_board[6]}")
      print(f"{game_board2[0]}{game_board2[1]}{game_board2[2]}{game_board2[3]}{game_board2[4]}{game_board2[5]}{game_board2[6]}")
      print(f"{game_board3[0]}{game_board3[1]}{game_board3[2]}{game_board3[3]}{game_board3[4]}{game_board3[5]}{game_board3[6]}")
      print("-------")
      game_start = False
      break
 elif(game_board[1] == "O" and game_board[3] == "O" and game_board[5] == "O" or game_board[1] == "O" and game_board2[3] == "O" and game_board3[5] == "O" or game_board[5] == "O" and game_board2[3] == "O" and game_board3[1] == "O" or game_board[3] == "O" and game_board2[3] == "O" and game_board3[3] == "O" or game_board[1] == "O" and game_board2[1] == "O" and game_board3[1] == "O" or game_board[5] == "O" and game_board2[5] == "O" and game_board3[5] == "O" or game_board2[1] == "O" and game_board2[3] == "O" and game_board2[5] == "O" or game_board3[1] == "O" and game_board3[3] == "O" and game_board3[5] == "O"):
      print("You Lose!")
      print("_______")
      print(f"{game_board[0]}{game_board[1]}{game_board[2]}{game_board[3]}{game_board[4]}{game_board[5]}{game_board[6]}")
      print(f"{game_board2[0]}{game_board2[1]}{game_board2[2]}{game_board2[3]}{game_board2[4]}{game_board2[5]}{game_board2[6]}")
      print(f"{game_board3[0]}{game_board3[1]}{game_board3[2]}{game_board3[3]}{game_board3[4]}{game_board3[5]}{game_board3[6]}")
      print("-------")
      game_start = False
      break
 elif(game_board[1] != "1" and game_board[3] != "2" and game_board[5] != "3" and game_board2[1] != "4" and game_board2[3] != "5" and game_board2[5] != "6" and game_board3[1] != "7" and game_board3[3] != "8" and game_board3[5] != "9"):
      print("Game Over! It's A Tie!")
      print("_______")
      print(f"{game_board[0]}{game_board[1]}{game_board[2]}{game_board[3]}{game_board[4]}{game_board[5]}{game_board[6]}")
      print(f"{game_board2[0]}{game_board2[1]}{game_board2[2]}{game_board2[3]}{game_board2[4]}{game_board2[5]}{game_board2[6]}")
      print(f"{game_board3[0]}{game_board3[1]}{game_board3[2]}{game_board3[3]}{game_board3[4]}{game_board3[5]}{game_board3[6]}")
      print("-------")
      game_start = False
      break
