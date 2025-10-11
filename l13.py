fruit_shop = ("durian", "grape", "pear", "dragon fruit", "longan")

fruit = input("masukan buah yang ingin di cari:")
if fruit in fruit_shop:
    print(f"{fruit_shop} ada di dalam toko")
else:
    print("buah nya habis")