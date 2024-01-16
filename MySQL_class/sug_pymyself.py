import pymysql

def main():
    # 데이터베이스 연결 설정
    connection = pymysql.connect(host='localhost',
                                 user='username',
                                 password='password',
                                 db='database_name',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    
    try:
        # SELECT 연산
        with connection.cursor() as cursor:
            sql = "SELECT * FROM table_name"
            cursor.execute(sql)
            result = cursor.fetchall()
            print("SELECT 연산 결과:")
            for row in result:
                print(row)

        # INSERT 연산
        with connection.cursor() as cursor:
            sql = "INSERT INTO table_name (column1, column2) VALUES (%s, %s)"
            cursor.execute(sql, ('data1', 'data2'))
        connection.commit()
        print("INSERT 연산 수행됨.")

        # UPDATE 연산
        with connection.cursor() as cursor:
            sql = "UPDATE table_name SET column1=%s WHERE column2=%s"
            cursor.execute(sql, ('new_data', 'criteria'))
        connection.commit()
        print("UPDATE 연산 수행됨.")

        # DELETE 연산
        with connection.cursor() as cursor:
            sql = "DELETE FROM table_name WHERE column_name=%s"
            cursor.execute(sql, ('criteria',))
        connection.commit()
        print("DELETE 연산 수행됨.")

    finally:
        # 데이터베이스 연결 종료
        connection.close()

if __name__ == "__main__":
    main()