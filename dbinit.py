#
# DB Query SQL 도움말
# - https://www.tutorialspoint.com/sql/sql-insert-query.htm
# - https://www.tutorialspoint.com/sql/sql-update-query.htm
import sqlite3

conn = sqlite3.connect('data1.db')
c = conn.cursor()

## 테이블 STUDENTS
try:
  c.execute('''CREATE TABLE username
               (name text)''')
  c.execute("INSERT INTO username VALUES ('kim')")
  conn.commit()
  print('Created username')
except:
  print('Skip username')
  pass



