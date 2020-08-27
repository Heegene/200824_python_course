import sqlite3

# 단일행 조회
def select_one_book():
    conn = sqlite3.connect('my_books.db')
    cur = conn.cursor()

    cur.execute("SELECT * FROM my_books")
    print('[3] 1개 데이터 조회하기')
    print(cur.fetchone())
    conn.close()

if __name__ == "__main__" :
    select_one_book()
    print("============================")