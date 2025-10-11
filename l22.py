animal = []
pjd = [len(h) for h in animal]

while True:
    animal_input = input("masukan nama hewan")
    animal.append(animal_input)
    
    choice = input("apakah anda ingin keluar")
    if choice == "yes":
        print(pjd)
        print("terimah kasih saya telah keluar")
        break