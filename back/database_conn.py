import psycopg2
from psycopg2._psycopg import OperationalError


def create_connection():
    try:
        conn = psycopg2.connect(
            database='trms-database',
            user='postgres',
            password='pass123',
            host='localhost',
            port='5432'
        )
        return conn
    except OperationalError as e:
        print(f"{e}")
        return None


conn = create_connection()


def _test():
    if conn:
        print("Connection is good")
    else:
        print("Connection is not working")


if __name__ == '__main__':
    _test()