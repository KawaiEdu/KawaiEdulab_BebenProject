def hitung_bmi (berat, tinggi):
    tm = tinggi / 100
    return round(berat / (tm ** 2), 2)

def cbmi (bmi):
    if bmi < 18.5:
        return "underweight"
    elif 18.5 <= bmi < 25:
        return "normal"
    elif 25 <= bmi < 30:
        return "overweigth"
    else:
        return "fatass"

dmbi = []
while True:
    print("\n Menu Pilihan Bmi:")
    print("1. input data BMI")
    print("2. Tampilkan BMI clasificasion")
    print("3. Keluar")
    menu = input("Masukaan menu anda: ")

    if menu == "1":
        jorg = int(input("Masukan jumlah orang "))
        dmbi = [
            {
                "nama": input(f"nama orang ke-{i + 1} "),
                "berat": float(input(f"berat badan orang ke-{i + 1} ")),
                "tinggi": float(input(f"tinggi badan orang ke-{i + 1} "))
            }
            for i in range(jorg)
        ]
        for borg in dmbi:
            borg["bmi"] = hitung_bmi(borg["berat"], borg["tinggi"])
            borg["kkbmi"] = cbmi(borg["bmi"])
    elif menu == "2" :
        if not dmbi :
            print("data belum masuk")
            continue
        print("\nhasil klasifikasi bmi")
        for i in dmbi :
            print(f"{i['nama']} dengan hasil BMI {i['bmi']} dan kategori bmi {i['kkbmi']}")
    elif menu == "3":
        print("terimah kasih dan datanglah lagi")
        break
    else :
        print("it's not the programs problem its your problem")