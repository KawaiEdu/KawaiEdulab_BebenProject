def tampilkan_menu():
    print("\nSelamat datang di program daftar tugas")
    print("1.Tambah Tugas")
    print("2.Tampilkan Daftar Tugas")
    print("3.Hapus Tugas")
    print("4.Hapus semua tugas ")
    print("5.Simpan Daftar ke File")
    print("6.Muat Daftar dari File")
    print("7.Keluar")
    #1
def tambah_tugas(daftar):
    tugas = input("masukan nama tugas: ")
    daftar.append(tugas)
    print("{} berhasil ditambakan ke daftar tugas.".format(tugas))
    #2
def tampilkan_daftar(daftar):
    if daftar:
        print("\nDaftar Tugas:")
        for i, tugas in enumerate(daftar, start=1):
            print("{}. {}".format(i, tugas))
    else:
        print("Daftar tugas kosong")
    #3
def hapus_tugas(daftar):
    tampilkan_daftar(daftar)
    try:
        nomor = int(input("masukan nomor tugas yang ingin di hapus:"))
        if 1 <= nomor <= len(daftar):
            tugas = daftar.pop(nomor - 1)
            print("{} berhasil diapus dari daftar tugas.".format(tugas))
        else:
            print("Nomor tugas tidak valid.")     
    except ValueError:
            print("Input harus angka")
    #4
def hapus_semua_tugas(daftar):
    tampilkan_daftar(daftar)
    konfirmasi = input("Apakah Anda yakin ingin menghapus semua tugas? (y/n): ").lower()
    if konfirmasi == 'y':
        del daftar[:]  
        print("Semua tugas berhasil dihapus.")
    else:
        print("Penghapusan dibatalkan.")
    #5
def simpan_daftar(daftar):
    try:
        with open("daftar_tugas.txt", "w") as file:
            for tugas in daftar:
                file.write(tugas + "\n")
            print("Daftar tugas berhasil disimpan ke file.")
    except Exception as e:
        print("Terjadi kesalahan saat menyimpan: {}".format(e))
    #6
def muat_daftar():
    try:
        with open("daftar_tugas.txt", "r") as file:
         daftar = [line.strip() for line in file]
         print("daftar tugas berhasil dimuat dari file")
         return daftar
    except IOError:
        print(" file daftar tugas tidak ditemukan. membuat daftar baru.")
        return []
    except Exception as e:
        print(" Terjadi kesalahan saat memuat: {}".format(e))
        return []
    #7
def main():
        daftar = muat_daftar()
        
        while True:
            tampilkan_menu()
            pilihan = input("masukan pilihan (1-7):")
            
            if pilihan == "1":
                tambah_tugas(daftar)
            elif pilihan == "2":
                tampilkan_daftar(daftar)
            elif pilihan == "3":
                hapus_tugas(daftar)
            elif pilihan == "4":
                hapus_semua_tugas(daftar)
            elif pilihan == "5":
                simpan_daftar(daftar)
            elif pilihan == "6":
                daftar = muat_daftar()
            elif pilihan == "7":
                print("terima kasih sampai jumpa!")
                break
            else:
                print("pilihan tidak valid silakan coba lagi")
                
if __name__=="__main__": 
    main()