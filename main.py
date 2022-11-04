from core.menu import Menu

class Main:
    def __init__(self):
        self.menu = Menu()

    def run(self):

        print(" ""\x1B[4m" +
        "                                        "
        + "\x1B[0m")
        text = "Welcome to the CRUD Program"
        centered_text = text.center(40)
        print("|" + centered_text + "|")
        print("|Please choose any avalaible menu below: |")
        print("|1. Create Data                          |")
        print("|2. Get all data                         |")
        print("|3. Get specific data                    |")
        print("|4. Update Data                          |")
        print("|"+
        "\x1B[4m" + "5. Delete data                          "
        + "\x1B[0m" + "|")

        choice = input("Choose menu: ")
        self.menu.get_menu(choice)

m = Main()
while True:
    m.run()