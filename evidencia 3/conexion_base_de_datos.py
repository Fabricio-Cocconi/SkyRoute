import mysql.connector
from config import host, user, password, database

def conectar():
    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )