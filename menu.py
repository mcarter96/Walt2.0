def mainMenu():
    selection = 1
    print("""
***Main Menu***
1. Play Game
2. Saved Trips
3. Point Value of Rides
4. Quit""")
    while selection != "4":
        selection = input("Please select a choice: ")
        if selection == "1":
            print("You selected play game")
        if selection == "2":
            savedTrips()
        if selection == "3":
            pointValues()
        if selection == "4":
            print("Thanks for playing!")

def pointValues():
    print("""
    Alien Swirling Saucers      1 pt
    Avatar Flight of Passage    2 pts
    DINOSAUR                    3 pts
    Expedition Everest          4 pts
    Kilimanjaro Safari          5 pts
    Na'vi River Journey         6 pts
    Pirates of the Caribbean    7 pts
    Rock 'n' Roller Coaster     8 pts
    Seven Dwarfs Mine Train     9 pts
    Slinky Dog Dash             10 pts
    Soarin'                     11 pts
    Spaceship Earth             12 pts
    Splash Mountain             13 pts
    Toy Story Mania             14 pts
    """)

def savedTrips():
    # Read from a file(?) 
    # Arraylist
    # csv file
    print("saved trips")
        
mainMenu()