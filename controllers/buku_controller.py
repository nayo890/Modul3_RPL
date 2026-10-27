import tkinter.messagebox as messagebox
from models.buku_model import BukuModel
from views.buku_view import BukuView

class BukuController:
    def __init__(self):
        self.model = BukuModel()
        self.view = BukuView()

        self.selected_id = None

        # 1. Binding Tombol Simpan
        if hasattr(self.view, 'btn_simpan'):
            self.view.btn_simpan.configure(command=self.simpan_data)

        # 2. Binding Tombol Perbarui (Cek penamaan btn_perbarui atau btn_update)
        if hasattr(self.view, 'btn_perbarui'):
            self.view.btn_perbarui.configure(command=self.perbarui_data)
        elif hasattr(self.view, 'btn_update'):
            self.view.btn_update.configure(command=self.perbarui_data)

        # 3. Binding Tombol Hapus (Cek penamaan btn_hapus atau btn_delete)
        if hasattr(self.view, 'btn_hapus'):
            self.view.btn_hapus.configure(command=self.hapus_data)
        elif hasattr(self.view, 'btn_delete'):
            self.view.btn_delete.configure(command=self.hapus_data)

        # 4. Binding event klik baris pada tabel
        self.view.tabel.bind("<<TreeviewSelect>>", self.pada_baris_diklik)

        # Memuat data ke tabel
        self.muat_data_tabel()

    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        data_buku = self.model.get_all_buku()

        for buku in data_buku:
            self.view.tabel.insert("", "end", values=(buku['id_buku'], buku['judul'], buku['penulis'], buku['tahun_terbit']))

    def pada_baris_diklik(self, event):
        selected_item = self.view.tabel.selection()
        if selected_item:
            item_data = self.view.tabel.item(selected_item[0])
            data = item_data.get('values', [])
            
            if data:
                # Simpan id_buku dari kolom pertama
                self.selected_id = data[0]

                # Isi input form secara otomatis
                self.view.entry_judul.delete(0, 'end')
                self.view.entry_judul.insert(0, str(data[1]))

                self.view.entry_penulis.delete(0, 'end')
                self.view.entry_penulis.insert(0, str(data[2]))

                self.view.entry_tahun.delete(0, 'end')
                self.view.entry_tahun.insert(0, str(data[3]))

    def bersihkan_form(self):
        self.selected_id = None
        self.view.entry_judul.delete(0, 'end')
        self.view.entry_penulis.delete(0, 'end')
        self.view.entry_tahun.delete(0, 'end')

    def simpan_data(self):
        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        berhasil = self.model.create_buku(judul, penulis, tahun)

        if berhasil:
            messagebox.showinfo("Sukses", "Data buku berhasil disimpan")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat menyimpan data.")

    def perbarui_data(self):
        if not self.selected_id:
            messagebox.showwarning("Peringatan", "Pilih data buku dari tabel terlebih dahulu!")
            return

        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        berhasil = self.model.update_buku(self.selected_id, judul, penulis, tahun)

        if berhasil:
            messagebox.showinfo("Sukses", "Data buku berhasil diperbarui")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Gagal memperbarui data.")

    def hapus_data(self):
        if not self.selected_id:
            messagebox.showwarning("Peringatan", "Pilih data buku dari tabel terlebih dahulu!")
            return

        konfirmasi = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus data ini?")
        if konfirmasi:
            berhasil = self.model.delete_buku(self.selected_id)

            if berhasil:
                messagebox.showinfo("Sukses", "Data buku berhasil dihapus")
                self.bersihkan_form()
                self.muat_data_tabel()
            else:
                messagebox.showerror("Error", "Gagal menghapus data.")

    def run(self):
        self.view.mainloop()