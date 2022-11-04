from core.app import App

class Menu:
    def __init__(self):
        self.app = App()

    def get_menu(self, choice):
        if choice == "1":
            self.app.create_data()
        elif choice == "2":
            self.app.get_all_data()
        elif choice == "3":
            self.app.get_data()
        elif choice == "4":
            self.app.update_data()
        elif choice == "5":
            self.app.delete_data()