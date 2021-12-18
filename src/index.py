from ui import gui
from database import db_connection
from services.user_service import UserService
from services.stock_service import StockService


def main():
    conn = db_connection.get_connection()
    user_service = UserService(conn)
    stock_service = StockService(conn)
    gui.start_gui(user_service, stock_service)


if __name__ == "__main__":
    main()
