class produk:
    def __init__(self, nama, harga):
        self.nama = nama; self.harga = harga
        def info(self):
            return f"{self.nama} -  Rp.{self.harga}"
        
class buku(produk):
    def __init__(self, nama, harga, penulis):
        super().__init__(nama, harga)
        self.penulis = penulis
    def info(self):
        return f"{self.nama} oleh {self.penulis} - Rp{self.harga}"
    
b1 = buku("python fun", 75000, "Devy")
print(b1.info())