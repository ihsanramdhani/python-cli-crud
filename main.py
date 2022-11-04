from core.menu import Menu
from helper.helper import Helper

class Main:
    def __init__(self):
        self.menu = Menu()
        self.helper = Helper()

    def run(self):
        while True:
            self.helper.header()

            choice = input("Choose menu: ")
            
            if choice.lower() == "exit":
                break
            self.menu.get_menu(choice)

m = Main()
m.run()