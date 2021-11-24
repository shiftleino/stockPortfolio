class UserRepository:
    def __init__(self, connection):
        self.__connection = connection
        cursor = self.__connection.cursor()
        sql = """CREATE TABLE IF NOT EXISTS users (
        id integer primary key autoincrement, 
        username text UNIQUE, 
        password text);"""
        cursor.execute(sql)
        self.__connection.commit()

    def check_username_exists(self, username):
        """Checks if the given username exists.

        Args:
            username (string): Given username.

        Returns:
            boolean: Exists or does not.
        """
        cursor = self.__connection.cursor()
        sql = "SELECT username FROM users WHERE username=?"
        cursor.execute(sql, (username,))
        self.__connection.commit()
        rows = cursor.fetchall()
        if len(rows) > 0:
            return True
        else: 
            return False
    
    def correct_password(self, username, password):
        """Checks if the given username matches the given password.

        Args:
            username (string): Given usernname.
            password (string): Given password.
        
        Returns:
            boolean: True or False
        """
        cursor = self.__connection.cursor()
        sql = "SELECT password FROM users WHERE username=?;"
        cursor.execute(sql, (username,))
        self.__connection.commit()
        pw = cursor.fetchone()[0]
        if password==pw:
            return True
        else:
            return False

    def get_user_id(self, username):
        """Finds and returns the id of the given username.

        Args:
            username (string): Given username.

        Returns:
            integer: Id matching the given username.
        """
        cursor = self.__connection.cursor()
        sql = "SELECT id FROM users WHERE username=?;"
        cursor.execute(sql, (username,))
        self.__connection.commit()
        id = cursor.fetchone()[0]
        return id

    def add_user(self, username, password):
        """[summary]

        Args:
            username ([type]): [description]
            password ([type]): [description]
        Returns:
            boolean: If the insertion is successful.
        """
        cursor = self.__connection.cursor()
        sql = "INSERT INTO users (username, password) VALUES (?, ?);"
        try:
            cursor.execute(sql, (username, password,))
            self.__connection.commit()
            return True
        except Exception:
            return False
    
    def return_conn(self):
        return self.__connection