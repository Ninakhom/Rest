<<<<<<< HEAD
=======
# ConnectDB.py

import mysql.connector

def connect():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="restaurant_management"
        )
        print("Connected to the database")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def close_connection(connection):
    if connection:
        connection.close()
        print("Connection closed")

def get_cursor(connection):
    if connection:
        return connection.cursor()
    else:
        return None
>>>>>>> af9223f9155d6239345970c54263e4e47445eafa
