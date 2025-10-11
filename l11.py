daftar_belanja = []

while True:
    print("\n daftar belanja:", daftar_belanja)
    print("1. tambah item")
    print("2. hapus item")
    print("3. keluar")
    choice = input("masukan opsi mu: ")
    
    if choice == "1":
        item = input("masukan item yang ingin di tambahkan ")
        daftar_belanja.append(item)
    elif choice == "2":
        item = input("masukan yang ingin di hapus ") 
        if item in daftar_belanja:
            daftar_belanja.remove(item)
        else:
            print("item tidak di temukan")
    elif choice == "3":
        print("terimah kasih atas menggunakan program ini")
        break
    else:
        print("your choice is false, please input again")
        