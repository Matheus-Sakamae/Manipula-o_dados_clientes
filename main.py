import os
import mysql.connector
from dotenv import load_dotenv

def main():
    load_dotenv()

    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
    )

    cursor = connection.cursor()
    cursor.execute("SELECT DATABASE()")
    print(cursor.fetchone())

    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()
