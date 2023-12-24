import tkinter as tk
from tkinter import ttk
import mysql.connector
from ConectDB import connect, close_connection

# Establish the database connection
connection = connect()
cursor = connection.cursor()

# Function to fetch menu items from the database
def fetch_menu_items():
    try:
        # Replace 'menu_items' with your actual table name
        query = "SELECT food_name, food_price FROM menu_items"
        cursor.execute(query)
        menu_items = cursor.fetchall()
        return menu_items

    except mysql.connector.Error as err:
        print(f"Error fetching menu items: {err}")
        return None

# Function to generate a bill
def generate_bill():
    # Retrieve data from the database
    menu_items = fetch_menu_items()

    if not menu_items:
        return

    # Create bill content
    table_number = combo_table.get()
    bill_content = f"Table Number: {table_number}\n\n{'Item': <15}{'Price'}\n"

    for item in menu_items:
        food_name, food_price = item
        bill_content += f"{food_name}: ${food_price:,.2f}\n"

    # Display the bill in a new window
    bill_window = tk.Toplevel(root)
    bill_window.title("Bill")

    # Create a Text widget to display the bill content
    bill_text = tk.Text(bill_window, height=20, width=40)
    bill_text.insert(tk.END, bill_content)
    bill_text.pack()

# Create the main window
root = tk.Tk()
root.title("Bill Generator")

# Create a ComboBox for table selection
combo_table = ttk.Combobox(root)
combo_table['values'] = ('1', '2', '3', '4', '5')
combo_table.pack()

# Create a button to generate the bill
generate_button = tk.Button(root, text="Generate Bill", command=generate_bill)
generate_button.pack()

# Create a TreeView to display menu items (replace 'menu_items' with your actual table name)
columns = ('food_name', 'food_price')
treeview = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    treeview.heading(col, text=col)

# Fetch and populate menu items in the TreeView
menu_items = fetch_menu_items()
if menu_items:
    for item in menu_items:
        treeview.insert('', 'end', values=item)

treeview.pack()

# Start the Tkinter event loop
root.mainloop()

# Close the database connection when the tkinter window is closed
root.protocol("WM_DELETE_WINDOW", lambda: [close_connection(connection), root.destroy()])
