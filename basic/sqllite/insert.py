import sqlite3

# 데이터 입력

def insert_books():
    conn = sqlite3.connect('my_books.db')
    cur = conn.cursor()
    # 데이터 입력
    cur.execute("INSERT INTO my_books VALUES ('개발자의 코드', '2019.02.28', 'A', 200, 0)")
    # 데이터 입력 sql
    insert_sql = 'INSERT INTO my_books VALUES(?, ?, ?, ?, ?)'

    # 튜플을 이용한 데이터 입력
    cur.execute(insert_sql, ('클린 코드', '2015.03.04', 'B', 584, 1))

    # 책의 정보를 담은 튜플의 리스트
    books = [
        ('빅데이터 마케팅', '2018.07.02', 'A', 296, 1),
        ('구글', '2017.02.10', 'B', 526, 0),
        ('강의력', '2012.12.12', 'A', 248, 1)
    ]

    # 여러 데이터 입력
    cur.executemany(insert_sql, books)
    print("insert_books start3...")
    conn.commit()
    conn.close()

if __name__ == '__main__':
    insert_books()
