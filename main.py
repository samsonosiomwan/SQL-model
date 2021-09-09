import sys
sys.path.append('src/models')
from src.utils.setup import *
from src.models.user import *
from src.models.book import *
from sqlite.setup import *
from sqlite.crud_operations import *



if __name__ == '__main__':
    
    #CREATE DEFAULT DATA
    # set_up = SetUpDatabase() 
    # check_set = set_up.setup_default_data()

    # #User Queries4
    new_user = User()
    # print(new_user.all())   # print all users in database
    # print(new_user.get(1))  # print one user using the user id
    # print(new_user.create(username ='tolu666',first_name = 'tolu',last_name ='omoseyin'))
    # print(new_user.update(username ='sma00',first_name='samson',last_name='biro',user_id=34))
    # print(new_user.destroy(19)) # delete user using using id
    # print('=============================================================')

    # Books Queries
    users_book = Book()
    # print(users_book.all(1))   # print all books attached to a user
    # print(users_book.get(1))     # print one book using book id 
    # print(users_book.create(user_id=1, book_name = 'nigeria constitution', pages=20))
    # print(users_book.update(39,1,'tomama',10)) #parameters format(book_id,user_id,book_name,pages)
    # print(users_book.destroy(1)) # delete user using using id
    # print('=============================================================')

    # sqllite3 Setup 
    # setup_database = SetUpSQL()
    # setup_database.convert_to_sql()

     # sqlite3 CrudOperations
    # crud_operation= CrudOperations()
    # print(crud_operation.read_all())
    # print(crud_operation.create(last_name = 'samson',first_name ='osiomwan',SSN = '123-45-6789', Test1 =50.1, Test2 = 50.1, Test3 = 50.2, Test4 = 50.3, Final = 50.1, Grade = 'D-'))
    # print(crud_operation.get_passed())
    # print(crud_operation.get_failed())
    # print(crud_operation.get_test1())
    # print(crud_operation.update(40,50,57,69,79,'D','123-45-6789'))
    # print(crud_operation.destroy("123-45-6789"))
    # print('=============================================================')


   