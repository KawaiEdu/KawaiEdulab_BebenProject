import os
import json

def baca_data_buku(fn):
    if os.path.exists(fn):
        with open(fn, 'r') as file:
            data = file.read()
            if data:
                return json.loads(data)
            else:
                return []
    else:
        return []

def tulis_data_buku(fn, data_buku):
    with open(fn, 'w') as file:
        file.write(json.dumps(data_buku, indent=4))

def tampilkan_buku(fn):
    data_buku = baca_data_buku(fn)
    if data_buku:
        print("\nDaftar Buku di Perpustakaan")
        for buku in data_buku:
            print(f"{buku['ID']} - {buku['Judul']} oleh {buku['Penulis']} ({buku['Tahun Terbit']})")
    else:
        print("Belum ada Buku di perpustakaan")

def tambah_buku(fn):
    
    id_buku = input("Masukkan id buku: ")
    judul_buku = input("Masukkan judul buku: ")
    penulis_buku = input("Masukkan penulis Buku: ")
    tahun_terbit = input("Masukkan tahun terbit buku: ")

   
    buku_baru = {
        "ID": id_buku,
        "Judul": judul_buku,
        "Penulis": penulis_buku,
        "Tahun Terbit": tahun_terbit
    }

    data_buku = baca_data_buku(fn)
    
    data_buku.append(buku_baru)

    tulis_data_buku(fn, data_buku)
    print("Buku berhasil ditambahkan!")
    
    data_buku = baca_data_buku(fn)
    data_buku.append(buku_baru)
    tulis_data_buku(fn,data_buku)
    print("buku berhasil ditambahkan")
    
def cari_buku(fn):
    id_buku = input("masukan id buku yang ingin dicari ")
    data_buku = baca_data_buku(fn)
    for buku in data_buku:
        if buku ["ID"] == id_buku:
            print(f"/nBuku ditemukan:{buku}")
            return
        print("buku tidak di temukan")
            
def main(): 
    file_name = "data_buku.txt"
    while True:
        print("\nMenu Perpustakaan:")
        print("1. Tambah buku")
        print("2. Tampilkan semua buku")
        print("3. Cari buku Berdasarkan id")
        print("4. Keluar")
        
        pilihan = input("npilih menu (1/2/3/4): ")
        if pilihan == '1':
            tambah_buku(file_name)
        elif pilihan == '2':
            tampilkan_buku(file_name)
        elif pilihan == '3':
            cari_buku(file_name)
        elif pilihan == '4':
            print("terima kasih telah memakai proram ini")
            break
        else:
            print("pilihan tidak valid coba lagi")

if __name__ =="__main__":
    main()
            
            