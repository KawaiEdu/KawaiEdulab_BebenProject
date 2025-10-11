def pbmi(A):
    if A < 18.5:
        print(f">>skinny<< {A}")
    elif A < 25:
        print(f">>normal<< {A}")
    elif A < 30:
        print(f">>overweight<< {A}") 
    else:
        print(f">>Fatass<< {A}")
        
while True:
    print("1. masukkan data bmi")
    print("1.5. lihat predikat bmi")
    print("2. keluar.")
    
    k = float(input("masukkan pilihan "))
    
    if k == 1:
        f = float(input("masukkan tinggi badan."))
        c = float(input("masukkan berat badan."))
        A = c / (f * f)
    elif k == 1.5 :
        pbmi(A)
    elif k == 2:
        break
    else:
        print("1323323214564654654678979877998798789798")