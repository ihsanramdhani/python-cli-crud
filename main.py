database = []

def input_nama():
    var = input("Masukkan nama: ")
    return var

def input_pekerjaan():
    var = input("Masukkan pekerjaan: ")
    return var

def input_umur():
    var = input("Masukkan umur: ")
    return var

def create_data():
    nama = input_nama()
    pekerjaan = input_pekerjaan()
    umur = input_umur()
    data = {
        "id": len(database) + 1,
        "nama": nama,
        "pekerjaan": pekerjaan,
        "umur": umur
    }

    database.append(data)

def get_datas():
    if database == []:
        print("Databasenya kosong")
    
    for data in database:
        print(f'ID: {data["id"]}')
        print(f"Nama: {data['nama']}")
        print(f"Pekerjaan: {data['pekerjaan']}")
        print(f"Umur: {data['umur']}")
        print("")

def get_data():
    choice = input("Masukkan id: ")

    flag = False
    for data in database:
        if int(choice) == data['id']:
            print(f"Nama: {data['nama']}")
            print(f"Pekerjaan: {data['pekerjaan']}")
            print(f"Umur: {data['umur']}")
            print("")
            flag = True

    if flag == False:
        print("Data yang kamu cari ga ada")

def update_data():
    choice = input("Masukkan id: ")

    flag = False
    for data in database:
        if int(choice) == data["id"]:
            data["nama"] = input_nama()
            data["pekerjaan"] = input_pekerjaan()
            data["umur"] = input_umur()
            print("")
            print("Update data sukses")
            print(f"Nama: {data['nama']}")
            print(f"Pekerjaan: {data['pekerjaan']}")
            print(f"Umur: {data['umur']}")
            print("")
            flag = True

    if flag == False:
        print("Kamu tidak bisa update data karena datanya ga ada")

def delete_data():
    choice = input("Masukkan id: ")

    flag = False
    for data in database:
        if int(choice) == data["id"]:
            database.remove(data)
            print(f"ID no {data['id']} berhasil di delete")
            flag = True
            get_datas()

    if flag == False:
        print("Gabisa delete data yang dari awal juga ga ada")

while True:
    choice = input("Pilih: ")
    if choice == "1":
        create_data()
    elif choice == "2":
        get_datas()
    elif choice == "3":
        get_data()
    elif choice == "4":
        update_data()
    elif choice == "5":
        delete_data()




            



