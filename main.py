import os, random, time
os.system("clear")
print("Rock, Paper, Scissors Battle 🪨 📃 ✂️")
print()

def home():
  print("Game Mode: \n 1. 👤 Play With Friend \n 2. 💻 Play With Computer")
  mode = input("Choose your game mode: ")
  os.system("clear")
  if mode == "1":
    Mfriend()
  elif mode =="2":
    Mcomp()


def Mfriend():
  print("Select your move (R, P or S) : ")
  print()

  player1Move = input("Player 1 > ")
  os.system("clear")
  player2Move = input("Player 2 > ")
  os.system("clear")
  print()

  if player1Move=="R":
    if player2Move=="R":
      print("You both picked Rock, draw!")
    elif player2Move=="S":
      print("Player1 smashed Player2's Scissors into dust with their Rock!")
    elif player2Move=="P":
      print("Player1's Rock is smothered by Player2's Paper!")
    else:
      print("Invalid Move Player 2!")                
  elif player1Move=="P":
    if player2Move=="R":
      print("Player2's Rock is smothered by Player1's Paper!")
    elif player2Move=="S":
      print("Player1's Paper is cut into tiny pieces by Player2's Scissors!")
    elif player2Move=="P":
      print("Two bits of paper flap at each other. Dissapointing. Draw.")
    else:
      print("Invalid Move Player 2!")
  elif player1Move=="S":
      if player2Move=="R":
        print("Player 2's Rock makes metal-dust out of Player1's Scissors")
      elif player2Move=="S":
        print("Ka-Shing! Scissors bounce off each other like a dodgy sword fight! Draw.")
      elif player2Move=="P":
        print("Player1's Scissors make confetti out of Player2's paper!")
      else:
        print("Invalid Move Player 2!")
  else:
    print("Invalid Move Player 1!")
  
  print()
  time.sleep(2)
  os.system("clear")
  home()

def Mcomp():
  print("Select your move (R, P or S) : ")
  player1Move = input("> ")
  com = random.randint(1, 3)
  if com == 1:
    player2Move = "R"
  elif com == 2:
    player2Move = "P"
  else:
    player2Move = "S"
  time.sleep(2)
  if player1Move=="R":
    if player2Move=="R":
       print("You both picked Rock, draw!")
    elif player2Move=="S":
       print("Player1 smashed Player2's Scissors into dust with their Rock!")
    elif player2Move=="P":
       print("Player1's Rock is smothered by Player2's Paper!")
    else:
       print("Invalid Move Player 2!")                
  elif player1Move=="P":
    if player2Move=="R":
       print("Player2's Rock is smothered by Player1's Paper!")
    elif player2Move=="S":
       print("Player1's Paper is cut into tiny pieces by Player2's Scissors!")
    elif player2Move=="P":
       print("Two bits of paper flap at each other. Dissapointing. Draw.")
    else:
      print("Invalid Move Player 2!")
  elif player1Move=="S":
    if player2Move=="R":
      print("Player 2's Rock makes metal-dust out of Player1's Scissors")
    elif player2Move=="S":
      print("Ka-Shing! Scissors bounce off each other like a dodgy sword fight! Draw.")
    elif player2Move=="P":
      print("Player1's Scissors make confetti out of Player2's paper!")
    else:
      print("Invalid Move Player 2!")
  else:
    print("Invalid Move Player 1!")

  time.sleep(2)
  os.system("clear")
  home()

home()                                                                                                                                                                                                      