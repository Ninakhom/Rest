import tkinter as tk
from tkinter import ttk, messagebox
from ConectDB import connect, close_connection

connection = connect()
cursor = connection.cursor()

def fetch_orders():
    try:
        connection = connect()
        cursor = connection.cursor()

        query = """
        SELECT orders.order_id, orders.user_id, orders.table_number, SUM(order_items.quantity) AS total_quantity,
               SUM(order_items.quantity * order_items.price) AS total_price
        FROM orders
        JOIN order_items ON orders.order_id = order_items.order_id
        GROUP BY orders.order_id, orders.user_id, orders.table_number
        """
        cursor.execute(query)
        orders = cursor.fetchall()
        return orders

    except Exception as err:
        messagebox.showerror("Error", f"Error fetching orders: {err}")
        return None

    finally:
        close_connection(connection)

def generate_bill(order_id, total_price, money_amount):
    bill_window = tk.Toplevel(frm)
    bill_window.title(f"Bill for Order ID: {order_id}")

    bill_content = f"Order ID: {order_id}\n\n"
    bill_content += f"{'Item': <20}{'Quantity': <10}{'Price'}\n"

    try:
        connection = connect()
        cursor = connection.cursor()

        query = "SELECT item_name, quantity, price FROM order_items WHERE order_id = %s"
        cursor.execute(query, (order_id,))
        order_items = cursor.fetchall()

        for item in order_items:
            item_name, quantity, price = item
            bill_content += f"{item_name: <20}{quantity: <10}${float(price) * quantity:,.2f}\n"

        bill_content += f"\nTotal: ${float(total_price):,.2f}\n"
        bill_content += f"Money Amount: ${float(money_amount):,.2f}\n"
        change = float(money_amount) - float(total_price)
        bill_content += f"Change: ${change:,.2f}"

        bill_text = tk.Text(bill_window, height=20, width=40)
        bill_text.insert(tk.END, bill_content)
        bill_text.pack()

    except Exception as e:
        messagebox.showerror("Error", f"Error fetching order items: {e}")

    finally:
        close_connection(connection)

def pay_money():
    try:
        money_amount = float(payment_entry.get())
        selected_item = treeview.focus()
        if not selected_item:
            messagebox.showwarning("No Selection", "Please select an order to process payment.")
            return

        selected_order = treeview.item(selected_item, 'values')
        order_id, user_id, table_number, total_quantity, total_price = selected_order[:5]

        if money_amount < float(total_price):
            messagebox.showerror("Error", "Insufficient payment amount.")
        else:
            result = messagebox.askyesno("Generate Bill", "Do you want to generate a bill?")
            if result:
                generate_bill(order_id, total_price, money_amount)

            change = money_amount - float(total_price)
            messagebox.showinfo("Payment Successful", f"Payment successful!\nChange: ${change:,.2f}")

    except ValueError:
        messagebox.showerror("Error", "Invalid payment amount. Please enter a valid number.")

frm = tk.Tk()
frm.title("Order Data")

columns = ('Order ID', 'User ID', 'Table Number', 'Quantity', 'Total Price')
global treeview
treeview = ttk.Treeview(frm, columns=columns, show="headings")

for col in columns:
    treeview.heading(col, text=col)

orders = fetch_orders()
if orders:
    for row in orders:
        treeview.insert("", "end", values=row)

treeview.pack()

generate_bill_button = tk.Button(frm, text="Generate Bill", command=generate_bill)
generate_bill_button.pack()

payment_label = tk.Label(frm, text="Enter Payment Amount:")
payment_label.pack()

payment_entry = tk.Entry(frm)
payment_entry.pack()

pay_button = tk.Button(frm, text="Pay", command=pay_money)
pay_button.pack()

frm.mainloop()
