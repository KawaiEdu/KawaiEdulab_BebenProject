def pbmi(hbmi):
    if hbmi < 18.5:
        return ">>skinny<<"
    elif 18.5 <= hbmi < 25:
        return ">>normal<<"
    elif 25 <= hbmi < 30:
        return ">>overweight<<"
    else:
        return ">>Fatass<<"

def bmi(weight, height):
    meter = height/100
    return round(weight / (meter ** 2), 2)
       
a = []
while True:
    print("1. masukkan jumlah orang")
    print("1.5. lihat predikat bmi")
    print("2. keluar.")
    
    k = float(input("masukkan pilihan "))
    
    if k == 1:
        jo = int(input("masukkan jumlah orang "))
        a = [{
            "nama" : input("masukkan nama "),
            "cm" : float(input(f"tinggi(cm) orang ke-{i + 1} ")),
            "kg" : float(input(f"berat(kg) orang ke-{i + 1} "))
            }
             for i in range(jo)
        ]
        for s in a:
            s["bmi"] = bmi(s["kg"], s["cm"])
            s["kkbmi"] = pbmi(s["bmi"])
    elif k == 1.5 :
        if not a :
            print("data belum dimasukkan")
            continue
        print("\nhasil klasifikasi bmi")
        for i in a:
            print(f"{i['nama']} dengan hasil BMI {i['bmi']} dan kategori bmi {i['kkbmi']}")
    elif k == 2:
        print("terimakasih telah menggunakan kode ini")
        break
    else:
        print("1323323214564654654678979877998798789798")