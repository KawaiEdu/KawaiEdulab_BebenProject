import random

class sword:
    def __init__(self, name: str, material: str, sword_rating: str) -> None:
        self.name = name
        self.material = material
        self.sword_rating = sword_rating
        self.basic_attack_ready: bool = True 

    def basic_attack(self) -> None:
        if self.basic_attack_ready:
            dmg = self.get_damage()
            print(f'sword ({self.material}) is preparing for basic attack.')
            self.basic_attack_ready = False
            print(f"sword ({self.material}) has performed a basic attack with damage: {dmg}")
        else:
            print(f'sword ({self.material}) is on cooldown.')

    def reset_basic(self) -> None:
        if not self.basic_attack_ready:
            self.basic_attack_ready = True
            print(f'sword ({self.material}) basic attack cooldown reset.')
        else:
            print(f'sword ({self.material}) is ready to use.')

    def attack(self, time: int) -> None:
        if not self.basic_attack_ready:
            dmg = self.get_damage()
            print(f"attacking with ({self.name}) for ({time}) seconds... Damage dealt: {dmg}")
            self.reset_basic()
        else:
            print(f'system: \"your basic attack is still on cooldown\"')

    def show_info(self):
        print(f"Nama Pedang: {self.name}")
        print(f"Material: {self.material}")
        print(f"Rating: {self.sword_rating}")

    def get_damage(self):
        damage_ranges = {
            "wood": (1, 10),
            "stone": (10, 25),
            "iron": (25, 35),
            "gold": (35, 40),
            "ruby": (40, 60),
            "diamond": (40, 100),
        }
        low, high = damage_ranges.get(self.material, (1, 5))
        return random.randint(low, high)


rating_material = {
    "wood": "F",
    "stone": "D",
    "iron": "B",
    "gold": "C",
    "ruby": "A",
    "diamond": "S"
}

print("\n Data Senjata")
name_input = input("Masukkan nama pedang: ")

while True:
    print("\nPilih material:")
    print("1. wood\n2. stone\n3. iron\n4. gold\n5. ruby\n6. diamond")
    material_input = input("Masukkan material (ketik nama material): ").lower()

    if material_input not in rating_material:
        print("Material tidak valid! Coba lagi.")
        continue

    rating_input = rating_material[material_input]

    my_sword = sword(name=name_input, material=material_input, sword_rating=rating_input)
    my_sword.show_info()

    pilihan = input("\nIngin memakai basic attack dulu? (yes/no): ").lower()

    if pilihan == "no":
        print("\nKembali ke pemilihan material...\n")
        continue

    elif pilihan == "yes":
        jumlah = int(input("Berapa banyak serangan yang ingin dijalankan?: "))

        print("\n-- Memulai Serangan --")
        for i in range(jumlah):
            print(f"\nSerangan ke-{i+1}:")
            if my_sword.basic_attack_ready:
                my_sword.basic_attack()
            else:
                my_sword.attack(3)

        break

    else:
        print("Input tidak valid! Ketik yes/no.")
        continue