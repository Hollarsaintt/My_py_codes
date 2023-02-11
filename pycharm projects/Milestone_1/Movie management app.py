"""
- Enter "a" to add movie, "l" to see movie, "f" to find movie and "q" to quit:

- add movie
- see movies
- find movie
- stop running the program

Task:
[]: movies storage structure
[]: format of a movie
[]: show user a menu, ask for their input
[]: allow user to add movie
[]: see all movies existing in their database
[]: find a movie
[]: allow user to stop the program

"""


def menu():
    user_input = input('Enter "a" to add a movie, "l" to see your movies, "f" to find a movie and "q" to quit: ')

    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            see_movie()
        elif user_input == 'f':
            find_movie()
        else:
            print('UNKNOWN COMMAND! - PLEASE TRY AGAIN!')

        user_input = input('Enter "a" to add a movie, "l" to see your movies, "f" to find a movie and "q" to quit: ')
    else:
        print('stopping program...\nEXIT SUCESSFULLY')