from helper.helper import Helper

class App:
    def __init__(self):
        self.helper = Helper()

    def create_data(self):
        data = self.helper.add_data()
        data['id'] = len(self.helper.database) + 1

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
        choice = int(input("Insert id: "))

        flag = False
        for data in self.helper.database:
            if choice == data['id']:
                self.helper.print_data(choice)
                flag = True

        if flag == False:
            self.helper.data_not_found()

    def update_data(self):
        choice = int(input("Insert id: "))
        
        flag = False
        for data in self.helper.database:
            if choice == data["id"]:
                data["name"] = input("Insert name: ")
                data["division"] = input("Insert division: ")
                data["age"] = input("Insert age: ")

                validation = self.helper.validate(data)
                if not validation:
                    return False
                
                self.helper.operation_success()
                flag = True

        self.helper.print_data(choice)
                

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
                self.helper.refresh_id()
                self.helper.print_all_data()

        if flag == False:
            self.helper.data_not_found()