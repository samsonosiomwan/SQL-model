import sys
sys.path.append('src/utils')
from connection import Connection
from interfaces import UserInterface
from datetime import datetime


class Book(UserInterface):
    '''this class initializes database connection. methods: all()(returns a list of all books), get()(returns a tuple of the book selected by book_id),
    create()(creates new user), update()updates  user records, destroy()destroy users record'''
    def __init__(self):
        self.connection = Connection()
        self.connect = self.connection.connect()
        self.cursor = self.connect.cursor()

    #get all books by a particular user
    def all(self,user_id):
        self.cursor.execute(f'SELECT * FROM books WHERE user_id ={user_id}')
        return self.cursor.fetchall()
    
    #get one book using book id
    def get(self,book_id):
        self.cursor.execute(f'SELECT * FROM books WHERE user_id ={book_id}')
        return self.cursor.fetchone()
    
    def create(self,user_id=1,book_name = '',pages=50):
        insert_query = "INSERT INTO books (user_id, book_name, pages) VALUES(%s,%s,%s) RETURNING *"
        self.cursor.execute(insert_query,(user_id,book_name,pages))
        self.connect.commit()
        return self.cursor.fetchone()
    
    def update(self,book_id,user_id,book_name,pages):
        update_time = datetime.now()
        update_query = 'UPDATE books SET user_id= %s, book_name = %s, pages=%s, updated_at=%s WHERE book_id=%s RETURNING *'
        self.cursor.execute(update_query,(user_id,book_name,pages,update_time,book_id))
        self.connect.commit()
        return self.cursor.fetchone()
    
    # method to delete user data from database using user id
    def destroy(self, user_id):
        self.cursor.execute(f'DELETE FROM  books WHERE user_id={user_id} RETURNING *')
        self.connect.commit()
        return self.cursor.fetchone()
