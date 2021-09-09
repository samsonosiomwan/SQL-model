import psycopg2

class Connection:
    
    def connect(self):
        try:
            with psycopg2.connect(host='localhost', database='my_library', user = 'postgres') as conn:
                return conn
        except Exception as err:
            print(f'database connection failed: {err}')


