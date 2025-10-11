# main.py

from utils import generate_fibonacci_series, save_series, load_series, plot_series
from data_generator import generate_aritmetic_series, generate_random_series, generate_mixed_series

while True:
    print("\nNo.1: fibonacci \nNo.2: aritmetika \nNo.3: acak \nNo.4: campuran \nNo.5: Keluar")
    jenis = input("Pilih menu anda: ")

    if jenis == "1":
        n = int(input("masukan angka yang akan di proses: "))
        series = generate_fibonacci_series(n, use_memo=True)
    elif jenis == "2":
        n = int(input("masukan angka yang akan di proses: "))
        series = generate_aritmetic_series(n)
    elif jenis == "3":
        n = int(input("masukan angka yang akan di proses: "))
        series = generate_random_series(n)
    elif jenis == "4":
        n = int(input("masukan angka yang akan di proses: "))
        series = generate_mixed_series(n)
    elif jenis == "5":
        print("Anda telah keluar dari program")
        break
    else:
        print("Pilihan Salah, Silahkan Input Ulang")
    
    save_series(series, filename=f"{jenis}_series.json")
    loaded = load_series(filename=f"{jenis}_series.json")

    print(f"deret {jenis.capitalize()}:")
    print(loaded)

    plot_series(loaded, title=f"deret {jenis.capitalize()}")