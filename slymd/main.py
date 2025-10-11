from data_generator import factorial, fibonacci, pangkat
from utils import tint, menu

while True:
    menu()
    v = input("Pilih: ").strip()
    if v == "4": print("Bye byee!"); break
    if v not in {"1","2","3","4"}: print("pilihan anda tidak valid"); continue

    vv = tint(input("Masukan n/angka-1: "))
    if vv is None: print("Harus memilih angka!"); continue

    if v == "1":
        print("hasil:", factorial(vv))
    elif v == "2":
        print("Hasil:", fibonacci(vv))
    elif v == "3":
        v1 = tint(input("Masukan angka-2 (pangkat): "))
        if v1 is None: print("Harus angka!"); continue
        print("Hasil:", pangkat(vv, v1))