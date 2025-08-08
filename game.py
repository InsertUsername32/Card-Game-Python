from ast import Pass
from os import stat
import time
#Tension BETA v0
#A Card Like Decision Game Based On Lapse
#Utilizes Full Text Like Sprites And 4 Attributes With Bars
from random import randint
#other
#-----------------------
def clear_screen():
    import os
    import sys
    # Check if running in Jupyter notebook
    try:
        from IPython import get_ipython
        if get_ipython() is not None:
            from IPython.display import clear_output
            clear_output(wait=True)
            return
    except ImportError:
        pass

    # For xterm.js in browser
    print("\033[2J\033[H", end="")

    # Fallback for terminal environments
    if os.name == 'posix':  # For Unix/Linux/MacOS
        os.system('clear')
    elif os.name == 'nt':   # For Windows
        os.system('cls')
def title():
 print("░▒▓████████▓▒░▒▓████████▓▒░▒▓███████▓▒░ ░▒▓███████▓▒░▒▓█▓▒░░▒▓██████▓▒░░▒▓███████▓▒░  ")
 print("   ░▒▓█▓▒░   ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ")
 print("   ░▒▓█▓▒░   ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ")
 print("   ░▒▓█▓▒░   ░▒▓██████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ")
 print("   ░▒▓█▓▒░   ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ")
 print("   ░▒▓█▓▒░   ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ")
 print("   ░▒▓█▓▒░   ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░  ")
 print("---------------------------------------------------------------------------------------")
 print("ALPHA V.0.0 - 08/06/2025")
 prompt1 = input("Press Enter To Play ")
 if(prompt1 == ""):
  clear_screen()
 else:
  clear_screen()
  return title()
#-----------------------
#cards
#-----------------------
def card1_Army1():
 print("")
 print("\033[1m  General Joe D. Pizenhower\033")
 print(".----------------------------.")
 print("|      ░░░░░░░░░░░░░░░░      |")
 print("|       ░░░░░░░░░░░░░░       |")
 print("|       █░░▒░░▒░░▒░░░█       |")
 print("|       ██████████████       |")  
 print("|        ████████████        |")
 print("|         ██████████         |")
 print("|          ████████          |")
 print("|     ██ ██  ████  ██ ██     |")
 print("|  █████░██▓░░░░░░▓██░█████  |")
 print("| ██████████░████░██████████ |")
 print("|████████████████████████████|")
 print("|████████████████████████████|")
 print("|████████████████████████████|")
 print("|████████████████████████████|")
 print("'----------------------------'")
 print("Our Military Cannot Defend Itself!")
 print("We Must Improve It!")
 print(f"(1) I'll Increase The Budget.")
 print(f"(2) Our Budget Is Stretched Too Thin.")
 time.sleep(0.25)
 prompt2 = str(input(""))
 if(prompt2 == "1"):
  clear_screen()
  add_bar("mil", 2)
  remove_bar("eco", 1)
 elif(prompt2 == "2"):
  clear_screen()
  add_bar("eco", 1)
  remove_bar("mil", 1)
  remove_bar("gov", 1)
 else:
  clear_screen()
  update_stats()
  return card1_Army1()
def card2_Army2():
 print("")
 print("\033[1m  Secretary General Henry Davis\033")
 print(".----------------------------.")                            
 print("|          ████████          |")     
 print("|         ██████████         |")     
 print("|        ████████████        |")     
 print("|        ████████████        |")                      
 print("|         ██████████         |")     
 print("|          ████████          |")     
 print("|          ████████          |")     
 print("|      ███   ████   ███      |")     
 print("|  ████████   ██   ████████  |")     
 print("| █████████   ██   █████████ |")     
 print("|███████████  ██  ███████████|")     
 print("|███████████ ████ ███████████|")     
 print("|████████████████████████████|")     
 print("|████████████████████████████|")  
 print("'----------------------------'")
 print("The Airforce Needs Faster Planes!")
 print("Divert More Funding To R&D!")
 print(f"(1) I'll See What I Can Do.")
 print(f"(2) Sorry, We're Short On Money.")
 time.sleep(0.25)
 prompt2 = str(input(""))
 if(prompt2 == "1"):
  clear_screen()
  add_bar("mil", 1)
  remove_bar("eco", 2)
  remove_bar("plant", 1)
 elif(prompt2 == "2"):
  clear_screen()
  add_bar("eco", 2)
  remove_bar("mil", 2)
  remove_bar("gov", 1)
 else:
  clear_screen()
  update_stats()
  return card2_Army2()                 
def card3_Army3():
 print("")
 print("\033[1m R&D Director Oliver Wilson\033")
 print(".----------------------------.")
 print("|          ████████          |")     
 print("|         ██████████         |")     
 print("|        ██░░░██░░░██        |")     
 print("|        ████████████        |")                      
 print("|         ██████████         |")         
 print("|          ████████          |")     
 print("|      ████  ████  ████      |")     
 print("|  ████████   ██   ████████  |")     
 print("| ██████████  ██  ██████████ |")     
 print("| ██████████  ██  ██████████ |")     
 print("| ██████████████████████████ |")     
 print("| ██████████████████████████ |")     
 print("| ██████████████████████████ |")
 print("'----------------------------'")
 print("The R&D Department Wants To Build More Facilities!")
 print("Please Allocate Funding For New Infrastructure.")
 print(f"(1) I'll Allocate Some Funds.")
 print(f"(2) Sorry, We Don't Have The Funds At The Moment.")
 time.sleep(0.25)
 prompt2 = str(input(""))
 if(prompt2 == "1"):
  clear_screen()
  add_bar("mil", 2)
  remove_bar("eco", 3)
  remove_bar("plant", 1)
 elif(prompt2 == "2"):
  clear_screen()
  add_bar("eco", 1)
  remove_bar("mil", 1)
  remove_bar("gov", 1)
 else:
  clear_screen()
  update_stats()
  return card3_Army3()     
def card4_Govern1():
 print("")
 print("\033[1m Southern Leader Elijah Miller\033")
 print(".----------------------------.")
 print("|          ▓▓▓▓▓▓▓           |")
 print("|         ▓▓▓▓▓▓▓▓▓▓         |")
 print("|        ▓▓▓▓███████▓        |")
 print("|         ██████████         |")
 print("|         ██████████         |")
 print("|          ████████          |")
 print("|     ██████ ████ ██████     |") 
 print("|   ████████  ██  ████████   |")
 print("|  █████████  ██  █████████  |")
 print("|  ██████████ ██ ██████████  |")
 print("|  ████████████████████████  |")
 print("|  ████████████████████████  |")
 print("|  ████████████████████████  |")
 print("|  ████████████████████████  |")
 print("'----------------------------'")
 print("The People In The South Are Starving!")
 print("We Need Food!")
 print(f"(1) I'll Divert Resources Immediately.")
 print(f"(2) Sorry, We Are In The Same Position.")
 time.sleep(0.25)
 prompt2 = str(input(""))
 if(prompt2 == "1"):
  clear_screen()
  add_bar("gov", 2)
  add_bar("eco", 1)
  remove_bar("plant", 2)
 elif(prompt2 == "2"):
  clear_screen()
  add_bar("eco", 3)
  remove_bar("gov", 2)
 else:
  clear_screen()
  update_stats()
  return card4_Govern1()     
def card5_Govern2():
 print("")
 print("\033[1m Northern Leader Daniel Davis\033")
 print(".----------------------------.")
 print("|          ▓▓▓▓▓▓▓           |")
 print("|         ▓▓▓▓▓▓▓▓▓▓         |")
 print("|        ▓▓▓▓███▓▓▓▓▓        |")
 print("|         ██████████         |")
 print("|         ███▓▓▓▓███         |")
 print("|          ████████          |")
 print("|     ██████ ████ ██████     |") 
 print("|   ████████  ██  ███████    |")
 print("|   ████████  ██  ████████   |")
 print("|   █████████ ██ █████████   |")
 print("|   ██████████████████████   |")
 print("|   ██████████████████████   |")
 print("|   ██████████████████████   |")
 print("|   ██████████████████████   |")
 print("'----------------------------'")
 print("The North Autonomous Zone Lacks Schools!")
 print("Please Allocate Funding For New Infrastructure.")
 print(f"(1) I'll Allocate Some Funds.")
 print(f"(2) Sorry, We Don't Have The Funds At The Moment.")
 time.sleep(0.25)
 prompt2 = str(input(""))
 if(prompt2 == "1"):
  clear_screen()
  add_bar("gov", 2)
  remove_bar("eco", 2)
  remove_bar("plant", 1)
 elif(prompt2 == "2"):
  clear_screen()
  add_bar("eco", 2)
  remove_bar("gov", 2)
 else:
  clear_screen()
  update_stats()
  return card5_Govern2()     
def card6_Govern3():
 print("")
 print("\033[1m Advisor Theodore Brown\033")
 print(".----------------------------.")
 print("|          ▓▓▓▓▓▓▓           |")
 print("|         ▓▓▓▓▓▓▓▓▓▓         |")
 print("|        ▓▓▓▓██▓▓▓▓█▓        |")
 print("|         ██████████         |")
 print("|         ███▓▓▓▓███         |")
 print("|          █▓▓▓▓▓▓█          |")
 print("|     ██████ ████ ██████     |") 
 print("|   ████████  ██  ████████   |")
 print("|  █████████  ██  █████████  |")
 print("|  ██████████ ██ ██████████  |")
 print("|  ████████████████████████  |")
 print("|  ████████████████████████  |")
 print("|  ████████████████████████  |")
 print("|  ████████████████████████  |")
 print("'----------------------------'")
 print("The Government Is Heavily Corrupt!")
 print("We Need To Reform The Government Now!")
 print(f"(1) Reform The Government.")
 print(f"(2) Sorry, This Isn't The Right Time.")
 time.sleep(0.25)
 prompt2 = str(input(""))
 if(prompt2 == "1"):
  clear_screen()
  add_bar("eco", 1)
  remove_bar("gov", 2)
  remove_bar("mil", 1)
 elif(prompt2 == "2"):
  clear_screen()
  add_bar("mil", 1)
  add_bar("gov", 1)
  remove_bar("eco", 2)
 else:
  clear_screen()
  update_stats()
  return card6_Govern3()     
def card7_Economy1():
 print("")
 print("\033[1m Economic Director William Wilson033")
 print(".----------------------------.")
 print("|          ▓▓▓▓▓▓▓           |")
 print("|         ▓▓▓▓▓▓▓▓▓▓         |")
 print("|        ▓▓▓▓███████▓        |")
 print("|         ██████████         |")
 print("|         ██████████         |")
 print("|          ████████          |")
 print("|       ████ ████ ████       |") 
 print("|     ███████ ██ ███████     |")
 print("|    ████████████████████    |")
 print("|    ████████████████████    |")
 print("|    ████████████████████    |")
 print("|    ████████████████████    |")
 print("|    ████████████████████    |")
 print("|    ████████████████████    |")
 print("'----------------------------'")
 print("The Government Is Drowning In Debt!")
 print("We Need To Cut Funding To Some Programs.")
 print(f"(1) I'll See What I Can Do.")
 print(f"(2) Sorry, There Are No Programs We Can Cut At The Moment.")
 time.sleep(0.25)
 prompt2 = str(input(""))
 if(prompt2 == "1"):
  clear_screen()
  add_bar("eco", 2)
  remove_bar("gov", 2)
  remove_bar("plant", 1)
  remove_bar("mil", 1)
 elif(prompt2 == "2"):
  clear_screen()
  add_bar("gov", 2)
  add_bar("mil", 1)
  remove_bar("eco", 2)
 else:
  clear_screen()
  update_stats()
  return card7_Economy1()     
def card8_Economy2():
 print("")
 print("\033[1m Secretary To Head Of Economics Noah Johnson\033")
 print(".----------------------------.")
 print("|          ████████          |")
 print("|         ██████████         |")
 print("|         ██████████         |")
 print("|         ██████████         |")
 print("|          ████████          |")
 print("|       ████ ████ ████       |") 
 print("|     ███████ ██ ███████     |")
 print("|    ████████ ██ ████████    |")
 print("|    ████████████████████    |")
 print("|    ████████████████████    |")
 print("|    ████████████████████    |")
 print("|    ████████████████████    |")
 print("|    ████████████████████    |")
 print("'----------------------------'")
 print("The Stock Market Is In Free Fall!")
 print("Please Allocate Funds To Stabilize The Economy.")
 print(f"(1) I'll Get The Funds As Soon As Possible.")
 print(f"(2) Sorry, We Don't Have The Funds At The Moment.")
 time.sleep(0.25)
 prompt2 = str(input(""))
 if(prompt2 == "1"):
  clear_screen()
  add_bar("eco", 2)
  add_bar("mil", 1)
  remove_bar("gov", 1)
 elif(prompt2 == "2"):
  clear_screen()
  remove_bar("eco", 3)
  remove_bar("gov", 1)
  remove_bar("plant", 1)
  remove_bar("mil", 1)
 else:
  clear_screen()
  update_stats()
  return card8_Economy2()     
def card9_Economy3():
 print("")
 print("\033[1m Trade Secretary Daniel Anderson\033")
 print(".----------------------------.")
 print("|          ████████          |")
 print("|         ██████████         |")
 print("|         ██████████         |")
 print("|         ██░░░░░░██         |")
 print("|          ████████          |")
 print("|     ██████  ██  ██████     |") 
 print("|   █████████ ██ █████████   |")
 print("|  ████████████████████████  |")
 print("|  ████████████████████████  |")
 print("|  ████████████████████████  |")
 print("|  ████████████████████████  |")
 print("|  ████████████████████████  |")
 print("|  ████████████████████████  |")
 print("'----------------------------'")
 print("Our Economy Needs A Boost!")
 print("Please Allow Trade Deals With Other Nations!")
 print(f"(1) I'll Allow Trade To These Nations.")
 print(f"(2) We Don't Negotiate With The Enemy.")
 time.sleep(0.25)
 prompt2 = str(input(""))
 if(prompt2 == "1"):
  clear_screen()
  add_bar("eco", 3)
  add_bar("mil", 1)
  remove_bar("gov", 2)
 elif(prompt2 == "2"):
  clear_screen()
  add_bar("gov", 1)
  remove_bar("mil", 2)
  remove_bar("eco", 1)
 else:
  clear_screen()
  update_stats()
  return card9_Economy3()     
def card10_Nature1():
 print("")
 print("\033[1m Nature R&D Director Lucas Garcia\033")
 print(".----------------------------.")
 print("|          ████████          |")     
 print("|         ██████████         |")     
 print("|        ████████████        |")     
 print("|        ████████████        |")                      
 print("|         ██████████         |")         
 print("|          ████████          |")
 print("|     ██████  ██  ██████     |") 
 print("|   █████████ ██ █████████   |")
 print("|  ████████████████████████  |")
 print("|  ████████████████████████  |")
 print("|  ████████████████████████  |")
 print("|  ████████████████████████  |")
 print("|  ████████████████████████  |")
 print("|  ████████████████████████  |")     
 print("'----------------------------'")
 print("The R&D Department Wants To Gain Access To Exotic Materials!")
 print("Please Allow The Purchase Of These Materials.")
 print(f"(1) I'll Allow The Purchase.")
 print(f"(2) Sorry, We Don't Have The Funds At The Moment.")
 time.sleep(0.25)
 prompt2 = str(input(""))
 if(prompt2 == "1"):
  clear_screen()
  add_bar("plant", 2)
  add_bar("gov", 1)
  remove_bar("eco", 2)
 elif(prompt2 == "2"):
  clear_screen()
  add_bar("eco", 1)
  remove_bar("plant", 2)
  remove_bar("gov", 1)
 else:
  clear_screen()
  update_stats()
  return card10_Nature1()     
def card11_Nature2():
 print("")
 print("\033[1m Scientific Director Michael Taylor\033")
 print(".----------------------------.")
 print("|          ████████          |")
 print("|         █░░░██░░░█         |")
 print("|         ██████████         |")
 print("|         ██░░░░░░██         |")
 print("|          ████████          |")
 print("|     ██████ ████ ██████     |") 
 print("|   ████████  ██  ████████   |")
 print("|  █████████  ██  █████████  |")
 print("|  ██████████ ██ ██████████  |")
 print("|  ████████████████████████  |")
 print("|  ████████████████████████  |")
 print("|  ████████████████████████  |")
 print("|  ████████████████████████  |")
 print("'----------------------------'")
 print("Our Scientists Discovered A New Super Virus!")
 print("We Need To Build A Containment Facility Immediately!")
 print(f"(1) Build It Immediately.")
 print(f"(2) We Should Be Fine.")
 time.sleep(0.25)
 prompt2 = str(input(""))
 if(prompt2 == "1"):
  clear_screen()
  add_bar("plant", 3)
  add_bar("gov", 1)
  remove_bar("eco", 2)
 elif(prompt2 == "2"):
  clear_screen()
  cardsp_deathbyplant()
  False
 else:
  clear_screen()
  update_stats()
  return card11_Nature2()     
def card12_Nature3():
 print("")
 print("\033[1m Head Scientist Mateo Smith\033")
 print(".----------------------------.")
 print("|          ▓▓▓▓▓▓▓           |")
 print("|         ▓▓▓▓▓▓▓▓▓▓         |")
 print("|        ▓▓▓▓███████▓        |")
 print("|         ██████████         |")
 print("|         ▓▓▓▓▓▓▓▓▓▓         |")
 print("|          ▓▓▓▓▓▓▓▓          |")
 print("|     ██████ ████ ██████     |") 
 print("|   ████████  ██  ████████   |")
 print("|  █████████  ██  █████████  |")
 print("|  ██████████ ██ ██████████  |")
 print("|  ████████████████████████  |")
 print("|  ████████████████████████  |")
 print("|  ████████████████████████  |")
 print("|  ████████████████████████  |")
 print("'----------------------------'")
 print("We've Created A Modified Plant That Could Feed The Entire Population!")
 print("We Need More Funding To Expand Our Operations.")
 print(f"(1) I'll Increase Your Funding.")
 print(f"(2) Sorry, We Can't Allocate Any Funds.")
 time.sleep(0.25)
 prompt2 = str(input(""))
 if(prompt2 == "1"):
  clear_screen()
  add_bar("plant", 2)
  add_bar("gov", 1)
  remove_bar("eco", 2)
 elif(prompt2 == "2"):
  clear_screen()
  add_bar("eco", 2)
  remove_bar("gov", 2)
  remove_bar("plant", 1)
 else:
  clear_screen()
  update_stats()
  return card12_Nature3()    
def cardsp_deathbymil():
 print("")
 print(".----------------------------.")    
 print("|            ████            |")
 print("|         ██████████         |") 
 print("|       ██████████████       |") 
 print("|       ██████████████       |") 
 print("|       ██    ██    ██       |") 
 print("|       ▒██ ░████░ ███       |") 
 print("|         ████  ████         |") 
 print("|         █ ▓████▓ █         |") 
 print("|    ██    ██▓  ▒██    ███   |") 
 print("|   ░████   ██████   ████    |") 
 print("|   ████████░    ▒████████   |") 
 print("|           ▒████░           |") 
 print("|   █████████    ████████▒   |") 
 print("|    ███▒            █████   |") 
 print("|    █▒                ██    |")
 print("'----------------------------'")
 print("The Military Becomes Unable To Defend Itself.")
 time.sleep(1)
 print("Rival Nations Invade Your Country And You Are Executed Shortly After.")
 time.sleep(1)
 print("Ending 1/4:","\033[32mMilitary Invasion\033[0m")
def cardsp_deathbygovern():
 print("")
 print(".----------------------------.")     
 print("|              ▓▓            |") 
 print("|              ▒             |") 
 print("|           ▒▒  ▒▒▒▒         |") 
 print("|        ▒▒▒▒▒▒▒▒▒▒▒▒▒▒      |") 
 print("|      ▒▒█▒██▒██▒██▒█▒▓      |") 
 print("|   ▒▒▒▒ █ ██ ██ ██ █▒▒▒▒▒▒  |") 
 print("|   █▒▓█ █ █▒ █▓ ▒█ █▒█▓█▓   |") 
 print("|   ▒▒▒▒ ▒ ▒▒ ▒▒ ▒▒ ▓▒▓▓▓▓   |") 
 print("|   █▒▓█ █ █▒ █▓ ▒█ █▒█▓█▓   |") 
 print("|   ▒▒▒▒       ▒▒  ▒ ▒▓▓▓▓   |") 
 print("|  ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓  |") 
 print("|  ▒▒▒▒▒▒▒▒▒▒▒▒████████████  |")
 print("'----------------------------'")
 print("Becoming Wildly Unpopular, You Are Deposed.")
 time.sleep(1)
 print("You Are Then Executed By The Government For Treason.")
 time.sleep(1)
 print("Ending 2/4:","\033[34mGovernment Coup\033[0m")
def cardsp_deathbyeco():
 print("")
 print(".----------------------------.")            
 print("|    ▓▓▓▓▓░                  |") 
 print("|         ▓▓▓▓▓░             |") 
 print("|    ▓▒▒▒      ▓▓            |") 
 print("|    ▓▒▒▒ ▒▒▒   ▓▓▓▓▓▓       |") 
 print("|    ▒▒▒▒ ▒▒▒ ▒▒▒     ▓▓     |") 
 print("|    ▒▒▒▒ ▒▒▒ ▒▒▒ ▒▒▒  ░▓▓   |") 
 print("|    ▒▒▒▒ ▒▒▒ ▒▒▒ ▒▒▒░  ░▓   |") 
 print("|    ▒▒▒▒ ▒▒▒ ▒▒▒ ▒▒▒░       |") 
 print("|    ▓▓███████████████████   |")       
 print("'----------------------------'")
 print("With The Economy Unchecked, It Crashes.")
 time.sleep(1)
 print("As The Nation Falls Apart, You Are Caught In The Crossfire And Die.")
 time.sleep(1)
 print("Ending 3/4:","\033[38;2;0;255;0mEconomic Collapse\033[0m")
def cardsp_deathbyplant():
 print("")
 print(".----------------------------.")
 print("|░░ ░░  ░  ░░ ░░  ░  ░░ ░░  ░|")  
 print("|░░ ░░  ░  ░░ ░░██████░ ░░  ░|")  
 print("| ░  ░░ ░░  ░ █░░ ░░█░░  ░░ ░|")
 print("|░ ░░  ░  ░░ █▒  ░  █░ ░░  ░ |") 
 print("|░ ░░  ░  ░░██░  ░ ██░ ░░  ░ |") 
 print("| ░  ░░ ░░ █░█ ░░ ░░█ ░  ░░ ░|")
 print("| ░  ░░ ░░  ░█ ░░ ░████  ░░ ░|")
 print("|░ ░░  ░  ░░ ███ ░ ██▓█░░  ░ |") 
 print("| ░  ░░ ░░  ░ █▓░  ██ ░  ░░ ░|")
 print("| ░  ░░ ░░  ░ █░░ ░░  ░  ░░ ░|")
 print("|░ ░░  ░  ░░▒████░  ░░ ░░  ░ |")
 print("| ░  ░░ ░███████████  ░  ░░ ░|")
 print("| ░  ░░ ░░  ░  ░░ ░░  ░  ░░ ░|")
 print("'----------------------------'")
 print("With No Regulations On The Environment, The Country Soon Becomes A Wasteland.")
 time.sleep(1)
 print("You Starve To Death As The World Around You Is Permanently Contaminated.")
 time.sleep(1)
 print("Ending 4/4:","\033[91mContaminated World\033[0m")
#-----------------------
#stability stats
#-----------------------
def stability_stats():
  global stats
  stats = {
    "🪖": -3,
    "🏛️": -3,
    "📈": -3,
    "🌱": -3
  }
def remove_bar(bar_type,bar_amount):
 if(bar_type == "mil" and bar_amount == 1):
  stats["🪖"] += 1
 elif(bar_type == "mil" and bar_amount == 2):
  stats["🪖"] += 2
 elif(bar_type == "mil" and bar_amount == 3):
  stats["🪖"] += 3
 elif(bar_type == "gov" and bar_amount == 1):
  stats["🏛️"] += 1
 elif(bar_type == "gov" and bar_amount == 2):
  stats["🏛️"] += 2
 elif(bar_type == "gov" and bar_amount == 3):
  stats["🏛️"] += 3
 elif(bar_type == "eco" and bar_amount == 1):
  stats["📈"] += 1
 elif(bar_type == "eco" and bar_amount == 2):
  stats["📈"] += 2
 elif(bar_type == "eco" and bar_amount == 3):
  stats["📈"] += 3
 elif(bar_type == "plant" and bar_amount == 1):
  stats["🌱"] += 1
 elif(bar_type == "plant" and bar_amount == 2):
  stats["🌱"] += 2
 elif(bar_type == "plant" and bar_amount == 3):
  stats["🌱"] += 3
def add_bar(bar_type,bar_amount):
  if(bar_type == "mil" and bar_amount == 1):
   stats["🪖"] -= 1
   if(stats["🪖"] <= -3):
    stats["🪖"] = -3
  elif(bar_type == "mil" and bar_amount == 2):
   stats["🪖"] -= 2
   if(stats["🪖"] <= -3):
    stats["🪖"] = -3
  elif(bar_type == "mil" and bar_amount == 3):
   stats["🪖"] -= 3
   if(stats["🪖"] <= -3):
    stats["🪖"] = -3
  elif(bar_type == "gov" and bar_amount == 1):
   stats["🏛️"] -= 1
   if(stats["🏛️"] <= -3):
    stats["🏛️"] = -3
  elif(bar_type == "gov" and bar_amount == 2):
    stats["🏛️"] -= 2     
    if(stats["🏛️"] <= -3):
     stats["🏛️"] = -3
  elif(bar_type == "gov" and bar_amount == 3):
   stats["🏛️"] -= 3
   if(stats["🏛️"] <= -3):
    stats["🏛️"] = -3
  elif(bar_type == "eco" and bar_amount == 1):
   stats["📈"] -= 1
   if(stats["📈"] <= -3):
    stats["📈"] = -3
  elif(bar_type == "eco" and bar_amount == 2):
   stats["📈"] -= 2
   if(stats["📈"] <= -3):
    stats["📈"] = -3
  elif(bar_type == "eco" and bar_amount == 3):
   stats["📈"] -= 3
   if(stats["📈"] <= -3):
    stats["📈"] = -3
  elif(bar_type == "plant" and bar_amount == 1):
   stats["🌱"] -= 1
   if(stats["🌱"] <= -3):
    stats["🌱"] = -3
  elif(bar_type == "plant" and bar_amount == 2):
   stats["🌱"] -= 2
   if(stats["🌱"] <= -3):
    stats["🌱"] = -3
  elif(bar_type == "plant" and bar_amount == 3):
   stats["🌱"] -= 3
   if(stats["🌱"] <= -3):
    stats["🌱"] = -3
#-----------------------
def update_stats():
 for stat_name in stats:
   print(" ",stat_name, end="    ")  
 for i in range(6):
  print("")
  for stat_name in stats:
    if i > stats[stat_name]:
      print("|████|", end="  ")
    else:
      print("|    |", end="  ")
#-----------------------
#card_shuffler
#-----------------------
def card_shuffler():
  card_randomizer = randint(1, 100)
  precise_shuffler = randint(1,3)
  if card_randomizer <= 25:
   if(precise_shuffler == 1):
    card1_Army1()
   elif(precise_shuffler == 2):
    card2_Army2()
   elif(precise_shuffler == 3):
    card3_Army3()
  elif card_randomizer <= 50:
   if(precise_shuffler == 1):
    card4_Govern1()
   elif(precise_shuffler == 2):
    card5_Govern2()
   elif(precise_shuffler == 3):
    card6_Govern3()
  elif card_randomizer <= 75:
   if(precise_shuffler == 1):
    card7_Economy1()
   elif(precise_shuffler == 2):
    card8_Economy2()
   elif(precise_shuffler == 3):
    card9_Economy3()
  elif card_randomizer <= 100:
   if(precise_shuffler == 1):
    card10_Nature1()
   elif(precise_shuffler == 2):
    card11_Nature2()
   elif(precise_shuffler == 3):
    card12_Nature3()
#-----------------------
title()
stability_stats()
while True:
  update_stats()
  card_shuffler()
  if(stats["🪖"] == 5):
   cardsp_deathbymil()
   break
   False
  elif(stats["🏛️"] == 5):
   cardsp_deathbygovern()
   break
   False
  elif(stats["📈"] == 5):
   cardsp_deathbyeco()
   break
   False
  elif(stats["🌱"] == 5):
   cardsp_deathbyplant()
   break
   False
