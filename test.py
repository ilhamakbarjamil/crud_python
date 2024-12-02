print("ketik selesai untk keluar dari program")

data_mahasiswa = []

while True:
    nama = input("masukkan nama : ")
    if nama.lower() == 'selesai':
        break
    mata_kuliah = input("masukkan mata kuliah : ")
    kelas = input("masukkan kelas : ")

    nama_sudah_ada = False
    for data in data_mahasiswa:
        if data['nama'] == nama:
            nama_sudah_ada = True
            break

    if nama_sudah_ada:
        print("nama sudah ada")
    else:
        di_simpan = {"nama": nama, "mata kuliah": mata_kuliah, "kelas": kelas}
        

with open("data_mahasiswa.txt", "a") as file:
    for data in data_mahasiswa:
        file.write(f"Nama : {data['Nama']}, Mata Kuliah : {data['mata kuliah']}, Kelas : {data['Kelas']}")

print("data berhasil di simpan")