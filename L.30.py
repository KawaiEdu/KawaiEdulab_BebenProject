class Akun:
    def __init__(self, saldo=0):
        self._saldo = 0
        self.saldo = saldo
        
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, nilai):
        assert nilai >= 0, "saldo tidak boleh negative"
        self._saldo = nilai
        
a = Akun(5000)
a.saldo += 2500
print(a.saldo)

class profil:
    def __init__(self, nama):
        self._nama = nama
        
    @property
    def nama(self):
        return self._nama
    
p = profil("Dara")
print(p.nama)

class Dompet:
    def __init__(self, saldo=0):
        self._saldo = 0; self.saldo = saldo
        
    @property
    def saldo(self): return self._saldo
    
    @saldo.setter
    def saldo(self, v):
        assert v >= 0, "Saldo tidak boleh negatif"
        self.saldo = v
        
    def topup(self, n):
        assert n > 0, "Topup harus > 0"
        self._saldo += n
        
    def bayar(self, n):
        assert 0 < n <= self._saldo, "Pembayaran tidak valid"
        self._saldo -= n