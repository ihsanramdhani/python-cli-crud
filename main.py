database = []

def create_data():
    input_nama = input("Masukkan nama: ")
    input_pekerjaan = input("Masukkan pekerjaan: ")
    input_umur = input("Masukkan umur: ")

    data = {
        "id": len(database) + 1,
        "nama": input_nama,
        "pekerjaan": input_pekerjaan,
        "umur": input_umur
    }

    database.append(data)

def get_datas():
    if database == []:
        print("Ga ada data di databasenya bro")
    
    for data in database:
        print(f'{data["id"]}.')
        print(f"Nama: {data['nama']}")
        print(f"Pekerjaan: {data['pekerjaan']}")
        print(f"Umur: {data['umur']}")
        print("")

while True:
    choice = input("Pilih: ")
    if choice == "1":
        create_data()
    elif choice == "2":
        datas = get_datas()



            



