from controller.library import Library

newLibrary = Library()

print('Welcome to newLibrary')

def show_menu():
    print('--- Menu ---')
    print('1 - Add book')
    print('2 - View all books')
    print('3 - View books by genre')
    print('4 - Edit book')
    print('5 - Remove book')
    print('0 - Close the system')

while True:
    show_menu()
    option = int(input('Option: '))
    if option == 0:
        print('Shutting down the system..')
        break
    if option == 1:
        title = input('Title: ')
        author = input('Author: ')
        edition = input('Edition: ')
        genre = input('Genre: ')
        print(newLibrary.add_book(title, author, edition, genre))
    if option == 2:
        print(newLibrary.get_all_books())
    if option == 3:
        genre = input('Genre: ')
        print(newLibrary.get_book_by_genre(genre))
    if option == 4:
        title = input('Title: ')
        newEdition = input('New edition: ')
        print(newLibrary.edit_book(title, newEdition))
    if option == 5:
        title = input('Title: ')
        print(newLibrary.delete_book(title))