import sys
sys.path.append('src/utils')
from connection import Connection
from interfaces import UserInterface
from datetime import datetime


class User(UserInterface):
    '''this class initializes database connection. methods: all()(returns a list of all users), get()(returns a tuple of the user selected),
    create()(creates new user), update()updates  user records, destroy()destroy users record'''
    def __init__(self):
        #insatiating database connection from Connection in connection module
        self.connection = Connection()
        self.connect = self.connection.connect()
        self.cursor = self.connect.cursor()
    
    # method to get all users from data base
    def all(self):
        '''method to get all users from data base'''
        
        self.cursor.execute('SELECT * FROM users')
        return self.cursor.fetchall()

     # method to get one user from data base using user id
    def get(self,user_id):
        self.cursor.execute(f'SELECT * FROM users WHERE user_id ={user_id}')
        return self.cursor.fetchone()

    
    def create(self,username ='',first_name = '',last_name =''):
        insert_query = "INSERT INTO users (username, first_name, last_name) VALUES(%s,%s,%s) RETURNING *"
        self.cursor.execute(insert_query,(username,first_name,last_name))
        self.connect.commit()
        return self.cursor.fetchone()

    def update(self,user_id,username ='',first_name='',last_name=''):
        update_time = datetime.now()
        update_query = 'UPDATE users SET username=%s,first_name=%s, last_name=%s, updated_at=%s WHERE user_id = %s RETURNING *' 
        self.cursor.execute(update_query,(username,first_name,last_name,update_time,user_id))
        self.connect.commit()
        return self.cursor.fetchone()
    
    # method to delete user data from database using user id
    def destroy(self, user_id):
        self.cursor.execute(f'DELETE FROM users WHERE user_id={user_id} RETURNING *')
        self.connect.commit()
        return self.cursor.fetchone()

   

