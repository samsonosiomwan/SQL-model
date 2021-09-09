from sqlite.interfaces import ToSQLInterface
import sqlite3
import pandas

class SetUpSQL(ToSQLInterface):
    '''this class initializies sqlite connection to sqlite3 and creates database if none exists, it has convert_to_sql method which opens csv files and converts it sql'''
    def __init__(self):
        self.connection = sqlite3.connect('sqlite/grades.db')
        self.cursor = self.connection.cursor()
    
    def convert_to_sql(self):
        with open('sqlite/grades.csv','r') as csv_to_sql:
            csv_data = pandas.read_csv(csv_to_sql)
            csv_data.to_sql('grades',self.connection, if_exists = 'replace', index=False)
