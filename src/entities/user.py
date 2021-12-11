class User:
    """Class for the User.
    """

    def __init__(self, user_id=None, username=None, password=None):
        """Constructor for the User class.

        Args:
            user_id (integer, optional): User id. Defaults to None.
            username (string, optional): Username. Defaults to None.
            password (string, optional): Password of the user. Defaults to None.
        """
        self.__id = user_id
        self.__username = username
        self.__password = password

    def return_id(self):
        """Returns user's id.

        Returns:
            integer: User's id.
        """
        return self.__id

    def return_username(self):
        """Returns user's username.

        Returns:
            string: Username.
        """
        return self.__username

    def return_password(self):
        """Returns user's password

        Returns:
            string: Password.
        """
        return self.__password

    def set_username(self, username):
        """Sets the username of the User object to given username.

        Args:
            username (string): Given username.
        """
        self.__username = username

    def set_password(self, password):
        """Sets the password of the user to the given password.

        Args:
            password (string): Given password.
        """
        self.__password = password

    def set_id(self, given_id):
        """Sets the id of the user to the given id.

        Args:
            given_id (integer): Given id.
        """
        self.__id = given_id
