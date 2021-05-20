import psycopg2

connection = psycopg2.connect(database="postgres", user="postgres", password="senha", host="127.0.0.1", port="5432")
print("Connection to Database success!")

try:
    cursor = connection.cursor()
    cursor.execute('''select * from public."agenda"''')
    alldata = cursor.fetchall()
    print("Table contents")
    print(alldata)

    cursor.execute('''select * from public."agenda" where "id" = 1''')
    register = cursor.fetchone()
    print("\nRegisters with ID = 1")
    print(register)

except psycopg2.DatabaseError as error:
    print("Database Error", error)

finally:
    if connection:
        cursor.close()
        connection.close()
