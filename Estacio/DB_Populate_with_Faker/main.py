from faker import Faker
import psycopg2

connection = psycopg2.connect(database="postgres", user="postgres", password="senha", host="127.0.0.1", port="5432")
print("Connection to Database success!")

cursor = connection.cursor()
fake = Faker("pt_BR")

try:
    n = 10
    for i in range(n):
        code = i+10
        name = 'produto_'+str(i+1)
        price = fake.pyfloat(left_digits=3, right_digits=3, positive=True,
                             min_value=5, max_value=1000)
        print(price)
        print(name)

        cmdSQL = '''INSERT INTO public."PRODUTO" ("CODIGO", "NOME", "PRECO") VALUES (%s,%s,%s)'''
        record = (code, name, price)
        cursor.execute(cmdSQL, record)
        connection.commit()
    print("Database populate success full")

except psycopg2.DatabaseError as error:
    print("Database error")

finally:
    if connection:
        cursor.close()
        connection.close()