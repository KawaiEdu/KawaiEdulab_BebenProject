class Siswa:
    def __init__(self, nama, kelas):
        self.nama = nama
        self.kelas = kelas

    def perkenalan(self):
        return f"Halo, nama i {self.nama} dari {self.kelas}"

dara = Siswa("dearly", "rahim ibu")
print(dara.perkenalan())