from dotenv import dotenv_values
import psycopg2 as pg

config = dotenv_values('.env')


class DatabaseOperator:
    def __init__(self, **params):
        self.host = params.get('host', config['DATABASE_HOST'])
        self.database_name = params.get('database', config['DATABASE_NAME'])
        self.user = params.get('user', config['DATABASE_USER'])
        self.password = params.get('password', config['DATABASE_PASSWORD'])
        self.port = params.get('port', config['DATABASE_PORT'])
        self.conn = pg.connect(
            host=self.host,
            database=self.database_name,
            user=self.user,
            password=self.password,
            port=self.port
        )

    def get_cursor(self):
        return self.conn.cursor()