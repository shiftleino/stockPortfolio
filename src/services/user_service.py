from repositories.user_repository import UserRepository
from entities.user import User


class UserService:
    """Class for the application logic of the user.
    """

    def __init__(self, conn):
        """Constructor for the class.

        Args:
            conn (SQLite3 Connection): The connection to the database.
        """
        self.__conn = conn
        self.__repo = UserRepository(self.__conn)
        self.__user = User()

    def add_user(self, username, password):
        """Method for adding a user to the database.

        Args:
            username (string): The username (must be unique).
            password (string): The password.

        Returns:
            boolean: If the addition was successful or not.
        """
        result = self.__repo.add_user(username, password)
        return result

    def login(self, username, password):
        """Logs in the user if username and password correct.

        Args:
            username (string): The given username.
            password (string): The given password.

        Returns:
            boolean: If the login was successful or not.
        """
        if self.__repo.check_username_exists(username) and self.__repo.correct_password(username, password):
            user_id = self.__repo.get_user_id(username)
            self.__user.set_username(username)
            self.__user.set_password(password)
            self.__user.set_id(user_id)
            return True
        return False

    def get_id(self, username):
        """Method for getting the id of the user.

        Args:
            username (string): The username of the user.

        Returns:
            integer: The user id of the user.
        """
        user_id = self.__repo.get_user_id(username)
        return user_id

    def set_username(self, username):
        """Sets the username to given username.

        Args:
            username (string): The given username.
        """
        self.__user.set_username(username)

    def set_password(self, password):
        """Sets the password to given password.

        Args:
            password (string): The given password.
        """
        self.__user.set_password(password)

    def set_id(self, user_id):
        """Sets the id to given id.

        Args:
            user_id (integer): The given id.
        """
        self.__user.set_id(user_id)

    def return_username(self):
        """Method for returning the username.

        Returns:
            string: The user's username.
        """
        return self.__user.return_username()

    def return_password(self):
        """Method for returning the password.

        Returns:
            string: The user's password.
        """
        return self.__user.return_password()

    def return_id(self):
        """Method for returning the id.

        Returns:
            integer: The user's id.
        """
        return self.__user.return_id()
