import tkinter as tk
from tkinter import ttk, messagebox
from ConectDB import connect, close_connection
import sys
connection = connect()
cursor = connection.cursor()

def fetch_bills():
    try:
        connection = connect()
        cursor = connection.cursor()

        query = """
        SELECT bill_id, order_id, total_amount, payment_status, bill_date
        FROM bills
        """
        cursor.execute(query)
        bills = cursor.fetchall()
        return bills

    except Exception as err:
        messagebox.showerror("Error", f"Error fetching bills: {err}")
        return None

    finally:
        close_connection(connection)

def display_bills():
    bills = fetch_bills()
    if bills:
        for row in bills:
            treeview.insert("", "end", values=row)

def generate_receipt(bill_id, order_id, total_amount, payment_amount, change):
    receipt_content = f"Receipt for Bill ID: {bill_id}\n"
    receipt_content += f"Order ID: {order_id}\n"
    receipt_content += f"Total Amount: ${total_amount:.2f}\n"
    receipt_content += f"Payment Amount: ${payment_amount:.2f}\n"
    receipt_content += f"Change: ${change:.2f}\n"

    receipt_window = tk.Toplevel(frm)
    receipt_window.title("Receipt")

    receipt_text = tk.Text(receipt_window, height=10, width=40)
    receipt_text.insert(tk.END, receipt_content)
    receipt_text.pack()

def pay_money():
    try:
        money_amount = float(payment_entry.get())
        selected_item = treeview.focus()
        if not selected_item:
            messagebox.showwarning("No Selection", "Please select a bill to process payment.")
            return

        selected_bill = treeview.item(selected_item, 'values')
        bill_id, order_id, total_amount, payment_status, bill_date = selected_bill

        # Convert total_amount to float before comparison
        total_amount = float(total_amount)

        if payment_status == 'Paid':
            messagebox.showinfo("Payment Status", "This bill has already been paid.")
            return

        if money_amount < total_amount:
            messagebox.showerror("Error", "Insufficient payment amount.")
        else:
            result = messagebox.askyesno("Generate Bill", "Do you want to generate a receipt?")
            if result:
                change = money_amount - total_amount
                generate_receipt(bill_id, order_id, total_amount, money_amount, change)

            # Update the payment status to 'Paid' in the "bills" table
            update_payment_status_query = "UPDATE bills SET payment_status = 'Paid', staff_id = %s WHERE bill_id = %s"
            cursor.execute(update_payment_status_query, (bill_id, staff_id))
            connection.commit()

            change = money_amount - total_amount
            messagebox.showinfo("Payment Successful", f"Payment successful!\nChange: kip{change:.2f}")

        # Refresh the displayed bills after payment
        treeview.delete(*treeview.get_children())
        display_bills()

    except ValueError:
        messagebox.showerror("Error", "Invalid payment amount. Please enter a valid number.")

frm = tk.Tk()
frm.title("Bill Data")
frm.config(bg='#CFD5E2')
frm.geometry("1200x600")

columns = ('Bill ID', 'Order ID', 'Total Amount', 'Payment Status', 'Bill Date')
treeview = ttk.Treeview(frm, columns=columns, show="headings")
#config tree view bg color
style = ttk.Style()
style.configure("Treeview", background='#CFD5E2')



for col in columns:
    treeview.heading(col, text=col)

display_bills()
treeview.pack()

if len(sys.argv) >= 4:
    position = sys.argv[1]
    staff_name = sys.argv[2]
    staff_id = sys.argv[3]
    print(f"Position: {position}, Staff Name: {staff_name}, Staff ID: {staff_id}")
    print("Print statement reached.")

payment_label = tk.Label(frm, text="Enter Payment Amount:")
payment_label.pack()
payment_label.config(bg='#CFD5E2')

payment_entry = tk.Entry(frm)
payment_entry.pack()

pay_button = tk.Button(frm, text="Pay", command=pay_money)
pay_button.pack()

frm.mainloop()
