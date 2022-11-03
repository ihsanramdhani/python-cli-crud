from helper.helper import Helper
from core.app import App
from core.menu import Menu

class Main:
    def __init__(self):
        self.helper = Helper
        self.app = App(self.helper)
        self.menu = Menu(self.app)

    def run(self):

        print(" ""\x1B[4m"+
        "                                        "
        +"\x1B[0m")
        text = "Welcome to the CRUD Program"
        rata_tengah = text.center(40)
        print("|"+rata_tengah+"|")
        print("|Please choose any avalaible menu below: |")
        print("|1. Create Data                          |")
        print("|2. Get all data                         |")
        print("|3. Get 1 data                           |")
        print("|4. Update Data                          |")
        print("|"+
        "\x1B[4m"+"5. Delete data                          "
        +"\x1B[0m"+"|")

        choice = input("Pilih menu: ")
        self.menu.get_menu(choice)

m = Main()
while True:
    m.run()

# database = []

# def input_nama():
#     var = input("Masukkan nama: ")
#     return var

# def input_pekerjaan():
#     var = input("Masukkan pekerjaan: ")
#     return var

# def input_umur():
#     var = input("Masukkan umur: ")
#     return var

# def create_data():
#     nama = input_nama()
#     pekerjaan = input_pekerjaan()
#     umur = input_umur()
#     data = {
#         "id": len(database) + 1,
#         "nama": nama,
#         "pekerjaan": pekerjaan,
#         "umur": umur
#     }

#     database.append(data)

# def get_datas():
#     if database == []:
#         print("Databasenya kosong")
    
#     for data in database:
#         print(f'ID: {data["id"]}')
#         print(f"Nama: {data['nama']}")
#         print(f"Pekerjaan: {data['pekerjaan']}")
#         print(f"Umur: {data['umur']}")
#         print("")

# def get_data():
#     choice = input("Masukkan id: ")

#     flag = False
#     for data in database:
#         if int(choice) == data['id']:
#             print(f"Nama: {data['nama']}")
#             print(f"Pekerjaan: {data['pekerjaan']}")
#             print(f"Umur: {data['umur']}")
#             print("")
#             flag = True

#     if flag == False:
#         print("Data yang kamu cari ga ada")

# def update_data():
#     choice = input("Masukkan id: ")

#     flag = False
#     for data in database:
#         if int(choice) == data["id"]:
#             data["nama"] = input_nama()
#             data["pekerjaan"] = input_pekerjaan()
#             data["umur"] = input_umur()
#             print("")
#             print("Update data sukses")
#             print(f"Nama: {data['nama']}")
#             print(f"Pekerjaan: {data['pekerjaan']}")
#             print(f"Umur: {data['umur']}")
#             print("")
#             flag = True

#     if flag == False:
#         print("Kamu tidak bisa update data karena datanya ga ada")

# def delete_data():
#     choice = input("Masukkan id: ")

#     flag = False
#     for data in database:
#         if int(choice) == data["id"]:
#             database.remove(data)
#             print(f"ID no {data['id']} berhasil di delete")
#             flag = True
#             get_datas()

#     if flag == False:
#         print("Gabisa delete data yang dari awal juga ga ada")

# while True:
#     choice = input("Pilih: ")
#     if choice == "1":
#         create_data()
#     elif choice == "2":
#         get_datas()
#     elif choice == "3":
#         get_data()
#     elif choice == "4":
#         update_data()
#     elif choice == "5":
#         delete_data()