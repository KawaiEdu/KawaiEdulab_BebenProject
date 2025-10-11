def write_note():
    note = input("masukan catatan anda ")
    with open("aqil news.txt", "a") as file:
        file.write(note + "\n")
    print("ur note has been saved")
    
def read_note():
    try:
        with open("aqil news.txt", "r") as file:
            print("\n catatan harian anda: ")
            print(file.read())
    except:
        print("no records have been record yet")

while True:
    print("\nPilih menu:")
    print("1. Tulis Catatan")
    print("2. Baca Catatan")
    print("3. Keluar")
    pilihan = input("Masukkan pilihan (1/2/3): ")
    
    if pilihan == "1":
        write_note()
    elif pilihan == "2":
        read_note()
    elif pilihan == "3":
        print("Terima kasih! Sampai jumpa.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")