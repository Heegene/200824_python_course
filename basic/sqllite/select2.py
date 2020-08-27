import sqlite3

#일부 조회용 함수
def select_some_books(number):
    conn = sqlite3.connect("my_books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM my_books")
    print('[2] 데이터 일부 출력')

    books = cur.fetchmany(number)

    for each in books:
        print(each)
        for num, item in enumerate(each):
            if num == 0:
                print("Subject ->", item) # 하나씩 제목 상세정보
            elif num == 1:
                print("Pub date ->", item)

    conn.close()

if __name__ == '__main__':
    select_some_books(3) # 위에서부터 3개만 나옴
    print("==================================================")
