import mysql.connector
from mysql.connector import Error

pw = "5qnwpjhr027frfhrmm"

def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
        )
        print("MySQL Server connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
       print("Error: database already exists")


def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection


def execute_query(connection, query, commit=False, fetch=False):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        if commit:
            connection.commit()

        if fetch:
            result = cursor.fetchone()

        print("Query successful")

        return result
    except Error as err:
        print(f"Error: '{err}'")


if __name__ == "__main__":

    connection = create_server_connection(host_name="localhost", 
                                     user_name="root", 
                                     user_password=pw)
    
    connection = create_db_connection(host_name="localhost",
                         user_name="root", 
                         user_password=pw,
                         db_name="rpg_stats")
