import random
import time

class Player:
    def __init__(self, name, max_ammo=8):
        self.name = name
        self.max_ammo = max_ammo
        self.ammo = max_ammo

    def shoot(self):
        if self.ammo <= 0:
            print("⚠ Amunisi habis! Reload dulu!")
            return 0

        self.ammo -= 1
        damage = random.randint(5, 30)
        print(f"{self.name} menembak! 🔫 Damage: {damage} | Sisa ammo: {self.ammo}")
        return damage

    def reload(self):
        print("🔄 Mengisi ulang amunisi...")
        time.sleep(1)
        self.ammo = self.max_ammo
        print(f"Amunisi penuh! ({self.ammo})")

    def status(self):
        print(f"--- STATUS PEMAIN ---")
        print(f"Nama    : {self.name}")
        print(f"Amunisi : {self.ammo}/{self.max_ammo}")
        print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------hehe------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")



class Enemy:
    def  __init__(self, name, health):
        self.name = name
        self.health = health

    def is_defeated(self):
        return self.health <= 0

    def show(self):
        print(f"Musuh muncul! 😈 {self.name} | HP: {self.health}")


class Game:
    def  __init__(self):
        self.player = None
        self.enemies = [
            Enemy("Zombie", 40),
            Enemy("Aqil", 50),
            Enemy("Boss orc", 80)
        ]

    def start(self):
        print("=== GAME AMUNISI — VERSI PANJANG ===")
        name = input("Masukkan nama pemain: ")
        self.player = Player(name)

        print("\nMemulai permainan...\n")
        time.sleep(1)

        for enemy in self.enemies:
            enemy.show()
            self.battle(enemy)

        print("\n🎉 SELAMAT! Semua musuh berhasil dikalahkan!")

    def battle(self, enemy):
        while not enemy.is_defeated():
            print("\nMenu:")
            print("1. Tembak")
            print("2. Reload")
            print("3. Status Pemain")

            pilihan = input("Pilih: ")

            if pilihan == "1":
                damage = self.player.shoot()
                enemy.health -= damage
                print(f"HP musuh sekarang: {max(enemy.health, 0)}")

                if enemy.is_defeated():
                    print(f"🔥 {enemy.name} dikalahkan!")
                    break

            elif pilihan == "2":
                self.player.reload()
            elif pilihan == "3":
                self.player.status()
            else:
                print("Pilihan tidak valid!")



# Jalankan game
game = Game()
game.start()