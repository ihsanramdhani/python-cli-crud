class Helper:
    def __init__(self):
        self.database = []

    def add_data(self, data):
        data["name"] = input("Insert name: ")
        data['division'] = input("Insert division: ")
        data["age"] = input("Insert age: ")

    def validate(self, data):
        if data['name'] == '' or data['division'] == '' or data['age'] == '':
            print()
            print("Data shouldn't empty")
            return False
        return True

    def print_data(self, choice):
        data = self.database[choice - 1]

        print()
        print(f'ID: {data["id"]}')
        print(f"Name: {data['name']}")
        print(f"Division: {data['division']}")
        print(f"Age: {data['age']}")
        print()

    def print_all_data(self):
        for data in self.database:
            print()
            print(f'ID: {data["id"]}')
            print(f"Name: {data['name']}")
            print(f"Division: {data['division']}")
            print(f"Age: {data['age']}")
            print()

    def refresh_id(self):
        index = 1
        for data in self.database:
            data['id'] = index
            index += 1

    def operation_success(self):
        print()
        print("Operation Success")
        print()

    def data_not_found(self):
        print()
        print("Data Not Found")
        print()

    def header(self):
        print(" ""\x1B[4m" +       
        "                                        "
        + "\x1B[0m")
        text = "Welcome to the CRUD Program"
        centered_text = text.center(40)
        print("|" + centered_text + "|")
        print("|Please choose any avalaible menu below: |")
        print("|1. Create Data                          |")
        print("|2. Get All Data                         |")
        print("|3. Get Specific Data                    |")
        print("|4. Update Data                          |")
        print("|5. Delete Data                          |")
        print("|"+
        "\x1B[4m" + "Type 'exit' to break the loop           "
        + "\x1B[0m" + "|")