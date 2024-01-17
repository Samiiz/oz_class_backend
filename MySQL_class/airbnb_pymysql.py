import pymysql

connection = pymysql.connect(
    host='localhost', 
    user='root', 
    password='samiiz', 
    db='airbnb',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

with connection.cursor() as cursor:
    # # 문제 1 : 새로운 제품 추가
    # sql = "INSERT INTO Products (productName, price, stockQuantity) VALUES (%s, %s, %s)"
    # cursor.execute(sql, ('Python Book', 10000, 10))
    # connection.commit()

    # 문제 2 : 고객 목록(제품 정보) 조회
    cursor.execute("SELECT * FROM Products")
    for book in cursor.fetchall():
        print(book)


cursor.close()