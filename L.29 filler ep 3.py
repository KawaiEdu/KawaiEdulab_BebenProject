class Hewan:
    def __init__(self, nama, jenis, suara):
        self.nama = nama
        self.jenis = jenis
        self.suara = suara
        
    def bergerak(self):
        return f"{self.nama} sedang bergerak."

    def bersuara(self):
        return f"{self.nama} bersuara: {self.suara}"
    
class manusia:
    def __init__(self, nama, umur, perkerjaan):
        self.nama = nama
        self.umur = umur
        self.perkerjaan = perkerjaan
        
    def perkenalan(self):
        return f"Halo, nama saya {self.nama}, umur saya {self.umur} tahun, berkerja sebagai {self.perkerjaan}."
    
    def berkerja(self):
        return f"{self.nama} sedang berkerja sebagai {self.perkerjaan}."

class benda:
    def __init__(self, nama, fungsi, bahan):
        self.nama = nama
        self.fungsi = fungsi
        self.bahan = bahan
        
    def deskripsi(self):
        return f"{self.nama} terbuat dari {self.bahan}, digunakan untuk {self.fungsi}"
        
def main():
    print("=== Input data hewan ===")
    nama_hewan = input("Masukan nama hewan: ")
    jenis_hewan = input("Masukan jenis hewa: ")
    suara_hewan = input("Masukan suara hewan: ")
    hewan1 = Hewan(nama_hewan, jenis_hewan, suara_hewan)
    print("\n=== Input data manusia ===")
    nama_manusia = input("Masukan nama manusia: ")
    umur_manusia = int(input("Masukan umur manusia: "))
    perkerjaan_manusia = input("Masukan perkerjaan manusia: ")
    manusia1 = manusia(nama_manusia, umur_manusia, perkerjaan_manusia)
    
    print("\n=== input data benda ===")
    nama_benda = input("Masukan nama benda: ")
    fungsi_benda = input("Masukan fungsi benda: ")
    bahan_benda = input("Masukan bahan benda: ")
    benda1 = benda(nama_benda, fungsi_benda, bahan_benda)
    
    while True:
        print("\n=== MENU PROGRAM ===")
        print("1. Tampilkan aktivita Hewan")
        print("2. Tampilkan aktivita manusia")
        print("3. Tampilkan deskripsi benda")
        print("Keluar")
        
        pilihan = input("masukan pilihan (1-4):")
        
        if pilihan == "1":
            print(hewan1.bergerak())
            print(hewan1.bersuara())
            
        elif pilihan == "2":
            print(manusia1.perkenalan())
            print(manusia1.berkerja())
        
        elif pilihan == "3":
            print(benda1.deskripsi())
               
        elif pilihan == "4":
            print("program telah selesai. Terima kasih!")
            break
        else:
            print("pilihan anda tidak valid coba lagi")
            
            
if __name__=="__main__":
    main()