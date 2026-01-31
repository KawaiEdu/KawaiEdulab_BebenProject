class hewan:
    def __init__(self, nama):
        self.nama = nama

    def suara():
        return ("hmmm")
    
class kucing(hewan):
    def suara():
        return ("meh")
    
class anjing(hewan):
    def suara():
        return ("weh")
    
class manusia(hewan):
    def suara():
        return ("bentar nanti HP ku tak kumpulin, he belum jam 2")
    
mimi = kucing("Mimi")
wiwi = anjing("wiwi")
dearyl = manusia("dearyl")
print(mimi.nama, "bersuara", kucing.suara())
print(wiwi.nama, "bersuara", anjing.suara())
print(dearyl.nama, "bilang", manusia.suara())