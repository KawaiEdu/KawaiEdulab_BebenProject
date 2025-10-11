def text_conversion (nilai):
    if nilai >= 95: return "A+"
    elif nilai >= 90: return "A"
    elif nilai >= 86: return "A-"
    elif nilai >= 81: return "B+"
    elif nilai >= 75: return "B"
    elif nilai >= 72: return "B-"
    elif nilai > 69: return "C+"
    elif nilai > 65: return "C"
    elif nilai > 61: return "C-"
    elif nilai > 57: return "D+"
    elif nilai > 54: return "D"
    elif nilai > 49: return "D-"
    elif nilai > 45: return "E+"
    elif nilai > 39: return "E"
    elif nilai > 35: return "E-"
    else: return "F"
    
data_siswa = []
kkm = None

while True: 
    print("\n=== menu utama ===")
    print("1. Input data siswa")
    print("2. Tampilkan siswa yang lulus")
    print("3. Tampilkan nilai akhir siswa dan nilai huruf")
    print("4. Keluar")
    menu = input("masukan pilihan anda: ")
    
    if menu == "1":
        jumlah_siswa = int(input("masukan jumlah siswa: "))
        data_siswa = [
            {
                "nama": input(f"masukan nama siswa ke - {i+1} "),
                "nilai": float(input(f"nilai siswa ke - {i+1} "))
            }
            for i in range(jumlah_siswa)
            ]
        kkm = float(input("masukan nilai kkm "))
        
        for s in data_siswa:
            s["tugas"] = float(input(f"nilai tugas {s['nama']} "))
            s["ujian"] = float(input(f"nilai ujian {s['nama']} "))
            s["nilai"] = round(0.3 * s["tugas"] + 0.7 * s["ujian"], 2)
            
        print("data siswa berhasil di simpan")
        
    elif menu == "2":
        if not data_siswa:
            print("data belum di masukan")
            continue
        siswa_lulus = [s["nama"] for s in data_siswa if s["nilai"] >= kkm]
        print("\n siswa yang lulus berdasarkan nilai awal")
        if siswa_lulus:
            print(", ".join(siswa_lulus))
        else :
            print("tidak ada siswa yang lulus")
        
    elif menu == "3":
        if not data_siswa :
            print("data belum di masukkan")
            continue
        sdnh = [{
            "nama" : s["nama"],
            "nilai" : s["nilai"],
            "nilai_huruf" : text_conversion(s["nilai"])
            }
            for s in data_siswa
        ]
        
        print("\ndaftar nilai akhir dan nilai huruf")
        for i in sdnh:
              print(f"{i['nama']}: {i['nilai']} ({i['nilai_huruf']})")
        
    elif menu == "4":
        print("terima kasih telah menggunakan program semoga lulus")
        break
    else:
        print("ada permasalahan di dalam programan silakan coba lagi")