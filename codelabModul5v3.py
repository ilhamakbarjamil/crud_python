import pandas as pd

file_name = 'data_mahasiswa.xlsx'

def load_data():
    try:
        return pd.read_excel(file_name)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Nama", "Semester", "Mata Kuliah"])
    except ValueError:
        return pd.DataFrame(columns=["Nama", "Semester", "Mata Kuliah"])

def save_data(df):
    df.to_excel(file_name, index=False)
    print(f"Data telah disimpan ke dalam file {file_name}")

def main():
    print("Masukkan data mahasiswa. Ketik 'selesai' pada nama untuk mengakhiri.")
    
    data = load_data()
    
    if "Nama" not in data.columns:
        data = pd.DataFrame(columns=["Nama", "Semester", "Mata Kuliah"])

    while True:
        nama = input("Masukkan Nama: ").strip()
        if nama.lower() == "selesai":
            break

        if nama in data['Nama'].values:
            print(f"Nama {nama} sudah ada, masukkan nama yang berbeda.")
            continue
        
        semester = input("Masukkan Semester: ").strip()
        mata_kuliah = input("Masukkan Mata Kuliah: ").strip()
        
        new_row = {"Nama": nama, "Semester": semester, "Mata Kuliah": mata_kuliah}
        data = pd.concat([data, pd.DataFrame([new_row])], ignore_index=True)
        print("Data berhasil ditambahkan!")

    save_data(data)

if __name__ == "__main__":
    main()
