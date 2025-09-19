# import mysql.connector
import pymysql
def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="Lavanyaguturu@314",
        database="StudentMnagementSystem"
    )
print("database connected successfully")
