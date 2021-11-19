from ui import gui
from repositories.user_repository import UserRepository
from database import db_connection
from entities.user import User

def main():
    conn = db_connection.get_connection()
    user_repo = UserRepository(conn)
    user = User()
    gui.start_gui(user_repo, user)

if __name__ == "__main__":
    main()