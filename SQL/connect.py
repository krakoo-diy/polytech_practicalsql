import psycopg2
from config import load_config


def create_tables(config):
    """ Create tables in the PostgreSQL database"""
    commands = [
            """
            CREATE TYPE mood AS ENUM ('sad', 'ok', 'happy');
            """,
            """
            CREATE TABLE activity_metadata5 (
                activity_metadata_id SERIAL PRIMARY KEY,
                activity_metadata_name VARCHAR(255) NOT NULL
            )"""
        ]  
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the CREATE TABLE statement
                for command in commands:
                    print(command)
                    cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


def connect(config):
    """ Connect to the PostgreSQL database server """
    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect(**config) as conn:
            print('Connected to the PostgreSQL server.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


if __name__ == '__main__':
    config = load_config()
    create_tables(config)