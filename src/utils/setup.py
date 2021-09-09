from ..utils.interface import SetUpDatabaseInteface
from ..utils.connection import Connection


class SetUpDatabase(SetUpDatabaseInteface):
    'this class setup connection and has the setup_default-data method which creates a dafault table and inserts default data automatically'
    def __init__(self):
        #instantiate connection from connection module
        self.connection = Connection()
        self.connect = self.connection.connect()
        self.cursor = self.connect.cursor()
    
    def setup_default_data(self):
        try:
            self.cursor.execute('DROP TABLE if exists books CASCADE')
            self.cursor.execute('DROP TABLE if exists users CASCADE')

            #create default table via schema.sql file
            with open('src/sql_files/schema.sql','r') as schema_file:
                self.cursor.execute(schema_file.read())
                self.connect.commit()
                print('create default table sucessful')

            #insert default data via seeder.sql file
            with open('src/sql_files/seeder.sql','r') as seeder_file:
                self.cursor.execute(seeder_file.read())
                self.connect.commit()
                print('insert default data sucessful')
        except Exception as error:
            print(f'failed to setup default data: {error}')
        finally:
            self.connect.close()


