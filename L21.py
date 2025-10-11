bread = []
while True:
    pizza = input("masukan makanan yang di inginkan ")
    bread.append(pizza)
    
    pickle = input("apakah anda ingin menanpilkan nama makanan yang sudah di masukan ")
    if pickle == "y":   
        for food in bread:
            print(food)
    elif pickle == "n":
        print(bread)
        print("sudah shoping dan mau keluar!")
        break
    else:
        print("inputan yang kamu masukan salah silakan coba lagi")