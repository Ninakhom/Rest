import tkinter as tk
from tkinter import ttk, messagebox
from ConectDB import connect, close_connection
import sys,os
from reportlab.pdfgen import canvas
from datetime import datetime
connection = connect()
cursor = connection.cursor()



c1='#020f12'
c2='#508CF7'
c3='#508CF7'
c4='black'
current_datetime = datetime.now()
frm = tk.Tk()
frm.title("Bill Data")
frm.config(bg='#CFD5E2')
frm.resizable(0,0)
frm.state('zoomed')
lbFrame1 = tk.LabelFrame(frm, text='Check bill',width=1100, height=500,background='#CFD5E2')
lbFrame1.place(x=460, y=150)
lbFrame1.config(font=("Times New Roman", 14, "bold"), fg="darkblue")

def update_label():

    current_datetime = datetime.now()  
    lbdate.config(text=current_datetime.strftime("%d-%m-%Y %H:%M:%S"),font=("Helvetica", 16))
    lbdate.after(1000, update_label)


def fetch_bills():
    try:
        connection = connect()
        cursor = connection.cursor()

        query = """
        SELECT bill_id, order_id, total_amount, payment_status, bill_date
        FROM bills
        WHERE payment_status != 'Paid'
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
    treeview.delete(*treeview.get_children())  
    bills = fetch_bills()
    if bills:
        for row in bills:
            treeview.insert("", "end", values=row)


def generate_receipt_pdf(bill_id, order_id, total_amount, payment_amount, change, items):
    pdf_filename = f"Receipt_Bill_{bill_id}.pdf"

   
    pdf = canvas.Canvas(pdf_filename)

    
    pdf.drawString(100, 800, f"Receipt for Bill ID: {bill_id}")
    pdf.drawString(100, 780, f"Order ID: {order_id}")
    pdf.drawString(100, 760, f"Staff ID: {staff_id}")

    
    pdf.drawString(100, 740, "-" * 50)
    pdf.drawString(100, 720, "Items:")
    pdf.drawString(200, 720, "Quantity:")
    pdf.drawString(300, 720, "Price:")
    pdf.drawString(100, 700, "-" * 50)

   
    y_position = 680
    for item in items:
        item_name, quantity, price = item
        pdf.drawString(100, y_position , f"{item_name}")
        pdf.drawString(200, y_position, f"{quantity}")
        pdf.drawString(300, y_position, f"{price:.2f} Kip")
        y_position -= 40

    pdf.drawString(100, y_position, "-" * 50)
    y_position -= 20

    pdf.drawString(100, y_position, f"Total Amount: {total_amount:.2f} Kip")
    pdf.drawString(100, y_position - 20, f"Payment Amount: {payment_amount:.2f} Kip")
    pdf.drawString(100, y_position - 40, f"Change: {change:.2f} Kip")


    pdf.save()

    messagebox.showinfo("PDF Generated", f"PDF receipt for Bill ID {bill_id} generated successfully.")



def generate_receipt(bill_id, order_id, total_amount, payment_amount, change):
    try:

        item_query = "SELECT item_name, quantity, price FROM order_items WHERE order_id = %s"
        cursor.execute(item_query, (order_id,))
        items = cursor.fetchall()

        receipt_content = f"Receipt for Bill ID: {bill_id}\n"
        receipt_content += f"Order ID: {order_id}\n"
        receipt_content += f"Staff ID: {staff_id}\n"
        

        receipt_content += "\nItems:\n"
        for item in items:
            item_name, quantity, price = item
            receipt_content += f"{item_name} - Quantity: {quantity}, Price: {price:.2f} Kip\n"
        receipt_content += f"Total Amount: {total_amount:.2f} Kip\n"
        receipt_content += f"Payment Amount: {payment_amount:.2f} Kip\n"
        receipt_content += f"Change: {change:.2f} Kip\n"

        receipt_window = tk.Toplevel(frm)
        receipt_window.title("Receipt")

        receipt_text = tk.Text(receipt_window, height=15, width=40)
        receipt_text.insert(tk.END, receipt_content)
        receipt_text.pack()

        # Generate PDF
        generate_receipt_pdf(bill_id, order_id, total_amount, payment_amount, change, items)

        # Bring the receipt window to the front
        receipt_window.lift()

    except Exception as err:
        messagebox.showerror("Error", f"Error generating receipt: {err}")



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
            messagebox.showerror("Error", "ຈຳນວນເງີນບໍ່ພໍ")
        else:
            result = messagebox.askyesno("Generate Bill", "Do you want to generate a receipt?")
            if result:
                change = money_amount - total_amount
                generate_receipt(bill_id, order_id, total_amount, money_amount, change)

            # Update the payment status to 'Paid' in the "bills" table
            update_payment_status_query = "UPDATE bills SET payment_status = 'Paid', staff_id = %s WHERE bill_id = %s"
            cursor.execute(update_payment_status_query, ( staff_id,bill_id,))
            connection.commit()

            change = money_amount - total_amount
            messagebox.showinfo("Payment Successful", f"Payment successful!\nChange: {change:.2f} Kip")
            payment_entry.delete(0,'end')

        # Refresh the displayed bills after payment
        treeview.delete(*treeview.get_children())
        display_bills()

    except ValueError:
        messagebox.showerror("Error", "Invalid payment amount. Please enter a valid number.")

def Logout():
    # Ask for confirmation using a messagebox
    confirmed = messagebox.askyesno("Confirm Logout", "Are you sure you want to logout?")

    if confirmed:
        # Perform any logout-related actions here
        print("Logging out...")

        # Optionally, destroy the main Tkinter window
        frm.destroy()
        os.system(f"python Stafflogin.py ")


lgn_frame = tk.Frame(frm, bg='#508CF7', width=2000, height=80)
lgn_frame.place(x=0, y=0)

columns = ('Bill ID', 'Order ID', 'Total Amount', 'Payment Status', 'Bill Date')
treeview = ttk.Treeview(frm, columns=columns, show="headings")

for col in columns:
    treeview.heading(col, text=col)

display_bills()
treeview.place(x=500,y=250)
if len(sys.argv) >= 4:
    position = sys.argv[1]
    staff_name = sys.argv[2]
    staff_id = sys.argv[3]
    print(f"Position: {position}, Staff Name: {staff_name}, Staff ID: {staff_id}")
    print("Print statement reached.")

payment_label = tk.Label(frm, text="Enter Payment Amount:",bg='#CFD5E2')
payment_label.place(x=800,y=500)

payment_entry = tk.Entry(frm)
payment_entry.place(x=1000,y=500)

pay_button = tk.Button(frm, text="Pay", command=pay_money ,bg=c2,
    fg=c4,
    activebackground=c3,
    activeforeground=c4,
    highlightthickness=2,
    highlightbackground=c2,
    highlightcolor='white',
    width=10,
    border=5,
    cursor='hand1',)
pay_button.place(x=1000,y=550)
button_Logout = tk.Button(text="Logout", command=Logout, bg=c2,
    fg=c4,
    activebackground=c3,
    activeforeground=c4,
    highlightthickness=2,
    highlightbackground=c2,
    highlightcolor='white',
    
    border=5,
    cursor='hand1',
    
    )
button_Logout.place(x=1450,y=650)
lbdate=tk.Label(frm,text=current_datetime,bg='#CFD5E2')
lbdate.place(x=860,y=120)
update_label()

frm.mainloop()
