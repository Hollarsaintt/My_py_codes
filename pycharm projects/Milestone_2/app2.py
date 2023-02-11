#Books management system
#should be able to list read and unread books.
from utils import database2 as d
USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all book
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit 
Your choice: """



def menu(): #will get the user's choice and call the necessay function that will perform the action.
    user_input = input(USER_CHOICE)
    while user_input.lower() != 'q':
        if user_input.lower() == 'a':
            d.add_book()
        elif user_input.lower() == 'l':
            d.list_book()
        elif user_input.lower() == 'r':
            d.mark_as_read()
        elif user_input.lower() == 'd':
            d.remove_book()
        else:
            print('\nINVALID RESPONSE: kindly follow the guide.')
        user_input = input(USER_CHOICE)

    else:
        exit_app()


def exit_app():
    choice = input('\nAre you sure you want to exit? Y/N: ')
    while choice.lower() != 'y' and choice.lower() != 'n': choice = input('Are you sure you want to exit? Y/N: ')
    if choice.lower() == 'n': menu()
    else: print('\nExiting...\nExited sucessfully!')

menu()