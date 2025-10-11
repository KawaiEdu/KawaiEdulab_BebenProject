def kalkulator():
    try:
        angka1 = float(input("Masukkan angka pertama:"))
        angka2 = float(input("Masukkan angka kedua:"))
        operasi = input("masukan operasi(+,-,*,/)")
        if operasi == "+":
            result = angka1 + angka2
        elif operasi == "-":
            result = angka1 - angka2
        elif operasi == "*":
            result = angka1 * angka2
        elif operasi == "/":
            result = angka1 / angka2
        else:
            print("operasi tidak valid")
        return print(f"hasil: {result}")
    
    except ValueError:
        print("input harus angka")
    
    except ZeroDivisionError:
        print("tidak bisa di bagi dengan 0")

while True:
    print("\n ===> CALCULATOR SEDERHANA <===")
    kalkulator()
    again = input("apakah anda ingin menghitung lagi (yes/no) ")
    if again.lower() != "yes":
        print("terima kasih byee!")
        break