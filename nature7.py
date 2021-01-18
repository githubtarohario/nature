import sqlite3
dbname='wikipedia.db'
conn=sqlite3.connect(dbname)
c = conn.cursor()
select_sql = "select title,contents from  wikipedia where title like '%中華人民共和国%'"
for row in c.execute(select_sql):
    print(row[0])
conn.close()

