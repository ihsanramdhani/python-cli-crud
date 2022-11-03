from core.app import App

class Menu:
    def __init__(self, app:App):
        self.app = app

    def get_menu(self, choice):
        if choice == "1":
            self.app.create_data()
        elif choice == "2":
            self.app.get_datas()
        elif choice == "3":
            self.app.get_data()
        elif choice == "4":
            self.app.update_data()
        elif choice == "5":
            self.app.delete_data()