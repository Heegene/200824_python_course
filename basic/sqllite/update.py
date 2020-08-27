import sqlite3

from sqllite.select3 import select_one_book
from sqllite.select1 import select_all_books
# impport sqllite3.select3 이렇게 해도 되는데 그럼 밑에 select3.select_all 이런식으로 적어줘야함

# 데이터 수정
def update_books():
    conn = sqlite3.connect('my_books.db')
    cur = conn.cursor()

    # 데이터 수정 sql
    update_sql = 'UPDATE my_books SET recommendation = ? WHERE title= ?'

    # 수정 SQL 실행
    cur.execute(update_sql, (3, '개발자의 코드'))
    conn.commit()
    conn.close()


if __name__ == '__main__':
    select_one_book()
    update_books()
    print('[데이터 수정 완료] ==================')
    select_all_books()
