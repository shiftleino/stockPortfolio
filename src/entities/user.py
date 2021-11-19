class User:
    """Class fo the User.
    """
    def __init__(self, id=None, username=None, password=None):
        """Constructor for the User-class.

        Args:
            id (integer, optional): User id. Defaults to None.
            username (string, optional): Username. Defaults to None.
            password (string, optional): Password of the user. Defaults to None.
        """
        self.__id = id
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

    def set_username(self, username):
        """Sets the username of the User object to given username.

        Args:
            usernname (string): Given username.
        """
        self.__username = username
    
    def set_password(self, password):
        """Sets the password of the user to the given password.

        Args:
            password (string): Given password
        """
        self.__password = password

    def set_id(self, id): 
        """Sets the id of teh user to the given id.

        Args:
            id (integer): Given id.
        """
        self.__id = id
    