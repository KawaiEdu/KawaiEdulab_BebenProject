import math as m
import random as r
from utils import kali as ka
from utils import max3 as ma3

for i in range(10):
    angka = r.randint(1, 100)
    kuadrat = m.sqrt(angka)
    pi = m.pi

    print(f"Hasil kuadrat : {kuadrat}")
    print(f"Hasil angka Acak : {angka}")
    print(f"Hasil pi : {pi}")   
    print(f"hasil 10 kali {i}={ka(10, i)}")
    print(f"hasil nilai max3 dari ({angka}, {i}, 50)= {ma3(angka, i, 50)}")