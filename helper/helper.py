class Helper:
    def __init__(self):
        self.database = []
        data = {}

    def validate(self, data):
        if data['name'] == '' or data['division'] == '' or data['age'] == '':
            print()
            print("Data shouldn't empty")
            return False
        return True

    def print_all_data(self):
        for data in self.database:
            print()
            print(f'ID: {data["id"]}')
            print(f"Name: {data['name']}")
            print(f"Division: {data['division']}")
            print(f"Age: {data['age']}")
            print()     

    def input_name(self):
        var = input("Insert name: ")
        return var
    
    def input_division(self):
        var = input("Insert division: ")
        return var

    def input_age(self):
        var = input("Insert age: ")
        return var

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