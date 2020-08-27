import cx_Oracle
dsn = cx_Oracle.makedsn("localhost", 1521, "xe")
con = cx_Oracle.connect("scott", "tiger", dsn)
cursor = con.cursor()

cursor.execute("""SELECT * FROM dept""")
# row = cursor.fetchone()
row = cursor.fetchall()
print(row)

con.close()
