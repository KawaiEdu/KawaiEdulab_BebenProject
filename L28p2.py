def tambah(a,b): return a+b

assert tambah(2,3) == 5, "Jawaban Salah"
assert tambah(-1,1) == 0, "Jawaban Salah"
print("semua tes lulus!")

def aman_bagi(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "tidak bisa di bagi dengan nol"
print(aman_bagi(10, 0))