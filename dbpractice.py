#Database Practice :)
import sqlite3

#Connection allows us to connect 
#python to a SQL databe :)
connection = sqlite3.connect("./database.db")
#cursor allows us to interact with the SQL DB
cursor = connection.cursor()

query = """
SELECT * FROM Products;
"""

result = cursor.execute(query).fetchall()
print(f"OUR SQL RESULT: {result}")

#BOTTOM/END OF OUR CODE
connection.commit() #this commits our changes 
connection.close() #this disconnects our connection