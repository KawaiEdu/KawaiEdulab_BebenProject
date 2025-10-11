keranjang = []
def tambah_item ():
    nama_pembeli = input("masukan barang yang ingin di masukan ")
    price_barang = float(input("harga barang tersebut: "))
    jumlah = int(input("jumlah dari semua barang "))
    keranjang.append({'nama ': nama_pembeli, 'harga ':price_barang, 'jumlah ':jumlah})
    print(f"{jumlah} x {nama_pembeli} berhasil ditambahkan.\n")

def tampilkan_keranjang ():
    if not keranjang:
        print("Keranjang masih kosong.\n")
        return
    print("Daftar belanja:")
    for i, item in enumerate(keranjang, start=1):
        print(f"{i}. {item['nama ']} - Rp{item['harga ']:.2f} x {item['jumlah ']} = Rp{item['harga '] * item['jumlah ']:.2f}")
        print()
    
def hitung_total():
    total = sum(item['harga'] * item['jumlah'] for item in keranjang)
    return total

def bayar():
    total = hitung_total
    print(f"Total belanja Anda: Rp{total:.2f}")
    uang = float(input("Masukkan jumlah uang: Rp"))
    if uang < total:
        print("uang kurang bang./n")
    else:
        kembalian = uang - total
        print(f"pembayaran berhasil. kembalian anda: Rp{kembalian:.2f}\n")
        keranjang.clear()
            
def main():
    while True:
        print("==> kasir mini <==")
        print("1. Teambah barang")
        print("2. lihat keranjang")
        print("3. bayar")
        print("4. keluar")
        pilihan = input("pilih menu (1-4): ")
            
        if pilihan == '1':
            tambah_item()
        elif pilihan == '2':
            tampilkan_keranjang()
        elif pilihan == '3':
            bayar()
        elif pilihan == '4':
            print("thanks kembali lagi besok")
            break
        else:
            print("nga valid bang. coba lagi.\n")
                
if __name__=="__main__": 
    main()