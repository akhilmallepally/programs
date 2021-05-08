from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host = "localhost",
        user = input("Enter user name: "),
        password = getpass("Enter password: "),
    ) as connection:
        print(connection)
except Error as e:
    print(e)