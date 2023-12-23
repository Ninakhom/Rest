import mysql.connector

def connect():
    try:
        # Replace these with your actual database connection details
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="restaurant_management"
        )

        return connection

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def close_connection(connection):
    if connection:
        connection.close()
        print("Database connection closed.")




# Example usage
# Uncomment the following lines and replace the placeholders with actual values
# conn = connect()
# close_connection(conn)
