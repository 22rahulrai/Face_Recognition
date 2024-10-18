import sqlite3

conn = sqlite3.connect("database.db") # Connects to a SQLite database file named 'database.db'. If it doesn't exist, it will create the file.
print("Connected to database successfully") # Prints a message confirming successful connection to the database.

# Executes an SQL command to create a table named 'faces' with two columns:
# - 'name' column: stores the name of the person (TEXT data type, cannot be NULL).
# - 'encoding' column: stores the face encoding (a string representation of the face, also TEXT and cannot be NULL).
conn.execute('CREATE TABLE faces(name TEXT NOT NULL, encoding TEXT NOT NULL)')

print("Table Created Successfully") # Prints a confirmation that the table was created.

conn.close() # Closes the connection to the database.
