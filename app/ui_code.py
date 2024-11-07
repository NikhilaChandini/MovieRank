# Import required modules
from tkinter import *
import sqlite3

# Create root window
root = Tk()

# Set root window title and dimensions
root.title("SQLite Data Display")
root.geometry('600x500')

# Connect to SQLite Database
db_path = "C:/Users/Movie_Info.db"  
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

# Labels and Entry Fields for genre_id and genre_name
lbl_id = Label(root, text="Enter Genre ID:")
lbl_id.grid(column=0, row=0, padx=10, pady=10)
entry_id = Entry(root, width=10)
entry_id.grid(column=1, row=0)

lbl_name = Label(root, text="Enter Genre Name:")
lbl_name.grid(column=0, row=1, padx=10, pady=10)
entry_name = Entry(root, width=20)
entry_name.grid(column=1, row=1)

# Label to display fetched data
lbl_result = Label(root, text="", wraplength=500, justify=LEFT)
lbl_result.grid(column=0, row=5, columnspan=3, padx=10, pady=20)

# Function to display genre by genre ID
def fetch_genre():
    genre_id = entry_id.get()
    cursor.execute("SELECT genre, genre_Id FROM genre WHERE genre_Id=?", (genre_id,))
    genre_data = cursor.fetchone()
    
    if genre_data:
        result_text = f"Genre: {genre_data[0]}, Genre ID: {genre_data[1]}"
    else:
        result_text = "No genre found with this ID."
    
    lbl_result.config(text=result_text)

# Button to trigger genre data fetch
btn_fetch_genre = Button(root, text="Fetch Genre", fg="red", command=fetch_genre)
btn_fetch_genre.grid(column=2, row=0, padx=10)

# Function to display all genres
def fetch_all_genres():
    cursor.execute("SELECT * FROM Movie_details")
    all_genres = cursor.fetchall()
    all_genres_text = "\n".join([f"ID: {row[0]}, Movie details: {row[1]}" for row in all_genres])
    lbl_result.config(text=all_genres_text)

# Button to display all genres
btn_all_genres = Button(root, text="Fetch All Movie details", fg="blue", command=fetch_all_genres)
btn_all_genres.grid(column=0, row=2, padx=10)

# Insert a new genre
def insert_genre():
    genre_name = entry_name.get()
    genre_id = entry_id.get()
    if genre_name:
        cursor.execute("INSERT INTO genre (genre_Id,genre) VALUES (?,?)", (genre_id, genre_name))
        connection.commit()
        lbl_result.config(text=f"Inserted Genre: {genre_name}")
    else:
        lbl_result.config(text="Please enter a genre name to insert.")

# Button to insert a genre
btn_insert_genre = Button(root, text="Insert Genre", fg="green", command=insert_genre)
btn_insert_genre.grid(column=1, row=2, padx=10)

# Update an existing genre
def update_genre():
    genre_id = entry_id.get()
    new_genre_name = entry_name.get()
    if genre_id and new_genre_name:
        cursor.execute("UPDATE genre SET genre=? WHERE genre_Id=?", (new_genre_name, genre_id))
        connection.commit()
        lbl_result.config(text=f"Updated Genre ID {genre_id} to {new_genre_name}")
    else:
        lbl_result.config(text="Please enter both Genre ID and new Genre Name to update.")

# Button to update genre
btn_update_genre = Button(root, text="Update Genre", fg="orange", command=update_genre)
btn_update_genre.grid(column=2, row=2, padx=10)

# Delete a genre by ID
def delete_genre():
    genre_id = entry_id.get()
    if genre_id:
        cursor.execute("DELETE FROM genre WHERE genre_Id=?", (genre_id,))
        connection.commit()
        lbl_result.config(text=f"Deleted Genre ID {genre_id}")
    else:
        lbl_result.config(text="Please enter a Genre ID to delete.")

# Button to delete a genre
btn_delete_genre = Button(root, text="Delete Genre", fg="purple", command=delete_genre)
btn_delete_genre.grid(column=0, row=3, padx=10)

# Display movies with their genre and MPAA rating using JOINs
def fetch_movies_with_genre_rating():
    cursor.execute("""
    SELECT b.title, c.genre, d.mpaa FROM Movie_Ranking a 
    JOIN Movie_details b ON a.Movie_Id = b.movie_id
    JOIN Genre c ON a.genre_Id = c.genre_Id
    JOIN MPAA_Rating d ON a.mpaa_Id = d.mpaa_Id
    """)
    movies_data = cursor.fetchall()
    movies_text = "\n".join([f"Title: {row[0]}, Genre: {row[1]}, MPAA Rating: {row[2]}" for row in movies_data])
    lbl_result.config(text=movies_text)

# Button to display movies with genre and rating
btn_movies_with_genre_rating = Button(root, text="Movies with Genre & Rating", fg="blue", command=fetch_movies_with_genre_rating)
btn_movies_with_genre_rating.grid(column=0, row=4, padx=10)

# Subquery to fetch movies with high domestic gross
def fetch_high_gross_movies():
    cursor.execute("""
    SELECT title, domestic_gross FROM Movie_details 
    WHERE domestic_gross > (SELECT AVG(domestic_gross) FROM Movie_details)
    """)
    high_gross_movies = cursor.fetchall()
    high_gross_text = "\n".join([f"Title: {row[0]}, Domestic Gross: {row[1]}" for row in high_gross_movies])
    lbl_result.config(text=high_gross_text)

# Button to display high gross movies
btn_high_gross_movies = Button(root, text="High Grossing Movies", fg="brown", command=fetch_high_gross_movies)
btn_high_gross_movies.grid(column=1, row=4, padx=10)

# Commit and close SQLite connection when done
connection.commit()

# Execute Tkinter
root.mainloop()

# Close SQLite connection after Tkinter window is closed
connection.close()
