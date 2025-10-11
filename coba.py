def predikatBMI(bmi):
  if bmi < 18.5:
    print("under weight")
  elif bmi<= 24.9:
     print("normal weight")
  elif bmi<= 29.9:
    print("over weight")
  else:
    print("obesitas")

while True:
    print("selamat datang BMI Hitungan")
    print("1. hitung bmi")
    print("2. predikat bmi")
    print("3. exit")
    choice = input("masukan pilihan: ")
    if choice == "1":
      bb = int(input("masukan bb: "))
      tb = float(input("masukan tb: "))
      bmi = bb / (tb*tb)
      print(f"hasil BMI: {bmi}")
    elif choice == "2":
      predikatBMI(bmi)
    elif choice == "3":
        print("Terima kasih! Sampai jumpa.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")