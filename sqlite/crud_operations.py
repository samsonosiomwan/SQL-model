import sqlite3
from sqlite.interfaces import CrudOperationInterface

class CrudOperations(CrudOperationInterface):
    '''this class handles CRUD Operations of grades database,methods(read_all(), create():creates new records, get_passed():returns students that passed, 
       get_failed() returns students that failed(get_test1():returns students that passed test1, update() and destroy()'''
    def __init__(self):
        self.connection = sqlite3.connect('sqlite/grades.db')
        self.cursor = self.connection.cursor()

    def read_all(self):
        self.cursor.execute('SELECT * FROM grades')
        return self.cursor.fetchall()

    def create(self, last_name = '',first_name ='',SSN = '', Test1 =40.2, Test2 =40.2, Test3 = 40.4, Test4 = 40.5, Final = 49.0, Grade = ''):
        insert_query = f"INSERT INTO grades VALUES (?,?,?,?,?,?,?,?,?)"
        self.cursor.execute(insert_query, (last_name,first_name,SSN,Test1,Test2,Test3,Test4,Final,Grade))
        self.connection.commit()
        return self.read_all()
    
    
    def get_passed(self):
        self.cursor.execute('SELECT * FROM grades WHERE Final>="50"')
        rows,new_rows = self.cursor.fetchall(),'' #rows and new_rows variable, new_rows set to empty
        for row in rows:new_rows+= f'\n\nstudent:\nLast Name:{row[0]}\nFirst Name:{row[1]}\nSSN:{row[2]}\nTest1:{row[3]}\nTest2:{row[4]}\nTest3:{row[5]}\nTest4:{row[6]}\nFinal:{row[7]}\nGrade:{row[8]}'
        return new_rows
    
    def get_failed(self):
        self.cursor.execute('SELECT * FROM grades WHERE Final<"50"')
        rows,new_rows = self.cursor.fetchall(),'' #rows and new_rows variable, new_rows set to empty
        for row in rows:new_rows+= f'\n\nstudent:\nLast Name:{row[0]}\nFirst Name:{row[1]}\nSSN:{row[2]}\nTest1:{row[3]}\nTest2:{row[4]}\nTest3:{row[5]}\nTest4:{row[6]}\nFinal:{row[7]}\nGrade:{row[8]}'
        return new_rows
    
    def get_test1(self):
        self.cursor.execute('SELECT * FROM grades WHERE Test1 >= 45')
        rows,new_rows = self.cursor.fetchall(),'' #rows and new_rows variable, new_rows set to empty
        for row in rows:new_rows+= f'\n\nstudent:\nLast Name:{row[0]}\nFirst Name:{row[1]}\nSSN:{row[2]}\nTest1:{row[3]}\nFinal:{row[7]}\nGrade:{row[8]}'
        return new_rows

    def update(self,Test1,Test2,Test3,Test4,Final,Grade,SSN):
        update_query = 'UPDATE grades SET Test1=?, Test2=?, Test3=?, Test4=?, Final=?, Grade=? WHERE SSN=?'
        self.cursor.execute(update_query, (Test1,Test2,Test3,Test4,Final,Grade,SSN))
        self.connection.commit()
        return self.read_all()

    def destroy(self, ssn):
        self.cursor.execute("DELETE FROM grades WHERE SSN=?",(ssn, ))
        self.connection.commit()
        return self.read_all()

