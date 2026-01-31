from abc import ABC, abstractmethod

class bentuk(ABC):
    @abstractmethod
    def luas(self): ...
    
class persegi:
    def __init__(self, s): self.s = s
    def luas(self): return self.s*self.s
    
class MesinSuara:
    def __init__(self, bunyi): self.bunyi = bunyi
    def suara(self): return self.bunyi
    
class robotkucing:
    def __init__(self):
        self.audio = MesinSuara("meong-robot")
    def suara(self):
        return self.audio.suara()
    
rk = robotkucing()
print(rk.suara())