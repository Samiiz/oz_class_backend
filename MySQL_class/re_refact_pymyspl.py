import pymysql

# 쿼리문 실행 함수
def execute_query(connection, query, args=None):

    with connection.cursor() as cursor:
        cursor.execute(query, args or ())
        
        # 쿼리문의 시작이 SELECT일 경우 
        if query.strip().upper().startswith('SELECT'):
            # SELECT 쿼리의 실행 결과를 모두 반환한다.
            return cursor.fetchall()
        # 아닐시 INSERT, UPDATE, DELETE 라고 판단하여 커밋을 진행한다.
        else:
            connection.commit()

def main():
    # pymysql.connect를 이용하여 데이터베이스 연결을 위한 정보를 적는다.
    connection = pymysql.connect(host='localhost',
                                 user='username',
                                 password='password',
                                 db='database_name',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        # i라는 변수에 input을 이용 하여 SELECT, INSERT, UPDATE, DELETE를 입력하여 CRUD중 수행할 작없을 선택 하도록 한다.
        i = input("[CRUD]수행할 작업을 선택하세요: ").strip().upper()

        # SELECT입력시
        if i.startswith('SELECT'):
            # 쿼리문 안에 들어갈 내용을 입력하도록 한다.
            table_name = input("SELECT 작업을 수행할 테이블의 이름을 입력하세요: ").strip()
            select_columns = input("SELECT 구문에 사용할 컬럼들을 입력하세요 (예: column1, column2): ").strip()
            join_condition = input("JOIN 구문에 사용할 조인 조건을 입력하세요 (예: table2 ON table1.column = table2.column, 미사용 시 Enter): ").strip()
            where_condition = input("WHERE 조건을 입력하세요 (미사용 시 Enter): ").strip()
            group_by_columns = input("GROUP BY 구문에 사용할 컬럼들을 입력하세요 (예: column1, column2, 미사용 시 Enter): ").strip()
            having_condition = input("HAVING 조건을 입력하세요 (미사용 시 Enter): ").strip()
            limit_condition = input("LIMIT 조건을 입력하세요 (미사용 시 Enter): ").strip()

            query = f"SELECT {select_columns} FROM {table_name}"

            # 각각 추가 작업이 있을경우 해당내용을 쿼리문에 추가한다.
            if join_condition:
                query += f" JOIN {join_condition}"
            if where_condition:
                query += f" WHERE {where_condition}"
            if group_by_columns:
                query += f" GROUP BY {group_by_columns}"
            if having_condition:
                query += f" HAVING {having_condition}"
            if limit_condition:
                query += f" LIMIT {limit_condition}"
            
            # result변수에 SELECT 쿼리문을 실행하는 함수를 할당한다. 
            result = execute_query(connection, query)

            # 연산 결과를 출력한다.
            print("SELECT 연산 결과:")
            for row in result:
                print(row)

        elif i == 'INSERT':
            table_name = input("INSERT 작업을 수행할 테이블의 이름을 입력하세요: ").strip()
            column_names = input("삽입할 컬럼들을 입력하세요 (예: column1, column2): ").strip()
            values = input("VALUES를 입력하세요 (예: 'value1', 'value2'): ").strip()
            execute_query(connection, f"INSERT INTO {table_name} ({column_names}) VALUES ({values})")
            print("INSERT 연산 수행됨.")

        elif i == 'UPDATE':
            table_name = input("UPDATE 작업을 수행할 테이블의 이름을 입력하세요: ").strip()
            set_condition = input("SET 조건을 입력하세요 (예: column1='new_value', column2='new_value'): ").strip()
            where_condition = input("WHERE 조건을 입력하세요 (미사용 시 Enter): ").strip()

            query = f"UPDATE {table_name} SET {set_condition}"
            if where_condition:
                query += f" WHERE {where_condition}"

            execute_query(connection, query)
            print("UPDATE 연산 수행됨.")

        elif i == 'DELETE':
            table_name = input("DELETE 작업을 수행할 테이블의 이름을 입력하세요: ").strip()
            where_condition = input("WHERE 조건을 입력하세요 (미사용 시 Enter): ").strip()

            query = f"DELETE FROM {table_name}"
            if where_condition:
                query += f" WHERE {where_condition}"

            execute_query(connection, query)
            print("DELETE 연산 수행됨.")

        elif i == 'OTHER':
            query = input("필요에 따라 f-string을 사용하세요")

            # 수행
            execute_query(connection, query)
            print("OTHER_OPERATION 연산 수행됨.")

        else:
            # OTHER 을 사용하여 직접입력도 가능하게 안내한다.
            print("잘못된 작업 선택!\nCRUD외의 다른 작업을 원할시 \"OTHER\"를 입력하세요.")

    # 예외 발생시 에러가 발생했다고 안내한다.
    except Exception as e:
        print(f"에러 발생: {e}")
    # 작업 종료시 데이터베이스와의 연결을 끊는다.
    finally:
        connection.close()

if __name__ == "__main__":
    main()