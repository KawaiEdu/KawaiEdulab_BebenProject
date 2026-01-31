import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from model.store import Store
from model.utils import safe_int, rupiah

ctk.set_appearance_mode("Dark") 
ctk.set_default_color_theme("blue")

class SmartCanteenApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Smart Canteen System")
        self.geometry("1200x650")
        self.resizable(False, False)

        self.store = Store()

        self.main_frame = ctk.CTkFrame(self, corner_radius=15)
        self.main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.lbl_judul = ctk.CTkLabel(self.main_frame, text="SMART CANTEEN\nSYSTEM", font=("Roboto", 24, "bold"))
        self.lbl_judul.pack(pady=(30, 20))

        self.menu_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.menu_frame.pack(pady=10)

        buttons = [
            ("1. Tambah Member", self.popup_tambah_member, 0, 0, "green"),
            ("2. Top Up Saldo", lambda: self.popup_transaksi("topup"), 0, 1, "green"),
            ("3. Beli (Belanja)", lambda: self.popup_transaksi("beli"), 1, 0, "orange"),
            ("4. Laporan Harian", self.show_laporan, 1, 1, "orange"),
            ("5. Lihat Member", self.show_semua_member, 2, 0, None),
            ("6. Info Member", self.popup_info_member, 2, 1, None),
            ("7. Top-3 Pembeli", self.show_top3, 3, 0, None),
        ]

        for text, cmd, r, c, color in buttons:
            btn_color = color if color else "primary"
            fg_color = None
            hover_color = None
            
            if color == "green": 
                fg_color = "#2CC985"
                hover_color = "#229A65"
            elif color == "orange":
                fg_color = "#E59113"
                hover_color = "#D19233"

            if "Top-3" in text:
                btn = ctk.CTkButton(self.menu_frame, text=text, command=cmd, width=320, height=40)
                btn.grid(row=r, column=0, columnspan=2, padx=10, pady=10)
            else:
                btn = ctk.CTkButton(self.menu_frame, text=text, command=cmd, width=150, height=40, 
                                    fg_color=fg_color, hover_color=hover_color)
                btn.grid(row=r, column=c, padx=10, pady=10)

        self.btn_keluar = ctk.CTkButton(self.main_frame, text="8. Keluar Aplikasi", command=self.keluar, 
                                        fg_color="#D64232", hover_color="#C83224", width=200, height=45)
        self.btn_keluar.pack(pady=30)

        self.lbl_status = ctk.CTkLabel(self, text="System Created by ~~~~ ", text_color="gray", font=("Arial", 10))
        self.lbl_status.pack(side="bottom", pady=5)


    def create_popup(self, title, height=350):
        top = ctk.CTkToplevel(self)
        top.title(title)
        top.geometry(f"620x{height}")
        top.attributes("-topmost", True)
        return top

    def popup_tambah_member(self):
        top = self.create_popup("Tambah Member", 350)
        
        ctk.CTkLabel(top, text="ID Member:").pack(pady=(20,5))
        e_id = ctk.CTkEntry(top); e_id.pack()
        
        ctk.CTkLabel(top, text="Nama:").pack(pady=5)
        e_nama = ctk.CTkEntry(top); e_nama.pack()
        
        ctk.CTkLabel(top, text="Kelas:").pack(pady=5)
        e_kelas = ctk.CTkEntry(top); e_kelas.pack()

        def save():
            try:
                self.store.tambah_member(e_id.get(), e_nama.get(), e_kelas.get())
                messagebox.showinfo("Sukses", "Data disimpan!")
                top.destroy()
            except Exception as e:
                messagebox.showerror("Error", str(e))

        ctk.CTkButton(top, text="SIMPAN", command=save, fg_color="green").pack(pady=20)

    def popup_transaksi(self, jenis):
        title = "Top Up Saldo" if jenis == "topup" else "Pembayaran Kantin"
        top = self.create_popup(title, 250)
        
        ctk.CTkLabel(top, text="ID Member:").pack(pady=(20,5))
        e_id = ctk.CTkEntry(top); e_id.pack()
        
        ctk.CTkLabel(top, text="Nominal (Rp):").pack(pady=5)
        e_nom = ctk.CTkEntry(top); e_nom.pack()

        def proses():
            try:
                nom = safe_int(e_nom.get())
                if jenis == "topup":
                    self.store.topup(e_id.get(), nom)
                    msg = f"Top Up {rupiah(nom)} Berhasil!"
                else:
                    self.store.beli(e_id.get(), nom)
                    msg = f"Pembayaran {rupiah(nom)} Berhasil!"
                messagebox.showinfo("Sukses", msg)
                top.destroy()
            except Exception as e:
                messagebox.showerror("Gagal", str(e))

        color = "#2CC985" if jenis == "topup" else "#E59113"
        ctk.CTkButton(top, text="PROSES", command=proses, fg_color=color).pack(pady=20)

    def show_laporan(self):
        lap = self.store.laporan_harian()
        txt = f"Total Top Up: {rupiah(lap['total_topup'])}\nTotal Penjualan: {rupiah(lap['total_beli'])}"
        messagebox.showinfo("Laporan Harian", txt)

    def show_semua_member(self):
        top = self.create_popup("Data Semua Member", 400)
        top.geometry("500x400")

        textbox = ctk.CTkTextbox(top, width=450, height=350, font=("Consolas", 12))
        textbox.pack(pady=10, padx=10)
        
        data = self.store.semua_member()
        for row in data:
            textbox.insert("end", row + "\n")
        textbox.configure(state="disabled") # Read only

    def popup_info_member(self):
        top = self.create_popup("Cari Info Member", 200)
        ctk.CTkLabel(top, text="Masukkan ID:").pack(pady=(20,5))
        e_id = ctk.CTkEntry(top); e_id.pack()
        
        def cari():
            try:
                info = self.store.info_member(e_id.get())
                messagebox.showinfo("Info Member", info)
                top.destroy()
            except Exception as e:
                messagebox.showerror("404", str(e))
        
        ctk.CTkButton(top, text="Cari", command=cari).pack(pady=20)

    def show_top3(self):
        data = self.store.top3_pembeli()
        msg = "TOP 3 SULTAN KANTIN:\n\n"
        for i, (nama, tot) in enumerate(data, 1):
            msg += f"{i}. {nama} : {rupiah(tot)}\n"
        messagebox.showinfo("Top 3", msg)

    def keluar(self):
        if messagebox.askyesno("Konfirmasi", "Keluar dari aplikasi?"):
            self.destroy()

if __name__ == "__main__":
    app = SmartCanteenApp()
    app.mainloop()