import random as r
from utils import valid_int
target = r.randint(1, 20)
while True:
    raw = input("tebak nomor 1-20")
    n = valid_int(raw)
    if n is None:
        print("masukan angka!"); continue
    if n == target: print("benar!"); break
    print("terlalu", "kecil" if n < target else "benar")