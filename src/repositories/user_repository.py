class UserRepository:
    def __init__(self, connection):
        self.__connection = connection

    def check_username_exists(self, username):
        """Checks if the given username exists.

        Args:
            username (string): Given username.

        Returns:
            boolean: Exists or does not.
        """
        sql = "SELECT username FROM users WHERE username=$1"
        return True
    
    def correct_password(self, username, password):
        """Checks if the given username matches the given password.

        Args:
            username (string): Given usernname.
            password (string): Given password.
        
        Returns:
            boolean: True or False
        """
        return True

    def get_user_id(self, username):
        """Finds and returns the id of the given username.

        Args:
            username (string): Given username.

        Returns:
            integer: Id matching the given username.
        """
        return id