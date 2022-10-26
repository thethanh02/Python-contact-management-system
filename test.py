# Import module
import sqlite3

# Connecting to sqlite
conn = sqlite3.connect('geeks2.db')

# Creating a cursor object using the
# cursor() method
cursor = conn.cursor()

# Creating table
table ="""CREATE TABLE STUDENT(NAME VARCHAR(255), CLASS VARCHAR(255),
SECTION INT);"""
cursor.execute(table)

# Queries to INSERT records.
cursor.execute('''INSERT INTO STUDENT VALUES ('Raju', '7th', 1)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Shyam', '8th', 3)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Baburao', '9th', 2)''')

# Display data inserted
print("Data Inserted in the table: ")
data=cursor.execute('''SELECT * FROM STUDENT''')
for row in data:
	print(row)

# Commit your changes in the database	
conn.commit()

# Closing the connection
conn.close()
