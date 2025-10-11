tambah = lambda x, y: x + y
kurang = lambda x, y: x - y
kali = lambda x, y: x * y
bagi = lambda x, y: x / y

# meminta input dari pengguna
print("selamat datang di kalkulator lambda")
x = float(input("masukan angka pertama: "))
y = float(input("masukan angka kedua: "))
operasi = input("pilih operasi(+,-,*,/)")

# menjalankan fungsi berdarsarkan operasi yang dipilih
if y !=0:
    if operasi == '+':
        print("hasil:",tambah(x,y))
    elif operasi =='-':
        print("hasil:",kurang(x,y))
    elif operasi =='*':
        print("hasil:",kali(x,y))
    elif operasi =='/':
        print("hasil:",bagi(x,y))
else:
    print("Error: tidak bisa dibagi dengan nol")