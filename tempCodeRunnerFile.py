def login():
    user = entry_username.get()
    password = entry_password.get()

    sql = "SELECT user_id, username, role FROM users WHERE username=%s AND password=%s"
    cursor.execute(sql, (user, password))
    user_info = cursor.fetchone()

    if user_info is None:
        messagebox.showinfo("Error", "Sorry, your username or password is incorrect")
    else:
        user_id, username, role = user_info

        # Store user information globally for access in other parts of the program
        set_user_info(user_id, username, role)
        user_author = role  # Replace this with your actual logic to determine the user's role
        name=username
        print(name)
        close_connection(connection)
        frm.destroy()
        os.system(f"python costumer.py {role} {username}")

        # Add your logic for what happens after a successful login here
        return user_author, role,name,username,user_id