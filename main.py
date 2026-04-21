from db import get_connection

def main():
    connection = get_connection()

    cursor = connection.cursor()
    cursor.execute("SELECT DATABASE()")
    print(cursor.fetchone())

    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()
