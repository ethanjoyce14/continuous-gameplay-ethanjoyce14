# Ethan Joyce
# Ms. Cotcher
# CS 30
# Period 1
# RPG Continuous Gameplay


# Lists for all menus, directions and actions
main_menu = ['Move', 'Explore', 'Inventory']
movement = ['North', 'South', 'East', 'West']
inventory = ['Attack', 'Defense', 'Restore']
attack = ['Bronze Sword', 'Iron Axe']
defense = ['Mail Tunic', 'Leather Pants', 'Iron Helmet', 'Wooden Roundshield']
restore = ['Bread', 'Apple', 'Health Potion']


def startup():
    """
    A guide to the program which runs at startup
    """
    print(
        '''
All menus within this program link up with one another. To access anything
within the menu, type it in lowercase. At any time, the user may type 'quit'
to exit the program. To back out of a menu, 'back' may be typed.
        '''
            )


def main():
    """
    A primary menu for all available actions
    """
    print("\nMain Menu:\n")

    # Items in the main menu printed with a loop
    for menu in main_menu:
        print(f"\t{menu}\n")

    # Input options to access different menus
    response = ""
    response = input("Which menu would you like to access?\n")
    if response == 'move':
        move()
    elif response == 'explore':
        print("\nNothing interesting here!")
        main()
    elif response == 'inventory':
        inv()
    elif response == 'quit':
        quit()
    else:
        print("I didn't understand that!")
        main()


def move():
    """
    Movement options
    """
    print("\nMovement Menu:\n")

    # Movement directons printed with a loop
    for direction in movement:
        print(f"\t{direction}\n")

    # Prompt and inputs for movement
    response = input("Which direction would you like to travel?\n")
    if response == 'north':
        print("\nYou head north.")
        main()
    elif response == 'south':
        print("\nYou head south.")
        main()
    elif response == 'east':
        print("\nYou head east.")
        main()
    elif response == 'west':
        print("\nYou head west.")
        main()
    elif response == 'back':
        main()
    elif response == 'quit':
        quit()
    else:
        print("\nI didn't understand that!")
        move()


def inv():
    """
    Inventory items within multiple menus
    """
    print("\nInventories:\n")

    # Inventory subcategories printed with a loop
    for invmenus in inventory:
        print(f"\t{invmenus}\n")

    # Prompt and inputs for inventory subcategories
    response = input("Which inventory would you like to access?\n")
    if response == 'attack':
        atk()
    elif response == 'defense':
        dfns()
    elif response == 'restore':
        rstr()
    elif response == 'back':
        main()
    elif response == 'quit':
        quit()
    else:
        print("\nI didn't understand that!")
        inv()


def atk():
    """
    All attack items within inventory are grouped here
    """
    print(f"\nAttack ({len(attack)} items):\n")

    # Items printed with a loop
    for weapon in attack:
        print(f"\t{weapon}\n")

    # Prompt and input to back out of inventory
    response = input("Type 'back' to return to Inventories.\n")
    if response == 'back':
        inv()
    elif response == 'quit':
        quit()
    else:
        print("\nI didn't understand that!")
        atk()


def dfns():
    """
    All defense items within inventory are grouped here
    """

    # Items printed with a loop
    print(f"\nDefense ({len(defense)} items):\n")
    for item in defense:
        print(f"\t{item}\n")

    # Prompt and input to back out of inventory
    response = input("Type 'back' to return to Inventories.\n")
    if response == 'back':
        inv()
    elif response == 'quit':
        quit()
    else:
        print("\nI didn't understand that!")
        dfns()


def rstr():
    """
    All restore items within inventory are grouped here
    """
    print(f"\nRestore ({len(restore)} items):\n")

    # Items printed with a loop
    for consumable in restore:
        print(f"\t{consumable}\n")

    # Prompt and input to back out of inventory
    response = input("Type 'back' to return to Inventories.\n")
    if response == 'back':
        inv()
    elif response == 'quit':
        quit()
    else:
        print("\nI didn't understand that!")
        rstr()


startup()

main()
