import os
import json

def tulis_catatan(filename, data_buku):
    with open(filename, "w") as file:
        file.write(json.dumps(data_buku, indent=4))

def baca_catatan(filename):
    if os.path.exists(filename):
        with open(filename,"r") as file:
            data = file.read()
            if data :
                return json.loads(data)
            else:
                return[]
    else:
        return[]

def isibuku(filename):
    id_buku = input("massukkan id buku")
    judul_buku = input(" masukkan judul buku")
    tahunbuku = input("masukkan tahun buku")
    nama_penerbit = input("masukkan nama penerbit")

    isi_buku = {
        "id_buku":id_buku,
        "judul_buku":judul_buku,
        "tahunbuku":tahunbuku,
        "nama_penerbit":nama_penerbit
    }

    data_buku = baca_catatan(filename)
    data_buku.append(isi_buku)

    tulis_catatan(filename, data_buku)
    print("buku berhasil ditambahkan")

def cari_buku(filename):
    id_buku = input("masukkan id buku yang ingin di cari: ")

    data_buku = baca_catatan(filename)

    for buku in data_buku:
        if buku ["id_buku"]== id_buku:
            print(f"\nbuku di temukan:{buku}")
            return
        print("buku tidak ditemukan ")

def tampilkan_buku(filename):
    data_buku = baca_catatan(filename)

    if data_buku:
        print("\ndaftar buku di perpustakann")
        for buku in data_buku:
            print(f"{buku['id_buku']} - {buku['judul_buku']} oleh {buku['nama_penerbit']} ({buku['tahunbuku']})")
    else:
        print("Belum Ada Buku Yang Tersimpan")

def main():
    filename = "data_buku.txt"

    while True:
        print("\nmenu perpustakaan")
        print("1. isi buku")
        print("2. cari buku")
        print("3. tampilkan buku")
        print("4. keluar")

        pilihan = input("\npilih menu 1,2,3,4 : ")

        if pilihan =='1':
            isibuku(filename)
        elif pilihan =='2':
            cari_buku(filename)
        elif pilihan =='3':
            tampilkan_buku(filename)
        elif pilihan =='4':
            print("terima kasih telah memakai progam ini !!")
            break
        else: 
            print("pilihan tidak valid")
            
if __name__ == "__main__":
    main()