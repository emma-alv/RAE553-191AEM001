import sqlite3
from mimesis import Person

person = Person('en')

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, pass text)"
cursor.execute(create_table)

user = (1, 'emma-alv', 'p4ssw0rd')
insert_query = 'INSERT INTO users VALUES (?, ?, ?)'
cursor.execute(insert_query, user)

# Radom creation of Users
for i in range (2, 6):
    user = (i, person.username(), person.password())
    insert_query = 'INSERT INTO users VALUES (?, ?, ?)'
    cursor.execute(insert_query, user)

# Get list of user from the database
insert_query = 'SELECT * FROM users'
cursor.execute(insert_query)
users = cursor.fetchall()

for i in users:
    print(i)

connection.commit()
connection.close()
