def luas_persegi(sisi):
    return sisi * sisi

def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

def convert_to_fahrenhiet(celsius):
    return (celsius * 9/5) + 32

persegi = luas_persegi(6)
persegi_panjang = luas_persegi_panjang(4, 5)
suhu = convert_to_fahrenhiet(20)

print(persegi)
print(persegi_panjang)
print(suhu)