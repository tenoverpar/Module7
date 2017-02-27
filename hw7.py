"""'
    Tracy Allen - Homework assignment #7
    March 2,2017


    1) Finish walking through this lecture to copy/paste the beginning of the script you will need for your homework. (Links to an external site.)
    2) Finish the user option to delete an entry from the dictionary by removing the "pass" statements and adding code to delete a user by name (extra challenge: can you figure out how to delete a user by name OR username?)
    3) Finish the user option to lookup a username by name by removing the "pass" statement and adding code to find a user by name
    4) Run the script and make sure each option works
    5) Add exception handling to each user input option.
    6) Add doc strings to the script and comment the code.
    7) Push your finished script to your personal, publicly accessible Github repo.
    8) Submit a link to the Github repo containing your script on canvas.


"""

# !/usr/bin/env python3

from sortedcontainers import SortedDict


def print_menu():
    print('1. Print Users')
    print('2. Add a User')
    print('3. Remove a User')
    print('4. Lookup a User Name')
    print('5. Quit')
    print()


# Create dictionary with key = Names, value = user_name
usernames = SortedDict()
usernames['Summer'] = 'summerela'
usernames['William'] = 'GoofyFish'
usernames['Steven'] = 'LoLCat'
usernames['Zara'] = 'zanyZara'
usernames['Renato'] = 'songDude'

# print(usernames)

# setup counter to store menu choice
menu_choice = 0

# display your menu
print_menu()

# as long as the menu choice isn't "quit" get user options
while menu_choice != 5:
    # get menu choice from user
    # Making sure a whole number is entered
    try:
        menu_choice = int(input("Type in a number (1-5): "))
    except ValueError:
        print("This should be a whole number")

    # view current entries
    if menu_choice == 1:
        print("Current Users:")
        for x, y in usernames.items():
            print("Name: {} \tUser Name: {} \n".format(x, y))

    # add an entry
    elif menu_choice == 2:
        print("Add User")
        # Add new name and force capitalization
        name = input("Name: ").capitalize()
        username = input("User Name: ")
        usernames[name] = username

    # remove an entry
    elif menu_choice == 3:
        # What are we doing here
        print("Remove User")
        # Want to remove the dictionary item
        name = input("Name: ")
        if name in usernames:
            del usernames[name]
            print("\nOkay, I deteted", name)
        else:
            print("\nI can't do that!", name, "doesn't exits in the dictionary.")

    # view user name
    elif menu_choice == 4:
        print("Lookup User")
        name = input("Name: ")
        if name in usernames:
            print(usernames[name])
        else:
            print(name, "User is not found")

    # Add some logic to catch numbers out of range
    elif menu_choice <= 0 or menu_choice >= 6:
        print("Enter number between 1 and 5")
    # is user enters something strange, show them the menu

    elif menu_choice != 5:
        print_menu()


