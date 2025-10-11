usia = int(input("Masukkan usia: "))
if usia < 12:
    print("Kategori: Anak-anak")
elif usia <= 18:
    print("Kategori: Remaja")
else:
    print("Kategori: Dewasa")
    
suhu = int(input("Masukkan suhu udara (°C): "))
if suhu > 30:
    print("Suhu udara sangat panas")
elif suhu > 20:
    print("Suhu udara normal")
elif suhu > 10:
    print("Suhu udara dingin")
else:
    print("Suhu udara sangat dingin")