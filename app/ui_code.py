# Import required modules
from tkinter import *
import sqlite3

# Create root window
root = Tk()

# Set root window title and dimensions
root.title("SQLite Data Display")
root.geometry('400x300')

# Connect to SQLite Database
db_path = "C:/Users/Movie_Info.db"  
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

# Label and Entry Fields
lbl = Label(root, text="Enter ID to fetch User:")
lbl.grid(column=0, row=0, padx=10, pady=10)

txt = Entry(root, width=10)
txt.grid(column=1, row=0)

# Label to display fetched data
lbl_result = Label(root, text="")
lbl_result.grid(column=0, row=2, columnspan=2, padx=10, pady=20)

# Function to display user data
def fetch_user():
    user_id = txt.get()
    cursor.execute("SELECT genre,genre_Id FROM genre WHERE genre_Id=?", (user_id,))
    user_data = cursor.fetchone()
    
    if user_data:
        result_text = f"genre: {user_data[0]}, genre_Id: {user_data[1]}"
    else:
        result_text = "No user found with this ID"
    
    lbl_result.config(text=result_text)

# Button to trigger data fetch from SQLite
btn = Button(root, text="Fetch User", fg="red", command=fetch_user)
btn.grid(column=2, row=0, padx=10)

# Another function to display all users from the database in the GUI
def fetch_all_users():
    cursor.execute("SELECT * FROM genre")
    all_users = cursor.fetchall()
    all_users_text = "\n".join([f"ID: {row[0]}, Name: {row[1]}" for row in all_users])
    lbl_result.config(text=all_users_text)

# Button to display all users
btn_all = Button(root, text="Fetch All Genre", fg="blue", command=fetch_all_users)
btn_all.grid(column=0, row=1, padx=10)

# Commit and close SQLite connection when done
connection.commit()

# Execute Tkinter
root.mainloop()

# Close SQLite connection after Tkinter window is closed
connection.close()
