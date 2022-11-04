from helper.helper import Helper

class App:
    def __init__(self):
        self.helper = Helper()

    def create_data(self):
        name = self.helper.input_name()
        division = self.helper.input_division()
        age = self.helper.input_age()

        data = {
            "id": len(self.helper.database) + 1,
            "name": name,
            "division": division,
            "age": age
        }

        validation = self.helper.validate(data)
        if not validation:
            return False

        self.helper.database.append(data)
        self.helper.operation_success()

    def get_all_data(self):
        if self.helper.database == []:
            self.helper.data_not_found()
        self.helper.print_all_data()

    def get_data(self):
        choice = input("Insert id: ")

        flag = False
        for data in self.helper.database:
            if int(choice) == data['id']:
                print()
                print(f'ID: {data["id"]}')
                print(f"Name: {data['name']}")
                print(f"Division: {data['division']}")
                print(f"Age: {data['age']}")
                print()
                flag = True

        if flag == False:
            self.helper.data_not_found()

    def update_data(self):
        choice = input("Insert id: ")
        
        flag = False
        for data in self.helper.database:
            if int(choice) == data["id"]:
                name = self.helper.input_name()
                division = self.helper.input_division()
                age = self.helper.input_age()

                data = {
                    "id": data['id'],
                    "name": name,
                    "division": division,
                    "age": age
                }
                validation = self.helper.validate(data)
                if not validation:
                    return False
                    
                self.helper.operation_success()

                print()
                print(f'ID: {data["id"]}')
                print(f"Name: {data['name']}")
                print(f"Division: {data['division']}")
                print(f"Age: {data['age']}")
                print()
                flag = True

        if flag == False:
            self.helper.data_not_found()

    def delete_data(self):
        choice = input("Insert id: ")

        flag = False
        for data in self.helper.database:
            if int(choice) == data["id"]:
                self.helper.database.remove(data)
                self.helper.operation_success()
                flag = True
                self.helper.print_all_data()

        if flag == False:
            self.helper.data_not_found()


