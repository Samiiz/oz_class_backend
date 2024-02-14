import pymysql

# 데이터 베이스 연결
connection = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='samiiz',
    db='classicmodels',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

# CRUD 해보기

## select * from
def get_customers():
    cursor = connection.cursor()

    sql = "select * from customers"
    cursor.execute(sql)

    customers = cursor.fetchone()
    print("customers : ", customers)
    print("customers : ", customers['customerNumber'])
    print("customers : ", customers['customerName'])
    print("customers : ", customers['country'])
    cursor.close()



## insert into
def add_customer():
    cursor = connection.cursor()
    name = 'sanghoon'
    LastName = 'park'
    sql = f"insert into customers(customerNumber, customerName, contactLastName) values({1005}, '{name}', '{LastName}')"
    cursor.execute(sql)
    connection.commit()
    cursor.close()

# add_customer()



## update set
def update_customer():
    cursor = connection.cursor()
    update_name = 'update_sanghoon'
    contactLastName = 'update_park'
    sql = f"update customers set customerName='{update_name}', contactLastName='{contactLastName}' where customerNumber=1000"
    cursor.execute(sql)
    connection.commit()
    cursor.close()

# update_customer()



## delete from
def delete_customer():
    cursor = connection.cursor()
    sql = "delete from customers where customerNumber=1004"
    cursor.execute(sql)
    connection.commit()
    cursor.close()

delete_customer()