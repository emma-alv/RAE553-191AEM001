import sqlite3

#Stablish connection with the database
connection = sqlite3.connect("data.db")
cursor = connection.cursor()

# Create table to storage users data
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

# Create table to storage items data
create_table = "CREATE TABLE IF NOT EXISTS items (name text PRIMARY KEY, price real)"
cursor.execute(create_table)

# Save changes and close connection
connection.commit()
connection.close()
