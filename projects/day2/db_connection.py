import pymysql

def db_Connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="Lavanyaguturu@314",
        database="HDFCBank"
    )
print("db connected successfully.....") 