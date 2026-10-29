import tkinter.messagebox as messagebox
from models.buku_model import BukuModel
from views.buku_view import BukuView
from views.login_view import LoginView
from controllers.login_controller import LoginController

class BukuController:
    def __init__(self, user_role="anggota"):
        self.user_role = user_role
        self.model = BukuModel()
        self.view = BukuView()

        # Menampilkan informasi role pada judul jendela aplikasi
        self.view.title(f"Sistem Manajemen Perpustakaan - Mode: {self.user_role.upper()}")

        # Binding callback logout dari View ke metode logout Controller
        self.view.on_logout_callback = self.logout

        # Binding tombol ke metode Controller
        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_update.configure(command=self.update_data)
        self.view.btn_delete.configure(command=self.delete_data)

        # OTORISASI: Hanya nonaktifkan tombol Update dan Delete jika bukan admin
        if self.user_role != "admin":
            self.view.btn_update.configure(state="disabled", text="Update (Khusus Admin)")
            self.view.btn_delete.configure(state="disabled", text="Hapus (Khusus Admin)")

        self.muat_data_tabel()

    def logout(self):
        # Konfirmasi logout
        if messagebox.askyesno("Konfirmasi Logout", "Apakah Anda yakin ingin keluar?"):
            # 1. Tutup/hancurkan jendela BukuView
            self.view.destroy()
            
            # 2. Inisialisasi dan tampilkan kembali jendela Login
            login_view = LoginView()
            LoginController(login_view)
            login_view.mainloop()

    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)
        data_buku = self.model.get_all_buku()
        for buku in data_buku:
            self.view.tabel.insert("", "end", values=(buku['id_buku'], buku['judul'], buku['penulis'], buku['tahun_terbit']))

    def simpan_data(self):
        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        if self.model.create_buku(judul, penulis, tahun):
            messagebox.showinfo("Sukses", "Data buku berhasil disimpan!")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Gagal menyimpan data.")

    def update_data(self):
        # Proteksi ganda otorisasi di level Controller
        if self.user_role != "admin":
            messagebox.showerror("Akses Ditolak", "Anda tidak memiliki izin untuk memperbarui data!")
            return

        selected_item = self.view.tabel.selection()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih data buku dari tabel yang ingin diperbarui!")
            return

        item_data = self.view.tabel.item(selected_item)['values']
        id_buku = item_data[0]

        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        if self.model.update_buku(id_buku, judul, penulis, tahun):
            messagebox.showinfo("Sukses", "Data buku berhasil diperbarui!")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Gagal memperbarui data.")

    def delete_data(self):
        # Proteksi ganda otorisasi di level Controller
        if self.user_role != "admin":
            messagebox.showerror("Akses Ditolak", "Anda tidak memiliki izin untuk menghapus data!")
            return

        selected_item = self.view.tabel.selection()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih data buku dari tabel yang ingin dihapus!")
            return

        item_data = self.view.tabel.item(selected_item)['values']
        id_buku = item_data[0]

        konfirmasi = messagebox.askyesno("Konfirmasi Hapus", "Apakah Anda yakin ingin menghapus buku ini?")
        if konfirmasi:
            if self.model.delete_buku(id_buku):
                messagebox.showinfo("Sukses", "Data buku berhasil dihapus!")
                self.bersihkan_form()
                self.muat_data_tabel()
            else:
                messagebox.showerror("Error", "Gagal menghapus data.")

    def bersihkan_form(self):
        self.view.entry_judul.delete(0, 'end')
        self.view.entry_penulis.delete(0, 'end')
        self.view.entry_tahun.delete(0, 'end')

    def run(self):
        self.view.mainloop()