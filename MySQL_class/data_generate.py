import mysql.connector
from faker import Faker
import random

# 1. MYSQL 연결 설정
db_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='samiiz',
    database='sample'
)

# 2. MYSQL 연결
cursor = db_connection.cursor()
faker = Faker()

# 100명의 users data 생성

for _ in range(100):
    username = faker.user_name()
    email = faker.email()

    sql = "insert into users(user_name, email) values(%s, %s)"
    values = (username, email)
    cursor.execute(sql, values)

# user_id 불러오기
cursor.execute("select user_id from users")
valid_user_id = [row[0] for row in cursor.fetchall()]

# 100개의 orders data 생성

for _ in range(100):
    user_id = random.choice(valid_user_id)
    product_name = faker.word()
    quantity = random.randint(1, 10)

    try:    
        sql = "insert into orders(user_id, product_name, quantity) values(%s, %s, %s)"
        values = (user_id, product_name, quantity)
        cursor.execute(sql, values)
    except:
        pass




db_connection.commit()
cursor.close()
db_connection.close()



