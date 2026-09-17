import mysql.connector
def get_connection():
    connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="ex"
    )
    return connection
# print("db succsessfully connected")
