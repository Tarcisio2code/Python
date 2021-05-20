import psycopg2

connection = psycopg2.connect(database="postgres", user="postgres", password="senha", host="127.0.0.1", port="5432")
print("Connection to Database success!")

try:
    cursor = connection.cursor()
    cursor.execute('''select * from public."agenda"''')
    record = cursor.fetchall()
    print("\nTable content before delete")
    print(record)

    cursor.execute('''delete from public."agenda" where "id" = 1''')
    connection.commit()
    print("\n", cursor.rowcount, "Record deleted success full")

except psycopg2.DatabaseError as error:
    print("Database Error", error)

finally:
    if connection:
        cursor.close()
        connection.close()
