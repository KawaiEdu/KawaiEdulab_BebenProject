print("=== PROGRAM LATIHAN LOOPING ===")
print("ketik keluar kapan saja untuk menghentikan program\n")

while True :
    print("\n pilih jenis looping")
    print("1. looping with range")
    print("2. looping with list")
    
    choice = input("masukan pilihan ")
    if choice == '1':
        limit = input("Masukkan Batas ")      
        if limit.lower() == 'keluar':
            break
        if limit.isdigit():
            limit = int(limit)
            print(f"\n hasil looping dari 0 sampai {limit-1} ")
            for b in range(limit):
                print(f"angka ke - {b}")
        else:
            print("maaf input harus angka")
    
    elif choice == '2':
        data = input("masukan beberapa item(pisahkan dengan koma) ")
        if data.lower() == 'keluar':
            break
        list = [item.strip() for item in data.split(',')]
        print("\n list yang anda masukan:")
        for item in list:
            print(f" - {item}")
    else:
        print("pilihan tidak valid silakan 1 atau 2")