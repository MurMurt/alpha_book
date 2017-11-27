import MySQLdb


class Connection:
    def __init__(self, user, passwd, db, host='localhost', charset='utf-8', use_unicode=True):
        self.user = user
        self.password = passwd
        self.db = db
        self.host = host
        self.charset = charset
        self.use_unicode = use_unicode
        self._connection = None
        self.cursor = None

    @property
    def connection(self):
        return self._connection

    def __enter__(self):
        self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._disconnect()

    def connect(self):
        if not self._connection:
            self._connection = MySQLdb.connect(
                host=self.host,
                user=self.user,
                passwd=self.password,
                db=self.db,
                charset="utf8",
                use_unicode=True
            )
            self.cursor = self._connection.cursor()

    def _disconnect(self):
        if self._connection:
            self._connection.close()

    def commit(self):
        self._connection.commit()