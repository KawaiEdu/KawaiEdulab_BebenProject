while True:
    print("\nMENU: \n 1. Informasi pribadi \n 2. Pelajaran yang kau sukai \n 3. keluar")
    pilih = input("Pilih: ").strip()
    if not pilih:
        continue
    if pilih == "1":
        print("Masukan informasi pribadi anda 100%' aman")
        nama = input("masukan nama: ") 
        usia = int(input("masukan usia: "))
        info_credit = input("masukan info credit: ")
        bni = input("masukan password BNI: ")
        cloth = input("masukan genre baju yang kamu sukai: ")
        money = input("apakah dompet mu lebih sering penuh atau kosong: ")
        rdm = input("apakah anda kecewa kerja di sini: ")
        ip = input("masukan IP rumah anda: ")
        pcr = input("masukan nama pacar mu yang baru: ")
        ruby = input("woi jadi belajar Ruby atau nga?: ")
        uang = input("berapa banyak uang tabunganmu sekarang: ")

        print("\nInformasi pribadimu : ")
        print(f"Nama kamu: {nama}")
        print(f"usia: {usia}")
        print(f"info credit {info_credit}")
        print(f"bni: {bni}")
        print(f"fav cloth: {cloth}")
        print(f"dompet: {money}")
        print(f"kecewa kerja: {rdm}")
        print(f"ip rumah: {ip}")
        print(f"pasangan: {pcr}")
        print(f"belajar ruby?: {ruby}")
        print(f"tabungan: {uang}")
        
    elif pilih == "2":
        print("Masukan pelajaran yang kau sukai")
        pfa = input("pelajaran favorit anda: ")
        nilai = input("nilai tertinggi dalam pelajaran tersebut: ")

        print(f"pelajaran fav: {pfa}")
        print(f"nilai tertinggi {nilai}")
        
    elif pilih == "3":
        print("thanks and byee! ")
        break
    else:
        print("pilihan tidak valid")