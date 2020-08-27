import sqlite3

def create_table():
    conn = sqlite3.connect('my_books.db') # 데이터베이스 커넥션 생성
    cur = conn.cursor()

    cur.execute('''CREATE TABLE my_books (
                                title text,
                                published_date text,
                                publisher text,
                                pages integer,
                                recommendation integer
                )'''
                )

    print("create_table Start3...")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()

