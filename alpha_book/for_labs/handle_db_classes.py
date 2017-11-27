from alpha_book.for_labs.connect_class import Connection


class User:
    def __init__(self, connection: Connection, name, age):
        self.name = name
        self.age = age
        self.connection = connection

    def save(self):
        self.connection.cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s);",
                  (self.name, self.age))
        self.connection.commit()

    def show_table(self):
        self.connection.cursor.execute('SELECT * FROM users')
        entries = self.connection.cursor.fetchall()
        for e in entries:
            print(e)


connect = Connection(host="localhost",
                     user='ab_user',
                     passwd='alpha',
                     db='alpha_book_db',
                     charset="utf8",
                     use_unicode=True)

with connect:
    user = User(connection=connect, name='Олег', age=20)
    user.save()
    user.show_table()


connect.cursor.execute('SELECT * FROM users')
