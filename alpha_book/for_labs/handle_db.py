import MySQLdb

# open connection

db = MySQLdb.connect(
    host="localhost",
    user='ab_user',
    passwd='alpha',
    db='alpha_book_db',
    charset="utf8",
    use_unicode=True
)

cursr = db.cursor()

'''INSERT INTO
    `users` (`name`, `age`)
VALUES
    ('Витя', 777)'''
cursr.execute('INSERT INTO users (name, age) VALUES (%s, %s);', ('Витя', int(777)))
db.commit()

cursr.execute('SELECT * FROM users')
entries = cursr.fetchall()

for e in entries:
    print(e)

cursr.execute('DELETE FROM users')
db.commit()

cursr.execute('SELECT * FROM users')
entries = cursr.fetchall()


for e in entries:
    print(e)

cursr.close()
db.close()
