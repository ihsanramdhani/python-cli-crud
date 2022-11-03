from helper.helper import Helper

class App:
    def __init__(self, helper: Helper):
        self.database = []
        self.helper = helper

    def create_data(self):
        nama = self.helper.input_nama()
        pekerjaan = self.helper.input_pekerjaan()
        umur = self.helper.input_umur()

        data = {
            "id": len(self.database) + 1,
            "nama": nama,
            "pekerjaan": pekerjaan,
            "umur": umur
        }

        self.database.append(data)
        print()
        print("Data berhasil dibuat!")
        print()

    def get_datas(self):
        if self.database == []:
            print()
            print("Databasenya kosong")
            print()

        for data in self.database:
            print()
            print(f'ID: {data["id"]}')
            print(f"Nama: {data['nama']}")
            print(f"Pekerjaan: {data['pekerjaan']}")
            print(f"Umur: {data['umur']}")
            print()

    def get_data(self):
        choice = input("Masukkan id: ")

        flag = False
        for data in self.database:
            if int(choice) == data['id']:
                print()
                print(f"Nama: {data['nama']}")
                print(f"Pekerjaan: {data['pekerjaan']}")
                print(f"Umur: {data['umur']}")
                print()
                flag = True

        if flag == False:
            print()
            print("Data yang kamu cari ga ada!")
            print()

    def update_data(self):
        choice = input("Masukkan id: ")

        flag = False
        for data in self.database:
            if int(choice) == data["id"]:
                data["nama"] = self.helper.input_nama()
                data["pekerjaan"] = self.helper.input_pekerjaan()
                data["umur"] = self.helper.input_umur()
                print()
                print("Update data sukses")
                print()
                print(f"Nama: {data['nama']}")
                print(f"Pekerjaan: {data['pekerjaan']}")
                print(f"Umur: {data['umur']}")
                print()
                flag = True

        if flag == False:
            print()
            print("Kamu tidak bisa update data karena"
            " datanya ga ada")
            print()

    def delete_data(self):
        choice = input("Masukkan id: ")

        flag = False
        for data in self.database:
            if int(choice) == data["id"]:
                self.database.remove(data)
                print()
                print(f"ID no {data['id']} berhasil di delete")
                print()
                flag = True


        if flag == False:
            print()
            print("Gabisa delete data yang dari awal" 
            " juga ga ada!")
            print()





    

    
