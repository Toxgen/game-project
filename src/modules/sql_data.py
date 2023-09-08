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


def execute_query(connection, query, 
                  ID=1, fetch=False, 
                  noText=False, autoSend=False, 
                  adv=False, 
                  
                  hp: int = 0, enemyhp: int = 0,
                  currentEffect: bool = None, mobName: str = "") -> (tuple | None):
    """
    Be careful with noText, it won't show if you made a error !!
    """
    
    cursor = connection.cursor()
    try:
        cursor.execute(query)

        if fetch:
            result = cursor.fetchone()

        if noText:
            print("Query successful")

        if autoSend:
            if adv:
                cursor.execute(f"""update stats
                                set hp = {hp}, enemyhp = {enemyhp}, mobName = {mobName}, cctEffect = {currentEffect}
                                where ID = {ID};""")
                
                # add extra columnns for those and check if they are even in an adventure
            cursor.execute(f"""update stats
                           set tut_boolean = True
                           where ID = {ID};""") # add query that allows it to update to the table based on the ID!!
            return

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
