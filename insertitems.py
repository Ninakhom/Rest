import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
import mysql.connector as mysql
from ConectDB import connect, close_connection
import os

def insert_menu_item():
    item_name = entry_item_name.get()
    description = entry_description.get()
    price = entry_price.get()

    connection = connect()

    if connection:
        try:
            cursor = connection.cursor()
            price_float = float(price.replace(',', ''))

            # SQL query to insert a menu item
            sql_query = "INSERT INTO menu_items (item_name, description, price) VALUES (%s, %s, %s)"
            values = (item_name, description, price_float)

            # Execute the query
            cursor.execute(sql_query, values)

            # Commit the changes to the database
            connection.commit()

            messagebox.showinfo("Success", "Menu item inserted successfully!")
            show_menu_items()

        except mysql.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

        finally:
            # Close the cursor and connection
            if cursor:
                cursor.close()

            close_connection(connection)

def show_menu_items():
    connection = connect()

    if connection:
        try:
            cursor = connection.cursor()

            # SQL query to select all menu items
            sql_query = "SELECT * FROM menu_items"
            cursor.execute(sql_query)

            # Clear existing items in the TreeView
            for row in treeview.get_children():
                treeview.delete(row)

            # Insert new items into the TreeView
            for row in cursor.fetchall():
                treeview.insert("", "end", values=row)

        except mysql.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

        finally:
            # Close the cursor and connection
            if cursor:
                cursor.close()

            close_connection(connection)

def delete_menu_item():
    selected_item = treeview.selection()

    if not selected_item:
        messagebox.showwarning("Warning", "Please select a menu item to delete.")
        return

    connection = connect()

    if connection:
        try:
            cursor = connection.cursor()

            # Get the item_id from the selected item
            item_id = treeview.item(selected_item, 'values')[0]

            # SQL query to delete a menu item
            sql_query = "DELETE FROM menu_items WHERE item_id = %s"
            values = (item_id,)

            # Execute the query
            cursor.execute(sql_query, values)

            # Commit the changes to the database
            connection.commit()

            messagebox.showinfo("Success", "Menu item deleted successfully!")
            show_menu_items()

        except mysql.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

        finally:
            # Close the cursor and connection
            if cursor:
                cursor.close()

            close_connection(connection)

def cancel():
    frm.destroy()
    os.system("python dash.py")

# GUI setup
frm = tk.Tk()
frm.geometry("1500x1000")
frm.title("Menu-Items")


# Entry widgets for item details
label_item_name = tk.Label(frm, text="Item Name:")
label_item_name.grid(row=0, column=0, padx=10, pady=10)
entry_item_name = tk.Entry(frm)
entry_item_name.grid(row=0, column=1, padx=10, pady=10)

label_description = tk.Label(frm, text="Description:")
label_description.grid(row=1, column=0, padx=10, pady=10)
entry_description = tk.Entry(frm)
entry_description.grid(row=1, column=1, padx=10, pady=10)

label_price = tk.Label(frm, text="Price:")
label_price.grid(row=2, column=0, padx=10, pady=10)
entry_price = tk.Entry(frm)
entry_price.grid(row=2, column=1, padx=10, pady=10)

# Button to insert menu item
button_insert = tk.Button(frm, text="Insert Menu Item", command=insert_menu_item)
button_insert.grid(row=3, column=0, columnspan=2, pady=10)

# TreeView to display menu items
treeview_columns = ("Item ID", "Item Name", "Description", "Price")
treeview = ttk.Treeview(frm, columns=treeview_columns, show="headings")
treeview.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

# Configure column headings
for col in treeview_columns:
    treeview.heading(col, text=col)
    treeview.column(col, width=100)

# Button to delete selected menu item
button_delete = tk.Button(frm, text="Delete Menu Item", command=delete_menu_item)
button_delete.place(x=50,y=50)

# Button to refresh menu items in TreeView
button_refresh = tk.Button(frm, text="Refresh Menu Items", command=show_menu_items)
button_refresh.grid(row=6, column=0, columnspan=2, pady=10)

button_cancel = tk.Button(frm, text="Cancel", command=cancel)
button_cancel.grid(row=10, column=0, columnspan=2, pady=10)

# Show initial menu items
show_menu_items()

frm.mainloop()
