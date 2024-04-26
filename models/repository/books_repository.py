class BooksRepository:
    def __init__(self,db_connection):
        self.db_connection = db_connection
        self.__collection = db_connection['library']

    def insert_new_book(self, title, genre, author, edition):
        result = self.__collection.insert_one({
            'title': title,
            'genre': genre,
            'author': author,
            'edition': edition
        })
        if result.acknowledged:
            print('Inserted!')
        else:
            print('Not inserted!')

    def select_all(self):
        books = self.__collection.find({}, {'_id': 0})
        return list(books)
    
    def select_by_genre(self, genre):
        book = self.__collection.find({
            'genre': genre
        })
        return list(book)
    
    def edit_book(self, title, new_edition):
        result = self.__collection.update_one(
            {'title': title},
            {'$set': {'edition': new_edition}}
        )
        return result.modified_count
    
    def delete_book(self, title):
        result = self.__collection.delete_one({
            'title': title
        })
        return result.deleted_count
