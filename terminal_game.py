import time
import random
import os

def clear():
    os.system('clear')  # On Windows use 'cls'

def slow_scene(lines, delay=0.2, final_pause=2):
    for line in lines:
        print(line)
        time.sleep(delay)
    time.sleep(final_pause)
    clear()

def type_text(text, speed=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(speed)
    print()


def victory_banner():
    print("""
██╗   ██╗██╗ ██████╗████████╗ ██████╗ ██████╗ ██╗   ██╗
██║   ██║██║██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗╚██╗ ██╔╝
██║   ██║██║██║        ██║   ██║   ██║██████╔╝ ╚████╔╝ 
╚██╗ ██╔╝██║██║        ██║   ██║   ██║██╔══██╗  ╚██╔╝  
 ╚████╔╝ ██║╚██████╗   ██║   ╚██████╔╝██║  ██║   ██║   
  ╚═══╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝                                                                       
""")


def gameover_banner():
    print("""
   ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███  
  ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒
 ▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒
 ░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  
 ░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒
  ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░
   ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░
 ░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░ 
       ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░     
                                                      ░ 
""")


def intro_title():
    print("""
    ████████╗██╗  ██╗███████╗     ████████╗██████╗ ██╗ █████╗ ██╗     
    ╚══██╔══╝██║  ██║██╔════╝     ╚══██╔══╝██╔══██╗██║██╔══██╗██║     
       ██║   ███████║█████╗          ██║   ██████╔╝██║███████║██║     
       ██║   ██╔══██║██╔══╝          ██║   ██╔══██═██║██╔══██║██║     
       ██║   ██║  ██║███████╗        ██║   ██║  ██ ██║██║  ██║███████╗
       ██╝   ╚═╝  ╚═╝╚══════╝        ╚═╝   ╚═╝  ██ ╚═╝╚═╝  ╚═╝╚══════╝
        ██                                     ██
         ██ 🌲 WELCOME TO THE FOREST TRIAL 🌲 ██
          ██       Will you survive?         ██
""")
    

slow_scene(intro_title, delay=0.1, final_pause=3)

# --- Get name ---
name = input("\nWhat is your name, adventurer? ")
print(f"\nHello {name}! Your journey begins now...\n")
time.sleep(2)
clear()

# --- Intro scene ---
forest_scene = [
    "   .       .     .  .      +     .      .          .         ",
    "     .       .      .     #       .           .+              ",
    "  .     .      .         ###            .      #.  +    .      ",
    '      .+     .   "#:. .:##"##:. .:#"  .       ###  #"   .      .   ',
    '   .   #   .    +  . "####"###"####"  .#     #######    .    .     ',
    '      ###.     "#:.  #"###"###"#:.    .:#"############     .       ',
    '.   ##""##  ""##"## "#:.  "####"###"####"  .:#" ###   .          . ',
    ' .##"####"###""######"###""##""##""#######"######"###"##"#"   .    ',
    ' #####""####"###"###."##"##### ##"##"##"######"###""#              ',
    '###"#"####""###"###""###""##"#####"###"##"########""###  .      .  ',
    '#####   🌲 You wake up in a dense, misty forest. ######   .  .     ',
    '##"##   🌫️  Shadows twist between ancient trees.  ####""           ',
    '#####   🌑  The cold air chills your bones.    .  ##"## .     .    ',
    '###"#   🔦  Two objects lie nearby, half-buried in leaves...     . ',
]
slow_scene(forest_scene, delay=0.2, final_pause=7)

# --- First choice ---
print("""
--------------------------------      
At your feet, you see two items: 
--------------------------------      
1. A Flickering Torch
2. A Rusty Dagger
""")
item = input("Which one do you pick up? (1 or 2): ")

# --- TORCH PATH ---
if item == "1":
    print(r"""
      /🔥\
    (  🔥  )
      )  (
     (    )
      |  |       🔥 You picked up the torch. The light pushes back the shadows.
      |  |   
     /____\
    """)
    time.sleep(1.75)

    print("""
    -----------------------------------
    Illumination has brought into view:
    -----------------------------------      
    1. A Gloomy Cave
    2. A Winding Forest Trail
    """)
    path = input("Which path do you choose? (1 or 2): ")

    if path == "1":
        print("""
              
              You step into the cave. It’s silent... a bit too silent.
              
              """)
        action = input("Do you approach it? (yes/no): ").lower()

        if action == "yes":
            print("🌅 You crawl to a forest edge and survive. You live to tell the tale!")
            victory_banner()
        else:
            print("You leave the cave... but wander too far into darkness. 🌑 GAME OVER.")
            gameover_banner()

    elif path == "2":
        print("The trail leads to a quiet meadow. You find a cabin and rest safely. 🏡 You win!")
        victory_banner()
    else:
        print("You walk in circles, confused. Night falls. 🌘 GAME OVER.")
        gameover_banner()

# --- DAGGER PATH ---
elif item == "2":
    print(r"""
     /\\
    /  ))     
   ||   ((
   ||   ))
   ||   ((          🗡️ You picked up the dagger. It feels cold in your hand.
   \|___))
    |__| 
    |__|        
    (  )
     ``
""")
    time.sleep(1.75)

    print("""
--------------------          
You see two options:
--------------------          
1. Follow fresh footprints into the brush
2. Head toward distant torchlight
""")
    path = input("Which do you choose? (1 or 2): ")

    if path == "1":
        print("""
              
              You find a wounded wolf. It's growling softly...
              
              """)
        action = input("Do you attack or help it? (attack/help): ").lower()
        if action == "attack":
            print("You stab the wolf. But others nearby hear and surround you. 🐺 GAME OVER.")
            gameover_banner()
        elif action == "help":
            print("You calm the wolf. It bonds with you and leads you to a hidden camp.")
            print("You are protected through the night. 🐺❤️ You win!")
            victory_banner()
        else:
            print("You hesitate. The wolf limps away. You're alone and lost. 🕳️ GAME OVER.")
            gameover_banner()
    elif path == "2":
        print("You reach a flickering light. It’s a bandit camp.")
        action = input("Do you sneak or confront? (sneak/confront): ").lower()

        if action == "sneak" and random.random() > 0.3:
            print("You steal a map and escape into the trees! 📜🏃 You win!")
            victory_banner()
        elif action == "confront":
            print("You charge into the camp, blade ready. But they overpower you. 🗡️ GAME OVER.")
            gameover_banner()
        else:
            print("You’re caught sneaking. Captured. GAME OVER.")
            gameover_banner()
    else:
        print("You trip in the dark and fall into a pit. 🕳️ GAME OVER.")
        gameover_banner()

# --- INVALID INPUT PATH ---
else:
    print("You take too long deciding... The forest swallows you whole. 🌑 GAME OVER.")
    gameover_banner()
