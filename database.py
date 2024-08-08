#database
import mysql.connector as sqltor
import time
def database():
    con=sqltor.connect(host='localhost',user='root',password='TIGER',database='hosman')
    return con
