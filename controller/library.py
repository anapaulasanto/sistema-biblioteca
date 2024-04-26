from models.connection.connection import DBConnectionHandler
from models.repository.books_repository import BooksRepository


class Library:
    def __init__(self):
        connection_handler = DBConnectionHandler()
        connection_handler.connect_to_db()
        db_connection = connection_handler.get_db_connection()
        self.__books_repo = BooksRepository(db_connection)

    def add_book(self, title, author, edition, genre):
        self.__books_repo.insert_new_book(title, author, edition,genre)

    def get_all_books(self):
        return self.__books_repo.select_all()
    
    def get_book_by_genre(self, genre):
        books = self.get_all_books()
        genres_available = set(book['genre'] for book in books)

        if genre in genres_available:
            return self.__books_repo.select_by_genre(genre)
        else:
            print('Book genre not found!')

    def edit_book(self,title, new_edition):
        books = self.get_all_books()
        titles_available = set(book['title'] for book in books)
        
        if title in titles_available:
            return self.__books_repo.edit_book(title, new_edition)
        else:
            print('Book title not found!')
    
    def delete_book(self, title):
        books = self.get_all_books()
        titles_available = set(book['title'] for book in books)
        
        if title in titles_available:
            return self.__books_repo.delete_book(title)
        else:
            print('Book title not found!')