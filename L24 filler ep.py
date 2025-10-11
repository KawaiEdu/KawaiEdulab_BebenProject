#program, nested loop dengan pola bintang dinamis

def pola_segitiga_kanan(n):
    for i in range (1,n + 1):
        print("*" * n)

def pola_segitiga_kiri(n):
    for i in range (1, n + 1):
        print(" " * (n - i) + "*" * i)

def pola_segitiga_terbalik (n):
    for i in range (n,0,-1):
        print("*" * i )

def pola_piramida (n):
    for i in range (1,n + 1):
        print(" " * (n -i) + "*" * (2 * i -1))

def main():
    print("program pola bintang")
    print("1. segitiga rata kiri")
    print("2. segitiga rata kanan")
    print("3. pola segitiga terbalik")
    print("4. pola piramida")

    choice = int(input("masukan pilihan "))
    baris = int(input("masukan jumlah baris segitiga "))

    if choice == 1:
        pola_segitiga_kiri(baris)
    elif choice == 2: pola_segitiga_kanan(baris)
    elif choice == 3: pola_segitiga_terbalik(baris)
    elif choice == 4: pola_piramida(baris)
    else:
        print("internet mu nga bisa")

main()