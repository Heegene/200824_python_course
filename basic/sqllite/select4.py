import sqlite3

# 쪽수가 맣은 책을 조회함

def find_big_books():
    conn = sqlite3.connect('my_books.db')
    cur = conn.cursor()

    cur.execute("SELECT title, pages FROM my_books WHERE pages > 300")
    print('[4] 페이지 많은 책 출력')
    books = cur.fetchall()

    for book in books:
        print(book)
    conn.close()

if __name__ == "__main__":
    find_big_books()
    print("====================================")