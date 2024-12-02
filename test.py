print("ketik selesai untk keluar dari program")

data_mahasiswa = []

while True:
    nama = input("masukkan nama : ")
    if nama.lower() == 'selesai':
        break
    mata_kuliah = input("masukkan mata kuliah : ")
    kelas = input("masukkan kelas : ")

    di_simpan = {"Nama": nama, "mata_kuliah": mata_kuliah, "Kelas": kelas}

    if nama in di_simpan:
        print("nama sudah ada")
        continue
    else:
        data_mahasiswa.append(di_simpan)
        print("nama belum ada")

with open("data_mahasiswa.txt", "w") as file:
    for data in data_mahasiswa:
        file.write(f"Nama : {data['Nama']}, Mata Kuliah : {data['mata_kuliah']}, Kelas : {data['Kelas']}")

print("data berhasil di simpan")