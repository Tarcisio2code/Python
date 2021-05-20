import psycopg2

connection = psycopg2.connect(database="postgres", user="postgres", password="senha", host="127.0.0.1", port="5432")
print("Connection to Database success!")

cursor = connection.cursor()
try:
    cursor.execute('''CREATE TABLE Agenda 
                        (ID INT PRIMARY KEY NOT NULL,
                        Nome TEXT NOT NULL,
                        Telefone CHAR(12));''')

    connection.commit()
    print("Table create success full")

    # Insert first data
    cursor.execute('''INSERT INTO public."agenda" ("id", "nome", "telefone") 
                        VALUES (1, 'Pessoa 1', '02199999999');''')
    connection.commit()
    print("Insert data success full!")

except psycopg2.DatabaseError as error:
    print("Database Error", error)

finally:
    if connection:
        cursor.close()
        connection.close()
