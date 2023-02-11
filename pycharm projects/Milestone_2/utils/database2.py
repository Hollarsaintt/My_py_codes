"""
Concerned with Storing and retrieving data from a our database.csv
"""
# books = [
#     {'name': 'lamlad physics', 'author': 'lamlad', 'read': True},
#     {'name': 'Independence', 'author': 'jamb', 'read': False},
#     {'name': 'sweet sixteen', 'author': 'Not known', 'read': True},
#     {'name': 'Invisible teacher', 'author': 'Dele Ashade', 'read': False}
# ]

import csv


def writer(book, mode, write):
    with open('database.csv',mode, newline='') as d:
        writer2 = csv.DictWriter(d, fieldnames= ['name', 'author', 'read'])
        with open('database.csv', 'r') as d:
            if d.read() == '':
                writer2.writeheader()
        if write == 's': writer2.writerows(book)
        else: writer2.writerow(book)


def reader():
    with open('database.csv', 'r') as d:
        books = csv.DictReader(d)
        return list(books)


def add_book():
    name = input('\nEnter the name of the book: ')
    author = input('Enter the name of the author: ')
    read = input('\nHave you read this book? Y/N: ')
    while read.lower() != 'y' and read.lower() != 'n': read = input('\nHave you read this book? Y/N: ')
    if read.lower() == 'y': read = True
    else: read = False
    if name != '' and author != '':
        book = {'name': name, 'author': author, 'read': read}
        writer(book, 'a', '')
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
        print_book = lambda book: print(f"{book['name']} by {book['author']}\tREAD: {(book['read'])}")
        try:
            books = reader()
            with open('database.csv', 'r') as d:
                if d.read() != '':
                    if _l == 'a':
                        for book in books: print_book(book)
                    elif _l == 'r':
                        for book in books:
                            if book['read'] == 'True': print_book(book)
                    elif _l == 'u':
                        for book in books:
                            if book['read'] != 'True': print_book(book)
                else: print('No data in database!\nAdd books!')
        except:
            print('No data in database yet!\nAdd data and try again!')


def remove_book():
    book_name = input("\nEnter the name of the book: ")
    try:
        books = reader()
        with open('database.csv', 'r') as d:
            if d.read() != '':
                for book in books:
                    if book_name.lower() == book['name'].lower():
                        books.remove(book)
                        writer(books, 'w', 's')
                        print('\nBOOK SUCESSFULLY REMOVE!')
                        break
                else:
                    print('\nYou have typed a name not in the database.')
            else: print('\nNo data!\nAdd DATA!')
    except:
        print('\nNo data in database yet!')


def mark_as_read():
    book_name = input("\nEnter the name of the book: ")
    try:
        books = reader()
        with open('database.csv', 'r') as d:
            if d.read() != '':
                for book in books:
                    if book_name.lower() == book['name'].lower():
                        book['read'] = 'True'
                        writer(books, 'w', 's')
                        print('\nBOOK SUCESSFULLY MARK AS READ!')
                        break
                else:
                    print('\nYou have typed a name not in the database.')
            else: print('\nI have no data in me.')
    except:
        print('\nADD data first!')

















