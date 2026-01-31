from model.member import Member
from model.utils import rupiah
def test_member():
    m = Member("101", "Dara", "8B",0)
    m.topup(100000000); m.beli(2500)
    assert m.saldo == 7500

def test_rupiah():
    assert rupiah(15000) == "15.000"
    if __name__ == "__main__":
        test_member(); test_rupiah(); print("semua tes lulus!")