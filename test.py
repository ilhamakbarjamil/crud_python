print("ketik selesai untk keluar dari program")

data_mahasiswa = [] #ini adalah variabel yang di gubnalan untuk menyimpan data mahassiwa

while True:
    nama = input("masukkan nama : ") #untuk menginput nama menggunakna variabel nama
    if nama.lower() == 'selesai': # kondisi ketika mengetik selesai maka program berhenti
        break
    mata_kuliah = input("masukkan mata kuliah : ")# ini sama untuk menginput mata_kuliah
    kelas = input("masukkan kelas : ") # ini juga sama untuk menginput kelas

    nama_sudah_ada = False # ini adalah boolean
    for data in data_mahasiswa: # saya menggunbakan for karena keanggotaan yaitu data_mahasiswa
        if data['nama'] == nama: # mengecek kesamaan antara variabel nama dengan variabel nama juga yang ada di data_mahasiswa
            nama_sudah_ada = True # mengganti nilai menjadi true, karena ada kesamaan
            break

    if nama_sudah_ada:
        print("nama sudah ada")
    else:
        di_simpan = {"nama": nama, "mata kuliah": mata_kuliah, "kelas": kelas} # jika tidak ada kesamaan maka data akan di simpan
        data_mahasiswa.append(di_simpan)
        print("data di tambahkan")

with open("data_mahasiswa.txt", "a") as file: # membuka file data_mahasiswa.txt, dan saya menggunakan tipe a supaya tidak terhapus / mulai ulang
    for data in data_mahasiswa: # menggunakan loop for untuk mengecek data pada data_mahasiswa
        file.write(f"Nama : {data['nama']}, Mata Kuliah : {data['mata kuliah']}, Kelas : {data['kelas']}\n") # data di tambahkan ke data_mahasiswa.txt

print("data berhasil di simpan") # pada akhir program ada tulisan data berhasil di simpan