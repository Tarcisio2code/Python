import psycopg2

connection = psycopg2.connect(database="postgres", user="postgres", password="senha", host="127.0.0.1", port="5432")
print("Connection to Database success!")

try:
    cursor = connection.cursor()
    print("\nRecord before update")
    cursor.execute('''select * from public."agenda" where "id" = 1''')
    record = cursor.fetchone()
    print(record)

    cursor.execute('''update public."agenda" set "telefone" = '02188888888' where "id" = 1''')
    connection.commit()

    print("\nRecord updated success full")

    cursor = connection.cursor()
    print("\nRecord after update")
    cursor.execute('''select * from public."agenda" where "id" = 1''')
    record = cursor.fetchone()
    print(record)

except psycopg2.DatabaseError as error:
    print("Database Error", error)

finally:
    if connection:
        cursor.close()
        connection.close()
