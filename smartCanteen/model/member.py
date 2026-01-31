class Member:
    def __init__(self, id, nama, kelas, saldo=0):
        self._id = id; self._nama = nama; self._kelas = kelas
        self._saldo = 0; self.saldo = saldo

    @property
    def id(self): return self._id        
    @property
    def nama(self): return self._nama
    @property
    def kelas(self): return self._kelas

    @property
    def saldo(self): return self._saldo
    @saldo.setter
    def saldo(self, v):
        assert v >= 0, "Saldo tidak boleh negatif"
        self._saldo = v

    def topup(self, n):
        assert n > 0, "Top up harus > 0"
        self._saldo += n

    def beli(self, n):
        assert 0 < n <= self._saldo, "Saldo tidak cukup"
        self._saldo -= n

    def to_dict(self):
        return {"id": self.id, "nama": self.nama, "kelas": self.kelas, "saldo": self.saldo}