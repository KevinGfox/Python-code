import random

def roll_dice():
    DICES = {  
        1: (  
            "┌─────────┐",  
            "│         │",  
            "│    ●    │",  
            "│         │ ",  
            "└─────────┘",  
        ),  
        2: (  
            "┌─────────┐",  
            "│    ●    │",  
            "│         │",  
            "│    ●    │",  
            "└─────────┘",  
        ),  
        3: (  
            "┌─────────┐",  
            "│ ●       │",  
            "│    ●    │",  
            "│       ● │",  
            "└─────────┘",  
         ),  
         4: (  
            "┌─────────┐",  
            "│ ●     ● │",  
            "│         │",  
            "│ ●     ● │",  
            "└─────────┘",  
        ),  
        5: (  
            "┌─────────┐",  
            "│ ●     ● │",  
            "│    ●    │",  
            "│ ●     ● │",  
            "└─────────┘",  
         ),  
        6: (  
            "┌─────────┐",  
            "│ ●     ● │",  
            "│ ●     ● │",  
            "│ ●     ● │",  
            "└─────────┘",  
        ),  
    }  

    roll = input("Roll the dice ? (Y/N): ")

    while roll.lower() == "Y".lower():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print("\n".join(DICES[dice1]))
        print("\n".join(DICES[dice2]))
        print("")
        print("dice rolled: {} and {}". format(dice1, dice2))
        print("")

        roll = input("Roll again? (Y/N)")

roll_dice()