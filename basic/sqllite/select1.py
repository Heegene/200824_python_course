import sqlite3

# 전체 조회
def select_all_books():
    conn = sqlite3.connect('my_books.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM my_books")

    print('[1] 전체 데이터 출력')
    books = cur.fetchall()

    for each in books:
        print(each)

    conn.close()

if __name__ == "__main__":
    select_all_books()
    print("------------------------------")