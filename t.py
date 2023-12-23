import matplotlib.pyplot as plt
import mysql.connector
from mysql.connector import Error
from ConectDB import connect, close_connection

def get_best_selling_items(connection):
    try:
        cursor = connection.cursor()
        query = """
            SELECT item_name, SUM(quantity) AS total_quantity
            FROM order_items
            GROUP BY item_name
            ORDER BY total_quantity DESC
            LIMIT 10
        """
        cursor.execute(query)
        return cursor.fetchall()
    except Error as e:
        print(f"Error fetching data: {e}")
        return None

def plot_chart(best_selling_items):
    if best_selling_items:
        items = [item[0] for item in best_selling_items]
        quantities = [float(item[1]) for item in best_selling_items]  # Convert Decimal to float

        plt.pie(quantities, labels=items, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.title('Best Selling Items')
        plt.show()
    else:
        print("No data available.")

def main():
    connection = connect()
    if connection:
        best_selling_items = get_best_selling_items(connection)
        plot_chart(best_selling_items)
        close_connection(connection)

if __name__ == "__main__":
    main()
