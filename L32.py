class kucing:
    def suara(self): return "kucing: meong"
    
class anjing:
    def suara(self): return "anjing: guk"
    
def bunyikan(hewan): 
    print(hewan.suara())
    
bunyikan(kucing())
bunyikan(anjing())

class persegi:
    def __init__(self, s): self.s=s
    def luas(self): return self.s*self.s
    
class lingkaran:
    def __init__(self, r): self.r=r
    def luas(self): return 3.14*self.r*self.r
    
bentuk = [persegi(2), lingkaran(3), persegi(4)]
total = 0 
for b in bentuk:
    total += b.luas()
    print(total)
