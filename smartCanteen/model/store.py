import json, os
from .member import Member
from .utils import rupiah
from collections import defaultdict

class Store:
    def __init__(self, path="data/data.json"):
        self.path = path
        self.members = {}      
        self.transaksi = []    
        self._load()

    def _load(self):
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        if not os.path.exists(self.path):
            self._save(); return
        with open(self.path, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.members = {m["id"]: Member(**m) for m in data.get("members", [])}
        self.transaksi = data.get("transaksi", [])

    def _save(self):
        data = {
            "members": [m.to_dict() for m in self.members.values()],
            "transaksi": self.transaksi
        }
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def tambah_member(self, id, nama, kelas):
        assert id not in self.members, "ID sudah ada"
        self.members[id] = Member(id, nama, kelas, 0)
        self._save()

    def topup(self, id, nominal):
        self.members[id].topup(nominal)
        self.transaksi.append({"id": id, "jenis": "topup", "nominal": int(nominal)})
        self._save()

    def beli(self, id, nominal):
        self.members[id].beli(nominal)
        self.transaksi.append({"id": id, "jenis": "beli", "nominal": int(nominal)})
        self._save()

    def laporan_harian(self):
        t = sum(t["nominal"] for t in self.transaksi if t["jenis"]=="topup")
        b = sum(t["nominal"] for t in self.transaksi if t["jenis"]=="beli")
        return {"total_topup": t, "total_beli": b}
    
    def info_member(self, id):
        m = self.members.get(id)
        assert m is not None, "Member tidak ditemukan"
        return f"{m.nama} ({m.kelas}) — Saldo: {rupiah(m.saldo)}"

    def semua_member(self):
        return [f"[{m.id}] {m.nama} ({m.kelas}) — {rupiah(m.saldo)}"
            for m in self.members.values()]
        
    def top3_pembeli(self):
        total_beli = defaultdict(int)
        for t in self.transaksi:
            if t["jenis"] == "beli":
                total_beli[t["id"]] += int(t["nominal"])
            ranking = sorted(total_beli.items(), key=lambda x: x[1], reverse=True)[:3]
            hasil = []
            for id, jumlah in ranking:
                m = self.members.get(id)
                nama = m.nama if m else id
                hasil.append((nama, jumlah))
            return hasil
            