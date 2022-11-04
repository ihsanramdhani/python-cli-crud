from core.menu import Menu
from helper.helper import Helper

class Main:
    def __init__(self):
        self.menu = Menu()
        self.helper = Helper()

    def run(self):
        self.helper.header()
        choice = input("Choose menu: ")
        self.menu.get_menu(choice)

m = Main()
while True:
    m.run()