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
            print("You selected saved trips")
        if selection == "3":
            print("You selected point values")
        if selection == "4":
            print("You selected quit")
        
mainMenu()