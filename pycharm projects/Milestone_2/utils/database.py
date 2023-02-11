"""
Concerned with Storing and retrieving data from a list
"""
books = [
    {'name': 'lamlad physics', 'author': 'lamlad', 'read': True},
    {'name': 'Independence', 'author': 'jamb', 'read': False},
    {'name': 'sweet sixteen', 'author': 'Not known', 'read': True},
    {'name': 'Invisible teacher', 'author': 'Dele Ashade', 'read': False}
]


def add_book():
    name = input('\nEnter the name of the book: ')
    author = input('Enter the name of the author: ')
    read = input('\nHave you read this book? Y/N: ')
    while read.lower() != 'y' and read.lower() != 'n': read = input('\nHave you read this book? Y/N: ')
    if read.lower() == 'y': read = True
    else: read = False
    if name != '' and author != '':
        book = {'name': name, 'author': author, 'read': read}
        books.append(book)
        print('\nBook sucessfully added!'.upper())
    else:
        print('\nYou have typed nothing!\nNothing is added to my database!')


def list_book():
    user_input = input("\n'a' to list all\n'r' to list read\n'u' to list unread\n\nYOUR CHOICE: ")
    _l = user_input.lower()
    while _l != 'a' and _l != 'r' and _l != 'u':
        print('\nEnter an option in the menu!')
        user_input = input("\n'a' to list all\n'r' to list read\n'u' to list unread\n\nYOUR CHOICE: ")
        _l = user_input.lower()
    else:
        print_book = lambda book: print(f"{book['name']} by {book['author']}\tREAD: {book['read']}")
        if _l == 'a':
            for book in books: print_book(book)
        elif _l == 'r':
            for book in books:
                if book['read'] == True:  print_book(book)
        elif _l == 'u':
            for book in books:
                if book['read'] != True: print_book(book)


def remove_book():
    book_name = input("\nEnter the name of the book: ")
    for book in books:
        if book_name.lower() == book['name'].lower():
            books.remove(book)
            print('\nBOOK SUCESSFULLY REMOVE!')
            break
    else:
        print('\nYou have typed a name not in the database.')


def mark_as_read():
    book_name = input("\nEnter the name of the book: ")
    for book in books:
        if book_name.lower() == book['name'].lower():
            book['read'] = True
            print('\nBOOK SUCESSFULLY MARK AS READ!')
            break
    else:
        print('\nYou have typed a name not in the database.')

















