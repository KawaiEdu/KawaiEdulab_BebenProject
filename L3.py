print("selamat datang calc mini")
x = int(input("masukan angka pertama: "))
y = int(input("masukan angka kedua: "))
print("1. penjumlahan")
print("2. pengurangan")
print("3. perkalian")   
print("4. pembagian")
print("5. sisa bagi")

choice = input("masukan pilihan: ")
if choice == "1":
  jumlah = x+y
  print(f"hasilnya: {jumlah}")
elif choice == "2":
  pengurangan = x-y
  print(f"hasilnya: {pengurangan}")
elif choice == "3":
  perkalian = x*y
  print(f"hasilnya: {perkalian}")
elif choice == "4":
  pembagian = x/y
  print(f"hasilnya: {pembagian}")
elif choice == "5":
  sisa_bagi = x % 2
  print(f"hasilnya: {sisa_bagi}")
else:
  print("Pilihan Tidak valid")