from abc import ABC, abstractmethod

class bentuk(ABC):
    @abstractmethod
    def luas(self): ...
    @abstractmethod
    def render(self): ...
    
class persegi(bentuk):
    def __init__(self, s): self.s=s
    def luas(self): return self.s*self.s
    def render(self): return f"persegi s= {self.s} luas={self.luas()}"
    
class lingkaran(bentuk):
    def __init__(self, r): self.r=r
    def luas(self): return 3.14*self.r*self.r
    def render(self): return f"lingkaran r={self.r} luas={self.luas():.2f}"
    
bentuk = [persegi(3), lingkaran(2), persegi(1)]
for b in bentuk:
    print(b.render())